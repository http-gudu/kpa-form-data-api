from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from bson import ObjectId
from datetime import datetime
from app.database import forms_collection, responses_collection
from app.schemas import (
    BogieChecksheetCreate, 
    WheelSpecificationCreate,
    APIResponse,
    PaginatedResponse,
    ConditionEnum,
    StatusEnum
)

router = APIRouter()

# Helper function to convert ObjectId to string
def obj_id_str(data):
    data["id"] = str(data["_id"])
    del data["_id"]
    return data

@router.post("/api/forms/bogie-checksheet", response_model=APIResponse)
async def create_bogie_checksheet(checksheet_data: BogieChecksheetCreate):
    try:
        data = {
            "bogie_details": checksheet_data.bogie_details.dict(),
            "bogie_checksheet": checksheet_data.bogie_checksheet.dict(),
            "bmbc_checksheet": checksheet_data.bmbc_checksheet.dict(),
            "remarks": checksheet_data.remarks,
            "overall_status": "COMPLETED",
            "created_at": datetime.utcnow()
        }
        result = await forms_collection.insert_one(data)
        return APIResponse(
            success=True,
            message="Bogie checksheet created successfully",
            data={
                "id": str(result.inserted_id),
                "bogie_number": data["bogie_details"]["bogie_number"],
                "coach_number": data["bogie_details"]["coach_number"],
                "created_at": data["created_at"].isoformat()
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create checksheet: {str(e)}")


@router.post("/api/forms/wheel-specifications", response_model=APIResponse)
async def create_wheel_specification(wheel_data: WheelSpecificationCreate):
    try:
        existing = await responses_collection.find_one({"wheel_number": wheel_data.wheel_number})
        if existing:
            raise HTTPException(status_code=400, detail="Wheel number already exists")
        
        wheel_doc = wheel_data.dict()
        wheel_doc["created_at"] = datetime.utcnow()
        wheel_doc["updated_at"] = datetime.utcnow()
        
        result = await responses_collection.insert_one(wheel_doc)
        
        return APIResponse(
            success=True,
            message="Wheel specification created successfully",
            data={
                "id": str(result.inserted_id),
                "wheel_number": wheel_data.wheel_number,
                "coach_number": wheel_data.coach_number,
                "created_at": wheel_doc["created_at"].isoformat()
            }
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create wheel spec: {str(e)}")


@router.get("/api/forms/wheel-specifications", response_model=PaginatedResponse)
async def get_wheel_specifications(
    wheel_number: Optional[str] = Query(None),
    coach_number: Optional[str] = Query(None),
    condition: Optional[ConditionEnum] = Query(None),
    manufacturer: Optional[str] = Query(None),
    status: Optional[StatusEnum] = Query(None),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0)
):
    try:
        filters = {}
        if wheel_number:
            filters["wheel_number"] = {"$regex": wheel_number, "$options": "i"}
        if coach_number:
            filters["coach_number"] = {"$regex": coach_number, "$options": "i"}
        if condition:
            filters["condition"] = condition
        if manufacturer:
            filters["manufacturer"] = {"$regex": manufacturer, "$options": "i"}
        if status:
            filters["status"] = status

        cursor = responses_collection.find(filters).skip(offset).limit(limit)
        wheels = []
        async for doc in cursor:
            doc = obj_id_str(doc)
            if "created_at" in doc:
                doc["created_at"] = doc["created_at"].isoformat()
            if "updated_at" in doc:
                doc["updated_at"] = doc["updated_at"].isoformat()
            wheels.append(doc)
        
        total = await responses_collection.count_documents(filters)
        
        return PaginatedResponse(
            success=True,
            message=f"Retrieved {len(wheels)} wheel specifications",
            data=wheels,
            total=total,
            limit=limit,
            offset=offset
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch data: {str(e)}")

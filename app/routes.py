from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.models import BogieChecksheet, WheelSpecification
from app.schemas import (
    BogieChecksheetCreate, 
    BogieChecksheetResponse,
    WheelSpecificationCreate,
    WheelSpecificationResponse,
    WheelSpecificationFilters,
    APIResponse,
    PaginatedResponse,
    ConditionEnum,
    StatusEnum
)

router = APIRouter()

@router.post("/api/forms/bogie-checksheet", response_model=APIResponse)
async def create_bogie_checksheet(
    checksheet_data: BogieChecksheetCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new bogie checksheet entry
    
    This endpoint accepts bogie inspection data including:
    - Bogie details (number, coach, inspection date, inspector)
    - Bogie checksheet conditions
    - BMBC checksheet conditions
    """
    try:
        # Create new bogie checksheet record
        db_checksheet = BogieChecksheet(
            # Bogie details
            bogie_number=checksheet_data.bogie_details.bogie_number,
            coach_number=checksheet_data.bogie_details.coach_number,
            inspection_date=checksheet_data.bogie_details.inspection_date,
            inspector_name=checksheet_data.bogie_details.inspector_name,
            
            # Bogie checksheet
            bogie_frame_condition=checksheet_data.bogie_checksheet.bogie_frame_condition,
            bolster=checksheet_data.bogie_checksheet.bolster,
            bolster_suspension_bracket=checksheet_data.bogie_checksheet.bolster_suspension_bracket,
            axle_guide=checksheet_data.bogie_checksheet.axle_guide,
            lower_spring_seat=checksheet_data.bogie_checksheet.lower_spring_seat,
            
            # BMBC checksheet
            adjusting_tube=checksheet_data.bmbc_checksheet.adjusting_tube,
            cylinder_body=checksheet_data.bmbc_checksheet.cylinder_body,
            piston_trunnion=checksheet_data.bmbc_checksheet.piston_trunnion,
            plunger_spring=checksheet_data.bmbc_checksheet.plunger_spring,
            
            # Additional fields
            remarks=checksheet_data.remarks,
            overall_status="COMPLETED"
        )
        
        db.add(db_checksheet)
        db.commit()
        db.refresh(db_checksheet)
        
        return APIResponse(
            success=True,
            message="Bogie checksheet created successfully",
            data={
                "id": db_checksheet.id,
                "bogie_number": db_checksheet.bogie_number,
                "coach_number": db_checksheet.coach_number,
                "created_at": db_checksheet.created_at.isoformat()
            }
        )
        
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Failed to create bogie checksheet: {str(e)}"
        )

@router.get("/api/forms/wheel-specifications", response_model=PaginatedResponse)
async def get_wheel_specifications(
    wheel_number: Optional[str] = Query(None, description="Filter by wheel number"),
    coach_number: Optional[str] = Query(None, description="Filter by coach number"),
    condition: Optional[ConditionEnum] = Query(None, description="Filter by wheel condition"),
    manufacturer: Optional[str] = Query(None, description="Filter by manufacturer"),
    status: Optional[StatusEnum] = Query(None, description="Filter by status"),
    limit: int = Query(10, ge=1, le=100, description="Number of records to return"),
    offset: int = Query(0, ge=0, description="Number of records to skip"),
    db: Session = Depends(get_db)
):
    """
    Get wheel specifications with optional filtering
    
    This endpoint returns wheel specification data with support for:
    - Filtering by wheel number, coach number, condition, manufacturer, status
    - Pagination with limit and offset
    - Complete wheel measurement and inspection data
    """
    try:
        # Build query with filters
        query = db.query(WheelSpecification)
        
        if wheel_number:
            query = query.filter(WheelSpecification.wheel_number.ilike(f"%{wheel_number}%"))
        
        if coach_number:
            query = query.filter(WheelSpecification.coach_number.ilike(f"%{coach_number}%"))
            
        if condition:
            query = query.filter(WheelSpecification.condition == condition)
            
        if manufacturer:
            query = query.filter(WheelSpecification.manufacturer.ilike(f"%{manufacturer}%"))
            
        if status:
            query = query.filter(WheelSpecification.status == status)
        
        # Get total count for pagination
        total = query.count()
        
        # Apply pagination
        wheel_specs = query.offset(offset).limit(limit).all()
        
        # Convert to response format
        wheel_data = []
        for spec in wheel_specs:
            wheel_data.append({
                "id": spec.id,
                "wheel_number": spec.wheel_number,
                "axle_number": spec.axle_number,
                "coach_number": spec.coach_number,
                "position": spec.position,
                "wheel_diameter": spec.wheel_diameter,
                "rim_thickness": spec.rim_thickness,
                "flange_height": spec.flange_height,
                "flange_thickness": spec.flange_thickness,
                "condition": spec.condition,
                "wear_pattern": spec.wear_pattern,
                "cracks_detected": spec.cracks_detected,
                "manufacturer": spec.manufacturer,
                "manufacture_date": spec.manufacture_date.isoformat() if spec.manufacture_date else None,
                "material_grade": spec.material_grade,
                "last_inspection_date": spec.last_inspection_date.isoformat() if spec.last_inspection_date else None,
                "next_inspection_due": spec.next_inspection_due.isoformat() if spec.next_inspection_due else None,
                "inspector_name": spec.inspector_name,
                "load_capacity": spec.load_capacity,
                "speed_rating": spec.speed_rating,
                "remarks": spec.remarks,
                "status": spec.status,
                "created_at": spec.created_at.isoformat(),
                "updated_at": spec.updated_at.isoformat()
            })
        
        return PaginatedResponse(
            success=True,
            message=f"Retrieved {len(wheel_data)} wheel specifications",
            data=wheel_data,
            total=total,
            limit=limit,
            offset=offset
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to retrieve wheel specifications: {str(e)}"
        )

@router.post("/api/forms/wheel-specifications", response_model=APIResponse)
async def create_wheel_specification(
    wheel_data: WheelSpecificationCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new wheel specification entry
    
    This endpoint accepts wheel specification data including:
    - Wheel identification and measurements
    - Condition and inspection details
    - Manufacturing information
    """
    try:
        # Check if wheel number already exists
        existing_wheel = db.query(WheelSpecification).filter(
            WheelSpecification.wheel_number == wheel_data.wheel_number
        ).first()
        
        if existing_wheel:
            raise HTTPException(
                status_code=400,
                detail=f"Wheel number {wheel_data.wheel_number} already exists"
            )
        
        # Create new wheel specification record
        db_wheel = WheelSpecification(**wheel_data.dict())
        
        db.add(db_wheel)
        db.commit()
        db.refresh(db_wheel)
        
        return APIResponse(
            success=True,
            message="Wheel specification created successfully",
            data={
                "id": db_wheel.id,
                "wheel_number": db_wheel.wheel_number,
                "coach_number": db_wheel.coach_number,
                "created_at": db_wheel.created_at.isoformat()
            }
        )
        
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Failed to create wheel specification: {str(e)}"
        )

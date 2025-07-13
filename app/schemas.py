from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List
from enum import Enum

# Enums
class ConditionEnum(str, Enum):
    GOOD = "GOOD"
    WORN_OUT = "WORN OUT"
    DAMAGED = "DAMAGED"
    CRACKED = "CRACKED"
    WORN = "WORN"

class PositionEnum(str, Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"

class StatusEnum(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    RETIRED = "RETIRED"

# Bogie Checksheet Schemas
class BogieDetailsSchema(BaseModel):
    bogie_number: str = Field(..., min_length=1, max_length=50)
    coach_number: str = Field(..., min_length=1, max_length=50)
    inspection_date: datetime
    inspector_name: str = Field(..., min_length=1, max_length=100)

class BogieChecksheetSchema(BaseModel):
    bogie_frame_condition: Optional[ConditionEnum] = None
    bolster: Optional[ConditionEnum] = None
    bolster_suspension_bracket: Optional[ConditionEnum] = None
    axle_guide: Optional[ConditionEnum] = None
    lower_spring_seat: Optional[ConditionEnum] = None

class BmbcChecksheetSchema(BaseModel):
    adjusting_tube: Optional[ConditionEnum] = None
    cylinder_body: Optional[ConditionEnum] = None
    piston_trunnion: Optional[ConditionEnum] = None
    plunger_spring: Optional[ConditionEnum] = None

class BogieChecksheetCreate(BaseModel):
    bogie_details: BogieDetailsSchema
    bogie_checksheet: BogieChecksheetSchema
    bmbc_checksheet: BmbcChecksheetSchema
    remarks: Optional[str] = None

class BogieChecksheetResponse(BaseModel):
    id: Optional[str]
    created_at: datetime
    bogie_number: str
    coach_number: str
    inspection_date: datetime
    inspector_name: str
    bogie_frame_condition: Optional[str]
    bolster: Optional[str]
    bolster_suspension_bracket: Optional[str]
    axle_guide: Optional[str]
    lower_spring_seat: Optional[str]
    adjusting_tube: Optional[str]
    cylinder_body: Optional[str]
    piston_trunnion: Optional[str]
    plunger_spring: Optional[str]
    remarks: Optional[str]
    overall_status: str

# Wheel Specification Schemas
class WheelSpecificationCreate(BaseModel):
    wheel_number: str = Field(..., min_length=1, max_length=50)
    axle_number: str = Field(..., min_length=1, max_length=50)
    coach_number: str = Field(..., min_length=1, max_length=50)
    position: Optional[PositionEnum] = None
    wheel_diameter: float = Field(..., gt=0)
    rim_thickness: Optional[float] = Field(None, gt=0)
    flange_height: Optional[float] = Field(None, gt=0)
    flange_thickness: Optional[float] = Field(None, gt=0)
    condition: Optional[ConditionEnum] = ConditionEnum.GOOD
    wear_pattern: Optional[str] = Field(None, max_length=100)
    cracks_detected: Optional[bool] = False
    manufacturer: Optional[str] = Field(None, max_length=100)
    manufacture_date: Optional[datetime] = None
    material_grade: Optional[str] = Field(None, max_length=50)
    last_inspection_date: Optional[datetime] = None
    next_inspection_due: Optional[datetime] = None
    inspector_name: Optional[str] = Field(None, max_length=100)
    load_capacity: Optional[float] = Field(None, gt=0)
    speed_rating: Optional[str] = Field(None, max_length=20)
    remarks: Optional[str] = None
    status: Optional[StatusEnum] = StatusEnum.ACTIVE

class WheelSpecificationResponse(BaseModel):
    id: Optional[str]
    created_at: datetime
    updated_at: datetime
    wheel_number: str
    axle_number: str
    coach_number: str
    position: Optional[str]
    wheel_diameter: float
    rim_thickness: Optional[float]
    flange_height: Optional[float]
    flange_thickness: Optional[float]
    condition: Optional[str]
    wear_pattern: Optional[str]
    cracks_detected: Optional[bool]
    manufacturer: Optional[str]
    manufacture_date: Optional[datetime]
    material_grade: Optional[str]
    last_inspection_date: Optional[datetime]
    next_inspection_due: Optional[datetime]
    inspector_name: Optional[str]
    load_capacity: Optional[float]
    speed_rating: Optional[str]
    remarks: Optional[str]
    status: Optional[str]

# Filters for query
class WheelSpecificationFilters(BaseModel):
    wheel_number: Optional[str] = None
    coach_number: Optional[str] = None
    condition: Optional[ConditionEnum] = None
    manufacturer: Optional[str] = None
    status: Optional[StatusEnum] = None
    limit: Optional[int] = Field(10, ge=1, le=100)
    offset: Optional[int] = Field(0, ge=0)

# API response models
class APIResponse(BaseModel):
    success: bool
    message: str
    data: Optional[dict] = None

class PaginatedResponse(BaseModel):
    success: bool
    message: str
    data: List[dict]
    total: int
    limit: int
    offset: int

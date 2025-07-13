from sqlalchemy import Column, Integer, String, DateTime, Text, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class BogieChecksheet(Base):
    __tablename__ = "bogie_checksheets"
    
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    # Bogie Details
    bogie_number = Column(String(50), nullable=False)
    coach_number = Column(String(50), nullable=False)
    inspection_date = Column(DateTime, nullable=False)
    inspector_name = Column(String(100), nullable=False)
    
    # Bogie Checksheet Fields
    bogie_frame_condition = Column(String(50))
    bolster = Column(String(50))
    bolster_suspension_bracket = Column(String(50))
    axle_guide = Column(String(50))
    lower_spring_seat = Column(String(50))
    
    # BMBC Checksheet Fields
    adjusting_tube = Column(String(50))
    cylinder_body = Column(String(50))
    piston_trunnion = Column(String(50))
    plunger_spring = Column(String(50))
    
    # Additional fields
    remarks = Column(Text)
    overall_status = Column(String(20), default="PENDING")

class WheelSpecification(Base):
    __tablename__ = "wheel_specifications"
    
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    # Wheel identification
    wheel_number = Column(String(50), nullable=False, unique=True)
    axle_number = Column(String(50), nullable=False)
    coach_number = Column(String(50), nullable=False)
    position = Column(String(20))  # LEFT/RIGHT
    
    # Wheel measurements
    wheel_diameter = Column(Float, nullable=False)
    rim_thickness = Column(Float)
    flange_height = Column(Float)
    flange_thickness = Column(Float)
    
    # Wheel condition
    condition = Column(String(50), default="GOOD")
    wear_pattern = Column(String(100))
    cracks_detected = Column(Boolean, default=False)
    
    # Manufacturing details
    manufacturer = Column(String(100))
    manufacture_date = Column(DateTime)
    material_grade = Column(String(50))
    
    # Inspection details
    last_inspection_date = Column(DateTime)
    next_inspection_due = Column(DateTime)
    inspector_name = Column(String(100))
    
    # Additional specifications
    load_capacity = Column(Float)
    speed_rating = Column(String(20))
    remarks = Column(Text)
    status = Column(String(20), default="ACTIVE")

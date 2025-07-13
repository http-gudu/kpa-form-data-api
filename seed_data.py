#!/usr/bin/env python3
"""
Database seeding script for KPA Form Data API
Populates the database with sample data for testing and demonstration
"""

import os
import sys
from datetime import datetime, timedelta
from sqlalchemy.orm import Session

# Add the app directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from app.database import SessionLocal, engine
from app.models import Base, BogieChecksheet, WheelSpecification

def create_tables():
    """Create all database tables"""
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created successfully")

def seed_bogie_checksheets(db: Session):
    """Seed bogie checksheet data"""
    print("🚂 Seeding bogie checksheet data...")
    
    bogie_checksheets = [
        {
            "bogie_number": "BG001",
            "coach_number": "CH001",
            "inspection_date": datetime.now() - timedelta(days=1),
            "inspector_name": "John Doe",
            "bogie_frame_condition": "GOOD",
            "bolster": "GOOD",
            "bolster_suspension_bracket": "WORN",
            "axle_guide": "GOOD",
            "lower_spring_seat": "GOOD",
            "adjusting_tube": "GOOD",
            "cylinder_body": "GOOD",
            "piston_trunnion": "WORN",
            "plunger_spring": "GOOD",
            "remarks": "Regular inspection completed. Minor wear on suspension bracket.",
            "overall_status": "COMPLETED"
        },
        {
            "bogie_number": "BG002",
            "coach_number": "CH002",
            "inspection_date": datetime.now() - timedelta(days=2),
            "inspector_name": "Jane Smith",
            "bogie_frame_condition": "GOOD",
            "bolster": "WORN",
            "bolster_suspension_bracket": "CRACKED",
            "axle_guide": "DAMAGED",
            "lower_spring_seat": "GOOD",
            "adjusting_tube": "WORN OUT",
            "cylinder_body": "GOOD",
            "piston_trunnion": "GOOD",
            "plunger_spring": "DAMAGED",
            "remarks": "Multiple issues found. Requires immediate maintenance.",
            "overall_status": "NEEDS_REPAIR"
        },
        {
            "bogie_number": "BG003",
            "coach_number": "CH003",
            "inspection_date": datetime.now() - timedelta(days=3),
            "inspector_name": "Mike Johnson",
            "bogie_frame_condition": "GOOD",
            "bolster": "GOOD",
            "bolster_suspension_bracket": "GOOD",
            "axle_guide": "GOOD",
            "lower_spring_seat": "WORN",
            "adjusting_tube": "GOOD",
            "cylinder_body": "WORN",
            "piston_trunnion": "GOOD",
            "plunger_spring": "GOOD",
            "remarks": "Minor wear on spring seat and cylinder body. Scheduled for next maintenance cycle.",
            "overall_status": "COMPLETED"
        },
        {
            "bogie_number": "BG004",
            "coach_number": "CH004",
            "inspection_date": datetime.now() - timedelta(days=5),
            "inspector_name": "Sarah Wilson",
            "bogie_frame_condition": "WORN",
            "bolster": "GOOD",
            "bolster_suspension_bracket": "GOOD",
            "axle_guide": "GOOD",
            "lower_spring_seat": "GOOD",
            "adjusting_tube": "GOOD",
            "cylinder_body": "GOOD",
            "piston_trunnion": "GOOD",
            "plunger_spring": "GOOD",
            "remarks": "Bogie frame showing wear patterns. Monitor for next inspection.",
            "overall_status": "COMPLETED"
        },
        {
            "bogie_number": "BG005",
            "coach_number": "CH005",
            "inspection_date": datetime.now() - timedelta(hours=6),
            "inspector_name": "David Brown",
            "bogie_frame_condition": "GOOD",
            "bolster": "GOOD",
            "bolster_suspension_bracket": "GOOD",
            "axle_guide": "GOOD",
            "lower_spring_seat": "GOOD",
            "adjusting_tube": "GOOD",
            "cylinder_body": "GOOD",
            "piston_trunnion": "GOOD",
            "plunger_spring": "GOOD",
            "remarks": "Excellent condition. All components within specifications.",
            "overall_status": "COMPLETED"
        }
    ]
    
    for checksheet_data in bogie_checksheets:
        checksheet = BogieChecksheet(**checksheet_data)
        db.add(checksheet)
    
    db.commit()
    print(f"✅ Added {len(bogie_checksheets)} bogie checksheet records")

def seed_wheel_specifications(db: Session):
    """Seed wheel specification data"""
    print("🎡 Seeding wheel specification data...")
    
    wheel_specifications = [
        {
            "wheel_number": "WH001",
            "axle_number": "AX001",
            "coach_number": "CH001",
            "position": "LEFT",
            "wheel_diameter": 915.0,
            "rim_thickness": 28.0,
            "flange_height": 25.0,
            "flange_thickness": 32.0,
            "condition": "GOOD",
            "wear_pattern": "Normal wear",
            "cracks_detected": False,
            "manufacturer": "ABC Wheels Ltd",
            "manufacture_date": datetime(2024, 1, 15),
            "material_grade": "R7",
            "last_inspection_date": datetime.now() - timedelta(days=30),
            "next_inspection_due": datetime.now() + timedelta(days=60),
            "inspector_name": "John Doe",
            "load_capacity": 22500.0,
            "speed_rating": "200 km/h",
            "remarks": "Wheel in excellent condition",
            "status": "ACTIVE"
        },
        {
            "wheel_number": "WH002",
            "axle_number": "AX001",
            "coach_number": "CH001",
            "position": "RIGHT",
            "wheel_diameter": 913.5,
            "rim_thickness": 27.5,
            "flange_height": 24.8,
            "flange_thickness": 31.5,
            "condition": "WORN",
            "wear_pattern": "Even wear",
            "cracks_detected": False,
            "manufacturer": "ABC Wheels Ltd",
            "manufacture_date": datetime(2024, 1, 15),
            "material_grade": "R7",
            "last_inspection_date": datetime.now() - timedelta(days=30),
            "next_inspection_due": datetime.now() + timedelta(days=30),
            "inspector_name": "John Doe",
            "load_capacity": 22500.0,
            "speed_rating": "200 km/h",
            "remarks": "Minor wear detected, within acceptable limits",
            "status": "ACTIVE"
        },
        {
            "wheel_number": "WH003",
            "axle_number": "AX002",
            "coach_number": "CH002",
            "position": "LEFT",
            "wheel_diameter": 910.0,
            "rim_thickness": 26.0,
            "flange_height": 23.5,
            "flange_thickness": 30.0,
            "condition": "WORN OUT",
            "wear_pattern": "Irregular wear",
            "cracks_detected": True,
            "manufacturer": "XYZ Rail Components",
            "manufacture_date": datetime(2023, 6, 10),
            "material_grade": "R8",
            "last_inspection_date": datetime.now() - timedelta(days=15),
            "next_inspection_due": datetime.now() + timedelta(days=7),
            "inspector_name": "Jane Smith",
            "load_capacity": 22500.0,
            "speed_rating": "200 km/h",
            "remarks": "Immediate replacement required due to cracks",
            "status": "INACTIVE"
        },
        {
            "wheel_number": "WH004",
            "axle_number": "AX002",
            "coach_number": "CH002",
            "position": "RIGHT",
            "wheel_diameter": 912.0,
            "rim_thickness": 27.0,
            "flange_height": 24.2,
            "flange_thickness": 31.0,
            "condition": "GOOD",
            "wear_pattern": "Minimal wear",
            "cracks_detected": False,
            "manufacturer": "XYZ Rail Components",
            "manufacture_date": datetime(2023, 6, 10),
            "material_grade": "R8",
            "last_inspection_date": datetime.now() - timedelta(days=15),
            "next_inspection_due": datetime.now() + timedelta(days=75),
            "inspector_name": "Jane Smith",
            "load_capacity": 22500.0,
            "speed_rating": "200 km/h",
            "remarks": "Good condition, continue monitoring",
            "status": "ACTIVE"
        },
        {
            "wheel_number": "WH005",
            "axle_number": "AX003",
            "coach_number": "CH003",
            "position": "LEFT",
            "wheel_diameter": 914.0,
            "rim_thickness": 27.8,
            "flange_height": 24.9,
            "flange_thickness": 31.8,
            "condition": "GOOD",
            "wear_pattern": "Normal wear",
            "cracks_detected": False,
            "manufacturer": "Premier Rail Works",
            "manufacture_date": datetime(2024, 3, 20),
            "material_grade": "R7",
            "last_inspection_date": datetime.now() - timedelta(days=45),
            "next_inspection_due": datetime.now() + timedelta(days=45),
            "inspector_name": "Mike Johnson",
            "load_capacity": 22500.0,
            "speed_rating": "200 km/h",
            "remarks": "New wheel performing well",
            "status": "ACTIVE"
        },
        {
            "wheel_number": "WH006",
            "axle_number": "AX003",
            "coach_number": "CH003",
            "position": "RIGHT",
            "wheel_diameter": 914.2,
            "rim_thickness": 28.0,
            "flange_height": 25.0,
            "flange_thickness": 32.0,
            "condition": "GOOD",
            "wear_pattern": "Normal wear",
            "cracks_detected": False,
            "manufacturer": "Premier Rail Works",
            "manufacture_date": datetime(2024, 3, 20),
            "material_grade": "R7",
            "last_inspection_date": datetime.now() - timedelta(days=45),
            "next_inspection_due": datetime.now() + timedelta(days=45),
            "inspector_name": "Mike Johnson",
            "load_capacity": 22500.0,
            "speed_rating": "200 km/h",
            "remarks": "New wheel performing excellently",
            "status": "ACTIVE"
        },
        {
            "wheel_number": "WH007",
            "axle_number": "AX004",
            "coach_number": "CH004",
            "position": "LEFT",
            "wheel_diameter": 908.0,
            "rim_thickness": 25.0,
            "flange_height": 22.5,
            "flange_thickness": 29.0,
            "condition": "DAMAGED",
            "wear_pattern": "Severe wear",
            "cracks_detected": True,
            "manufacturer": "Old Rail Co",
            "manufacture_date": datetime(2022, 8, 5),
            "material_grade": "R6",
            "last_inspection_date": datetime.now() - timedelta(days=10),
            "next_inspection_due": datetime.now() - timedelta(days=5),
            "inspector_name": "Sarah Wilson",
            "load_capacity": 22500.0,
            "speed_rating": "200 km/h",
            "remarks": "Critical condition - immediate replacement required",
            "status": "RETIRED"
        },
        {
            "wheel_number": "WH008",
            "axle_number": "AX004",
            "coach_number": "CH004",
            "position": "RIGHT",
            "wheel_diameter": 911.0,
            "rim_thickness": 26.5,
            "flange_height": 23.8,
            "flange_thickness": 30.5,
            "condition": "WORN",
            "wear_pattern": "Uneven wear",
            "cracks_detected": False,
            "manufacturer": "Old Rail Co",
            "manufacture_date": datetime(2022, 8, 5),
            "material_grade": "R6",
            "last_inspection_date": datetime.now() - timedelta(days=10),
            "next_inspection_due": datetime.now() + timedelta(days=20),
            "inspector_name": "Sarah Wilson",
            "load_capacity": 22500.0,
            "speed_rating": "200 km/h",
            "remarks": "Showing wear patterns, monitor closely",
            "status": "ACTIVE"
        }
    ]
    
    for wheel_data in wheel_specifications:
        wheel = WheelSpecification(**wheel_data)
        db.add(wheel)
    
    db.commit()
    print(f"✅ Added {len(wheel_specifications)} wheel specification records")

def main():
    """Main seeding function"""
    print("🌱 Starting database seeding process...")
    
    # Create database session
    db = SessionLocal()
    
    try:
        # Create tables if they don't exist
        create_tables()
        
        # Check if data already exists
        existing_bogies = db.query(BogieChecksheet).count()
        existing_wheels = db.query(WheelSpecification).count()
        
        if existing_bogies > 0 or existing_wheels > 0:
            print(f"⚠️  Existing data found: {existing_bogies} bogie checksheets, {existing_wheels} wheel specifications")
            response = input("Do you want to continue and add more sample data? (y/N): ")
            if response.lower() != 'y':
                print("❌ Seeding cancelled")
                return
        
        # Seed the data
        seed_bogie_checksheets(db)
        seed_wheel_specifications(db)
        
        # Print summary
        total_bogies = db.query(BogieChecksheet).count()
        total_wheels = db.query(WheelSpecification).count()
        
        print("\n🎉 Database seeding completed successfully!")
        print(f"📊 Total records in database:")
        print(f"   - Bogie Checksheets: {total_bogies}")
        print(f"   - Wheel Specifications: {total_wheels}")
        print(f"\n🚀 You can now start the API server and test the endpoints!")
        print(f"   - Start server: python -m app.main")
        print(f"   - API Docs: http://localhost:8000/docs")
        print(f"   - Health Check: http://localhost:8000/")
        
    except Exception as e:
        print(f"❌ Error during seeding: {str(e)}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()

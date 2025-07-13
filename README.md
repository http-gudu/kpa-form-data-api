# KPA Form Data API

A FastAPI backend service implementing bogie checksheet and wheel specification management APIs for railway maintenance operations.

## Features

- **Bogie Checksheet Management**: Create and manage bogie inspection records
- **Wheel Specifications**: CRUD operations with advanced filtering capabilities
- **PostgreSQL Integration**: Robust database storage with SQLAlchemy ORM
- **Input Validation**: Comprehensive data validation using Pydantic schemas
- **Auto-generated Documentation**: Swagger UI and ReDoc available
- **RESTful API Design**: Following REST principles with proper HTTP status codes

## API Endpoints

### 1. POST /api/forms/bogie-checksheet
Creates a new bogie checksheet entry with inspection data.

**Request Body:**
```json
{
  "bogie_details": {
    "bogie_number": "BG001",
    "coach_number": "CH001",
    "inspection_date": "2025-07-13T10:00:00",
    "inspector_name": "John Doe"
  },
  "bogie_checksheet": {
    "bogie_frame_condition": "GOOD",
    "bolster": "GOOD",
    "bolster_suspension_bracket": "CRACKED",
    "axle_guide": "WORN",
    "lower_spring_seat": "GOOD"
  },
  "bmbc_checksheet": {
    "adjusting_tube": "DAMAGED",
    "cylinder_body": "WORN OUT",
    "piston_trunnion": "GOOD",
    "plunger_spring": "GOOD"
  },
  "remarks": "Inspection completed successfully"
}

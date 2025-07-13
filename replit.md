# KPA Form Data API - System Architecture

## Overview

This is a FastAPI-based backend service for railway maintenance operations, specifically designed to manage bogie checksheets and wheel specifications. The application provides a RESTful API for recording and retrieving inspection data, with comprehensive validation and database persistence.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Backend Framework
- **FastAPI**: Modern, fast web framework for building APIs with Python
- **Rationale**: Chosen for automatic API documentation, built-in validation, and high performance
- **Benefits**: Auto-generated Swagger UI, type hints support, async capabilities

### Database Layer
- **PostgreSQL**: Primary database for data persistence
- **SQLAlchemy ORM**: Object-relational mapping for database operations
- **Rationale**: PostgreSQL provides ACID compliance and robust data integrity for critical railway maintenance records
- **Connection Management**: Uses connection pooling with StaticPool for efficient database connections

### Data Validation
- **Pydantic**: Schema validation and serialization
- **Custom Enums**: Predefined condition states (GOOD, WORN, DAMAGED, etc.)
- **Field Validation**: Length constraints, required fields, and type checking

## Key Components

### 1. Database Models (`app/models.py`)
- **BogieChecksheet**: Main inspection record model with bogie details, checksheet conditions, and BMBC data
- **WheelSpecification**: Wheel measurement and specification tracking
- **Audit Fields**: Automatic created_at and updated_at timestamps

### 2. API Schemas (`app/schemas.py`)
- **Nested Validation**: Separate schemas for bogie details, checksheet data, and BMBC data
- **Enum Validation**: Standardized condition values
- **Response Models**: Structured API responses with proper typing

### 3. Route Handlers (`app/routes.py`)
- **POST /api/forms/bogie-checksheet**: Create new inspection records
- **Wheel Specifications API**: CRUD operations with filtering capabilities
- **Error Handling**: Proper HTTP status codes and error responses

### 4. Database Configuration (`app/database.py`)
- **Environment-based Configuration**: Database URL from environment variables
- **Connection Pooling**: Optimized database connections
- **Session Management**: Proper database session lifecycle

## Data Flow

1. **Request Reception**: FastAPI receives HTTP requests with JSON payloads
2. **Validation**: Pydantic schemas validate incoming data structure and types
3. **Business Logic**: Route handlers process validated data
4. **Database Operations**: SQLAlchemy ORM performs database CRUD operations
5. **Response Formation**: Structured JSON responses with proper status codes

## External Dependencies

### Core Dependencies
- **FastAPI**: Web framework and API server
- **SQLAlchemy**: Database ORM and connection management
- **Pydantic**: Data validation and serialization
- **PostgreSQL Driver**: Database connectivity

### Development Tools
- **Uvicorn**: ASGI server for running the application
- **Postman Collection**: API testing and documentation

## Deployment Strategy

### Environment Configuration
- **Database URL**: Configurable via environment variables
- **CORS Configuration**: Currently set to allow all origins (needs production hardening)
- **Auto-generated Documentation**: Available at `/docs` and `/redoc` endpoints

### Database Management
- **Auto Migration**: Tables created automatically on startup
- **Seed Data**: Python script available for populating test data
- **Connection Pooling**: Configured for production-ready database connections

### Production Considerations
- **CORS Origins**: Should be restricted to specific domains in production
- **Database Echo**: Currently enabled for debugging, should be disabled in production
- **Error Logging**: Basic error handling implemented, could be enhanced with structured logging

The application follows a clean architecture pattern with clear separation between data models, business logic, and API endpoints, making it maintainable and testable.
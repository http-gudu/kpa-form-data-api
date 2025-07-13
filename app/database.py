import motor.motor_asyncio
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MongoDB Atlas URI from environment
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

# Create MongoDB client
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)

# Access your MongoDB database
db = client.kpa_db

# Collections
forms_collection = db.forms
responses_collection = db.responses

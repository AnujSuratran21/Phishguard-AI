from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import Base, engine

# Import models
from app.models.user import User
from app.models.scan import Scan

# Import routers
from app.api.routes import auth
from app.api.routes import scan
from app.api.routes import history

app = FastAPI(
    title="PhishGuard AI"
)

# Create tables
Base.metadata.create_all(bind=engine)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(scan.router)
app.include_router(history.router)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import admin, books, users, qr, websocket
from app.db import create_tables

app = FastAPI(title="Library Management System", version="1.0.0")

# CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(admin.router, prefix="/admin", tags=["admin"])
app.include_router(books.router, prefix="/books", tags=["books"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(qr.router, prefix="/qr", tags=["qr"])
app.include_router(websocket.router, prefix="/ws", tags=["websocket"])

@app.on_event("startup")
async def startup_event():
    create_tables()
from fastapi import FastAPI
from app.routers.health import health_router

app = FastAPI(title="react ecom")

@app.get("/")
def root():
    return {"message": "welcome"}

app.include_router(prefix="/api/health", router=health_router, tags=["health"])
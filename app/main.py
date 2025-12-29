from fastapi import FastAPI
from app.api.schedule import router as schedule_router
from app.api.analytics import router as analytics_router

app = FastAPI(title="Smart Schedule")

app.include_router(schedule_router)
app.include_router(analytics_router)
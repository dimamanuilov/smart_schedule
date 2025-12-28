from fastapi import FastAPI
from app.api.schedule import router

app = FastAPI(title="Smart Schedule (Local)")
app.include_router(router)

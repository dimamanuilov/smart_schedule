from fastapi import APIRouter
from app.services.product_analytics import feature_usage

router = APIRouter()


@router.get("/analytics/features")
def features():
    return feature_usage()
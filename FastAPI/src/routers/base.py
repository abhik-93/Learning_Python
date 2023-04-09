from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def base_page():
    return {"Welcome to Subscription Home Page"}

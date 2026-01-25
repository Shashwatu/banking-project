from fastapi import APIRouter

router = APIRouter(prefix="/home")

@router.get("/")
def read_root():
    return {"message": "Welcome to the Banking Project"}
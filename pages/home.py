from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db
from crud import get_products
from main import get_current_user

router = APIRouter()

templates = Jinja2Templates(directory="template")

@router.get("/home")
async def home(request: Request, db: Session = Depends(get_db)):
    products = get_products(db)
    return templates.TemplateResponse("home.html", {"request": request, "products": products})

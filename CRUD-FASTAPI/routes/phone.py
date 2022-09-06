from fastapi import APIRouter, Response, status
from config.db import conn
from models.phone import phones
from schemas.phone import Phone
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT

key = Fernet.generate_key()
f = Fernet(key)

phone = APIRouter()

@phone.get("/phones", response_model=list[Phone], tags=["phones"])
def get_phones():
    return conn.execute(phones.select()).fetchall()

@phone.post("/phones", response_model=list[Phone], tags=["phones"])
def create_phone(phone: Phone):
    new_phone = {"brand": phone.brand, "model": phone.model, "price": phone.price, "stock": phone.stock}
    result = conn.execute(phones.insert().values(new_phone))
    
    return conn.execute(phones.select().where(phones.c.id == result.lastrowid)).first()

@phone.get("/phones/{id}", response_model=list[Phone], tags=["phones"])
def get_phone(id: str):
    
    return conn.execute(phones.select().where(phones.c.id == id)).first()

@phone.delete("/phones/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["phones"])
def delete_user(id: str):
    conn.execute(phones.delete().where(phones.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

@phone.put("/phones/{id}", response_model=Phone, tags=["phones"])
def update_user(id: str, phone: Phone):
    conn.execute(phones.update().values(brand=phone.brand,
        model=phone.model, price=phone.price, stock=phone.stock).where(phones.c.id == id))
    return conn.execute(phones.select().where(phones.c.id == id)).first()
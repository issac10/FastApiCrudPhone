from fastapi import FastAPI
from routes.phone import phone

app = FastAPI(

    tittle="My example FASTAPI",
    description="Este es mi capacitacion de FastApi",
    openapi_tags=[{
        "name": "phones",
        "description": "phone routes"
    }]

)

app.include_router(phone)

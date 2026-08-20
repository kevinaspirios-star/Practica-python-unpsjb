from datetime import datetime
from pydantic import BaseModel, PositiveInt, Field, EmailStr
from typing import Annotated

class Estudiante(BaseModel):
    legajo:int
    nombre_completo:Annotated[str,Field (min_length=5)]
    email:EmailStr
    promedio:Annotated[float , Field ( default=0.0, ge=0.0, le=10.0)]


datos= {"legajo": "2345", "nombre_completo": "Kevin Rios", "email": "kevin@gmail.com"}
estd1= Estudiante(**datos)
print(estd1.legajo)
print(estd1.promedio)
datos2= {"legajo": "4567", "nombre_completo": "Facu Rios", "email": "Mati@gmail.com", "promedio": "8"}
estd2= Estudiante(**datos2)
print(estd2.legajo)
print(estd2.promedio)
datos3= {"legajo": "7890", "nombre_completo": "Franco Romero", "email": "franci@gmail.com", "promedio": "9"}
estd3= Estudiante(**datos3)
print(estd3.legajo)
print(estd3.promedio)
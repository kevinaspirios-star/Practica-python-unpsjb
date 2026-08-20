from datetime import datetime
from pydantic import BaseModel, PositiveInt, Field, EmailStr
from typing import Annotated, Optional, Union, Literal

CoordenadaGPS = Annotated[float, Field(ge=-90.0 , le=90.0)]


class Ubicacion(BaseModel):
    latitud: CoordenadaGPS
    longitud: CoordenadaGPS
    etiqueta: Optional[str] = None


datos= {"latitud": "-40.5", "longitud": "30.8"}
ubi1= Ubicacion(**datos)
print(ubi1.longitud)
print(ubi1.latitud)
print(ubi1.etiqueta)

datos2= {"latitud": "-100.5", "longitud": "200.8", "etiqueta":"playa"}
ubi2= Ubicacion(**datos2)
print(ubi2.longitud)
print(ubi2.latitud)
print(ubi2.etiqueta)

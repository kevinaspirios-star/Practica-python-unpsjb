from cmath import e
from datetime import datetime
from pydantic import BaseModel, PositiveInt, Field, EmailStr, ValidationError
from typing import Annotated, Optional, Union, Literal

class UsuarioSistema(BaseModel):
    email: EmailStr
    nivel_acceso: Annotated[int, Field(ge=1,le=5)]



try:
    datos={"email":"kevin@gmail.com", "nivel_acceso":"4"}
    usua1=UsuarioSistema(**datos)
    print(usua1.email)
    print(usua1.nivel_acceso)
    datos2={"email":"Mati@gmail.com", "nivel_acceso":"7"}
    usua2=UsuarioSistema(**datos2)
    print(usua2.email)
    print(usua2.nivel_acceso)
except ValidationError:
    print("Ocurrio un error de validacion")

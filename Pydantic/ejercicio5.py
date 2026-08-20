from cmath import e
from datetime import datetime
from pydantic import BaseModel, PositiveInt, Field, EmailStr, ValidationError
from typing import Annotated, List, Optional, Union, Literal


class PerfilUsuario(BaseModel):
    username: Annotated[str, Field(pattern=r"^[a-z0-9_]{3,20}$")]
    biografia: Optional[str] =Field(default=None,max_length=200)
    redes_sociales: Optional[List[str]] = None


datos={"username": "213khk","redes_sociales":{"pizza","arroz"}}
perfil1= PerfilUsuario(**datos)
print(perfil1.username)
print(perfil1.redes_sociales)
print(perfil1.biografia)

datos2={"username": "4545ls","biografia":"hola"}
perfil2= PerfilUsuario(**datos2)
print(perfil2.username)
print(perfil2.redes_sociales)
print(perfil2.biografia)
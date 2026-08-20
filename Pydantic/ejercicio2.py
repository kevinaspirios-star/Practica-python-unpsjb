from datetime import datetime
from pydantic import BaseModel, PositiveInt, Field, EmailStr
from typing import Annotated, Union, Literal

STATUS = Literal["sensor","actuador","gateway"]
class Dispositivo(BaseModel):
    id_dispositivo: Union[int,str]
    tipo:STATUS

datos= {"id_dispositivo":"14", "tipo":"sensor"}
disp1=Dispositivo(**datos)
print(disp1.id_dispositivo)
print(disp1.tipo)
datos2= {"id_dispositivo":"catorce", "tipo":"actuador"}
disp2=Dispositivo(**datos2)
print(disp2.id_dispositivo)
print(disp2.tipo)
datos3= {"id_dispositivo":"14cat", "tipo":"ninguno"}
disp3=Dispositivo(**datos3)
print(disp3.id_dispositivo)
print(disp3.tipo)
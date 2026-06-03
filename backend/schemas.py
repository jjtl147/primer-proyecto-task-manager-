from pydantic import BaseModel
from datetime import date, time  # ← así, en minúscula

class CrearTarea(BaseModel):
    nombre_tarea: str
    descripcion: str
    fecha_fin: date     #sistema agrega automaticamente (caso no poner nada) o usuario puede establecer
    hora_fin: time
    fecha_inicio: date      #tambien se puede dar la opcion de ahora mismo y el sistema asigna automaticamente
    hora_inicio: time
    estado: str

class RespuestaTarea(BaseModel):
    id: int
    nombre_tarea: str
    descripcion: str
    fecha_inicio: date
    hora_inicio: time
    fecha_fin: date
    hora_fin: time
    estado: str
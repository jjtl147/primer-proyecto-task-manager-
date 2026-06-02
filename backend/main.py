from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
new_tarea = []
class Tarea(BaseModel):
    titulo: str
    estado: str
@app.post("/tareas")
def crear_tarea(datos: Tarea):
    nueva = {
        "id": len(new_tarea) + 1,
        "titulo": datos.titulo,     
        "estado": datos.estado  
    }
    new_tarea.append(nueva)
    return nueva
@app.get("/tareas")
def retornar_tareas():
    return new_tarea
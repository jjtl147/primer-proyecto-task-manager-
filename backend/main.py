from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import engine, SessionLocal

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/tareas")
def mostrarTarea(db: Session = Depends(get_db)):
    mostrarTarea = db.query(models.Tarea).all()
    return mostrarTarea

@app.post("/tareas")
def crearTarea(tarea: schemas.CrearTarea, db: Session = Depends(get_db)):
    nueva_tarea = models.Tarea(
    nombre_tarea = tarea.nombre_tarea,
    descripcion = tarea.descripcion,
    fecha_inicio = tarea.fecha_inicio,
    hora_inicio = tarea.hora_inicio,
    fecha_fin = tarea.fecha_fin,
    hora_fin = tarea.hora_fin,
    estado = tarea.estado
    )
    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)
    return nueva_tarea
from sqlalchemy import Column, Integer, String, Date, Time
from database import Base #from database viene del archivo python donde esta la ruta de la base de datos

class Tarea(Base):
    __tablename__ = "TB_tareas" 
    id = Column(Integer, primary_key=True, index=True)
    nombre_tarea = Column(String, index=True)
    descripcion = Column(String)
    fecha_inicio = Column(Date, index=True)
    hora_inicio = Column(Time, index=True)
    fecha_fin = Column(Date, index=True)
    hora_fin = Column(Time, index=True)
    estado = Column(String, index=True)
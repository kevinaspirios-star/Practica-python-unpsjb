from datetime import date, datetime, timezone
from email.headerregistry import Address
from typing import List, Optional
from sqlalchemy import ForeignKey, String, engine, create_engine, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase, Session, relationship, Mapped, mapped_column
from datetime import date
from sqlalchemy import Table, Column, ForeignKey, String, Float, Date
from sqlalchemy import func

engine = create_engine("sqlite://", echo=True)

class Base(DeclarativeBase):
    pass


class Departamento(Base):

    __tablename__= "departamento"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))

    profesor: Mapped[List[Profesor]] = relationship()


class Profesor(Base):

    __tablename__= "profesor"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    email: Mapped[str]
    fecha_ingreso: Mapped[date] = mapped_column(default=date.today)

    departemento_id: Mapped[int] = mapped_column(ForeignKey("departamento.id"))

    departamento: Mapped[Departamento] = relationship(back_populates="profesor")

    cursos: Mapped[List[Curso]] = relationship(back_populates="profesor")

class Inscripcion(Base):

    __tablename__="inscripcion"

    curso_id: Mapped[int] = mapped_column(ForeignKey("curso.id"), primary_key=True)
    estudiante_id: Mapped[int] = mapped_column(ForeignKey("estudiante.id"), primary_key=True)
    fecha_inscripcion: Mapped[date ] = mapped_column(default=date.today())
    calificacion_final: Mapped[float]

    extra_data: Mapped[Optional[str]]

    estudiante: Mapped["Estudiante"] = relationship(back_populates="cursos")
    curso: Mapped["Curso"] = relationship(back_populates="estudiantes")

class Curso(Base):
     
    __tablename__= "curso"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(200))
    creditos: Mapped[float]

    profesor_id: Mapped[int] = mapped_column(ForeignKey("profesor.id"))

    profesor: Mapped[Profesor] = relationship(back_populates="cursos")

    clases: Mapped[List["Clase"]] = relationship()

    estudiantes: Mapped[List["Inscripcion"]] = relationship(back_populates="curso")

class Clase(Base):

    __tablename__="clase"

    id: Mapped[int] = mapped_column(primary_key=True)
    tema: Mapped[str] = mapped_column(String(200))
    duracion_M: Mapped[int]

    curso_id: Mapped[int] = mapped_column(ForeignKey("curso.id"))

class Estudiante(Base):

    __tablename__="estudiante"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(200))
    legajo: Mapped[int]

    cursos: Mapped[List["Inscripcion"]] = relationship(back_populates="estudiante")

Base.metadata.create_all(engine)


def Matricular_Alumno(alumIns,cursoIns,calificacionF,fecha_inscrip=date.today()):

   inscrip=Inscripcion(estudiante= alumIns,curso=cursoIns, fecha_inscripcion=fecha_inscrip, calificacion_final=calificacionF)

   session.add(inscrip)
   session.commit()
   
with Session(engine) as session:

   clase1 = Clase(tema="metodologias",duracion_M=44)
   clase2 = Clase(tema="agiles",duracion_M=44)
   profe1= Profesor(nombre="kevin", email="rioskevin@gmail.com")
   profe2= Profesor(nombre="facu", email="facu@gmail.com")
   profe3= Profesor(nombre="jose", email="jose@gmail.com")
   alum1= Estudiante(nombre="kevin", legajo= 112232)
   curso1= Curso(titulo="software", creditos= 2.45, profesor= profe3, clases=[clase1 ,clase2])
   curso2= Curso(titulo="ingeniero", creditos= 2.45, profesor= profe2, clases=[clase2])
   dep1 = Departamento(nombre="Desarrollo", profesor=[profe1,profe2,profe3])
   session.add(dep1)
   session.commit()

   try:
     Matricular_Alumno(alum1,curso1,6.5)
     Matricular_Alumno(alum1,curso1,9.5)
   except SQLAlchemyError as e:
      session.rollback()
      print(f"error detectado {e}")
      print("rollback ejecutado correctamente")
   stmt = (
    select(Profesor)
    .join(Profesor.cursos)
    .filter(Profesor.id== 2)
)

   profesores = session.scalars(stmt).all()

   print("\n--- LISTA DE PROFESORES ---")
   if not profesores:
    print("No se encontró ningún profesor con ese nombre o no tiene cursos asociados.")
   for p in profesores:
        nombres_cursos = [c.titulo for c in p.cursos] if p.cursos else "Ninguno"
        print(f"ID: {p.id} | Nombre: {p.nombre} | Email: {p.email} | Ingreso: {p.fecha_ingreso} | Departamento: {p.departemento_id} | NombreDep: {p.departamento.nombre} | Curso: {nombres_cursos}")

   stmt = select(Curso)
   cursos= session.scalars(stmt).all()
   for c in cursos:
       nombre_clase= [cl.tema for cl in c.clases] if c.clases else "Ninguno"
       print(f"ID: {c.id} | Titulo: {c.titulo} | Clase: {nombre_clase}")

   stmt = select(Estudiante)
   estudiantes = session.scalars(stmt).all()

   for e in estudiantes:
      for c in e.cursos:
       print(f"Nombre: {e.nombre} | Titulo_Cursos: {c.curso.titulo} | Fecha_d_inscripcion: {c.fecha_inscripcion} |  Calificacion_final: {c.calificacion_final}")

   stmt = (
    select(func.avg(Inscripcion.calificacion_final))
    .where(Inscripcion.estudiante_id == 1)
)

   promedio = session.scalar(stmt)
   print(f"El promedio de calificaciones es: {promedio}")

   stmt = (
    select(Curso.titulo, func.count(Inscripcion.estudiante_id).label("total_estudiantes"))
    .join(Inscripcion, Curso.id == Inscripcion.curso_id)
    .group_by(Curso.id, Curso.titulo)
)
   resultados= session.execute(stmt).all()
   print("\n--- ESTUDIANTES INSCRIPTOS POR CURSO ---")
   for titulo_curso, total in resultados:
    print(f"Curso: {titulo_curso} | Estudiantes_inscriptos: {total}")


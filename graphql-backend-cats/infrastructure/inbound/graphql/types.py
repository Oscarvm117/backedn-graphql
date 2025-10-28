import strawberry
from typing import Optional


@strawberry.type
class StudentType:
    id: int
    nombre: str
    edad: int
    correo: str
    carrera: str
    facultad: str


@strawberry.type
class BreedType:
    id: str
    name: str
    weight: Optional[str] = None
    height: Optional[str] = None
    life_span: Optional[str] = None
    bred_for: Optional[str] = None
    breed_group: Optional[str] = None
    temperament: Optional[str] = None
    origin: Optional[str] = None
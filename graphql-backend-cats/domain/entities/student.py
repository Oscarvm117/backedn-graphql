from dataclasses import dataclass
from typing import Optional


@dataclass
class Student:
    id: int
    nombre: str
    edad: int
    correo: str
    carrera: str
    facultad: str

    @classmethod
    def from_dict(cls, data: dict) -> 'Student':
        return cls(
            id=data.get('id'),
            nombre=data.get('nombre'),
            edad=data.get('edad'),
            correo=data.get('correo'),
            carrera=data.get('carrera'),
            facultad=data.get('facultad')
        )
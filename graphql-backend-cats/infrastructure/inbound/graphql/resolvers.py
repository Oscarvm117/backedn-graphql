from typing import List, Optional
import strawberry
from infrastructure.inbound.graphql.types import StudentType, BreedType
from application.use_cases.get_students import GetStudentsUseCase
from application.use_cases.get_breed import GetBreedUseCase


class Resolvers:
    def __init__(
        self,
        get_students_use_case: GetStudentsUseCase,
        get_breed_use_case: GetBreedUseCase
    ):
        self.get_students_use_case = get_students_use_case
        self.get_breed_use_case = get_breed_use_case

    async def resolve_students(self) -> List[StudentType]:
        """Resolver para obtener todos los estudiantes"""
        students = await self.get_students_use_case.execute()
        
        return [
            StudentType(
                id=student.id,
                nombre=student.nombre,
                edad=student.edad,
                correo=student.correo,
                carrera=student.carrera,
                facultad=student.facultad
            )
            for student in students
        ]

    async def resolve_breed(self, breed_id: str) -> Optional[BreedType]:
        """Resolver para obtener una raza por ID"""
        breed = await self.get_breed_use_case.execute(breed_id)
        
        if not breed:
            return None
        
        return BreedType(
            id=breed.id,
            name=breed.name,
            weight=breed.weight,
            height=breed.height,
            life_span=breed.life_span,
            bred_for=breed.bred_for,
            breed_group=breed.breed_group,
            temperament=breed.temperament,
            origin=breed.origin
        )
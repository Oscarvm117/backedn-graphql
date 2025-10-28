from typing import List
from domain.entities.student import Student
from domain.ports.student_repository import StudentRepository


class GetStudentsUseCase:
    def __init__(self, student_repository: StudentRepository):
        self.student_repository = student_repository

    async def execute(self) -> List[Student]:
        """
        Caso de uso: Obtener todos los estudiantes
        """
        return await self.student_repository.get_all_students()
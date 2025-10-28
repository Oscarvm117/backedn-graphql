from abc import ABC, abstractmethod
from typing import List
from domain.entities.student import Student


class StudentRepository(ABC):
    @abstractmethod
    async def get_all_students(self) -> List[Student]:
        """Obtiene todos los estudiantes de la base de datos"""
        pass
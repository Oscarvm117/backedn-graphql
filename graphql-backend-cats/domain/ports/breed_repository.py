from abc import ABC, abstractmethod
from typing import Optional
from domain.entities.breed import Breed


class BreedRepository(ABC):
    @abstractmethod
    async def get_breed_by_id(self, breed_id: str) -> Optional[Breed]:
        """Obtiene una raza por su ID"""
        pass
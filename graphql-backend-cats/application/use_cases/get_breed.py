from typing import Optional
from domain.entities.breed import Breed
from domain.ports.breed_repository import BreedRepository


class GetBreedUseCase:
    def __init__(self, breed_repository: BreedRepository):
        self.breed_repository = breed_repository

    async def execute(self, breed_id: str) -> Optional[Breed]:
        """
        Caso de uso: Obtener una raza por ID
        """
        if not breed_id:
            raise ValueError("El ID de la raza es requerido")
        
        return await self.breed_repository.get_breed_by_id(breed_id)
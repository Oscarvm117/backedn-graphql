import os
import requests
from typing import Optional
from domain.entities.breed import Breed
from domain.ports.breed_repository import BreedRepository


class CatAPIBreedRepository(BreedRepository):
    def __init__(self):
        self.base_url = os.getenv('CAT_API_URL', 'https://api.thecatapi.com/v1')
        self.api_key = os.getenv('CAT_API_KEY', '')

    async def get_breed_by_id(self, breed_id: str) -> Optional[Breed]:
        """Obtiene información de una raza desde The Cat API"""
        try:
            headers = {}
            if self.api_key:
                headers['x-api-key'] = self.api_key
            
            url = f"{self.base_url}/breeds/{breed_id}"
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                return Breed.from_api_response(data)
            else:
                print(f"Error al consultar raza: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"Error al consultar Cat API: {e}")
            return None
from dataclasses import dataclass
from typing import Optional


@dataclass
class Breed:
    id: str
    name: str
    weight: Optional[str] = None
    height: Optional[str] = None
    life_span: Optional[str] = None
    bred_for: Optional[str] = None
    breed_group: Optional[str] = None
    temperament: Optional[str] = None
    origin: Optional[str] = None

    @classmethod
    def from_api_response(cls, data: dict) -> 'Breed':
        weight = data.get('weight', {})
        weight_str = f"{weight.get('imperial', '')} pounds" if isinstance(weight, dict) else None
        
        height = data.get('height', {})
        height_str = f"{height.get('imperial', '')} inches" if isinstance(height, dict) else None
        
        return cls(
            id=str(data.get('id', '')),
            name=data.get('name', ''),
            weight=weight_str,
            height=height_str,
            life_span=data.get('life_span'),
            bred_for=data.get('bred_for'),
            breed_group=data.get('breed_group'),
            temperament=data.get('temperament'),
            origin=data.get('origin')
        )
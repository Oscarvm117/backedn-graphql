from typing import List, Optional
import strawberry
from infrastructure.inbound.graphql.types import StudentType, BreedType
from infrastructure.inbound.graphql.resolvers import Resolvers

# Variable global para los resolvers
resolvers: Optional[Resolvers] = None


def set_resolvers(resolver_instance: Resolvers):
    """Configura la instancia de resolvers"""
    global resolvers
    resolvers = resolver_instance


@strawberry.type
class Query:
    @strawberry.field
    async def students(self) -> List[StudentType]:
        """Query para obtener todos los estudiantes"""
        if resolvers is None:
            raise Exception("Resolvers no configurados")
        return await resolvers.resolve_students()

    @strawberry.field
    async def breed(self, breed_id: str) -> Optional[BreedType]:
        """Query para obtener una raza por ID"""
        if resolvers is None:
            raise Exception("Resolvers no configurados")
        return await resolvers.resolve_breed(breed_id)


# Crear el schema de GraphQL
schema = strawberry.Schema(query=Query)
import os
from pathlib import Path

# Solo cargar .env si existe (local)
if Path('.env').exists():
    from dotenv import load_dotenv
    load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter

from infrastructure.outbound.database.sqlite_student_repository import SQLiteStudentRepository
from infrastructure.outbound.api.catapi_breed_repository import CatAPIBreedRepository
from application.use_cases.get_students import GetStudentsUseCase
from application.use_cases.get_breed import GetBreedUseCase
from infrastructure.inbound.graphql.resolvers import Resolvers
from infrastructure.inbound.graphql.schema import schema, set_resolvers

# Configuración
DATABASE_URL = os.getenv('DATABASE_URL', 'mi_base_de_datos.db')

print(f"🔍 Using DATABASE_URL: {DATABASE_URL}")

# Inicializar repositorios
student_repository = SQLiteStudentRepository(DATABASE_URL)
breed_repository = CatAPIBreedRepository()

# Inicializar casos de uso
get_students_use_case = GetStudentsUseCase(student_repository)
get_breed_use_case = GetBreedUseCase(breed_repository)

# Inicializar resolvers
resolvers = Resolvers(get_students_use_case, get_breed_use_case)
set_resolvers(resolvers)

# Crear aplicación FastAPI
app = FastAPI(
    title="GraphQL Backend - Cats & Students",
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Agregar ruta GraphQL
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
async def root():
    db_exists = os.path.exists(DATABASE_URL)
    return {
        "message": "GraphQL Backend - Cats & Students API",
        "graphql_endpoint": "/graphql",
        "status": "running",
        "database_exists": db_exists,
        "database_path": DATABASE_URL
    }

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

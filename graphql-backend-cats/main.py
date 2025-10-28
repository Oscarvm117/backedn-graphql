import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter

# Cargar variables de entorno
load_dotenv()

# Importar dependencias
from infrastructure.outbound.database.sqlite_student_repository import SQLiteStudentRepository
from infrastructure.outbound.api.catapi_breed_repository import CatAPIBreedRepository
from application.use_cases.get_students import GetStudentsUseCase
from application.use_cases.get_breed import GetBreedUseCase
from infrastructure.inbound.graphql.resolvers import Resolvers
from infrastructure.inbound.graphql.schema import schema, set_resolvers

# Configuración
DATABASE_URL = os.getenv('DATABASE_URL', 'students.db')
PORT = int(os.getenv('PORT', 8000))

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
app = FastAPI(title="GraphQL Backend - Cats & Students")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especifica los orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Agregar ruta GraphQL
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

# Ruta de health check
@app.get("/")
async def root():
    return {
        "message": "GraphQL Backend - Cats & Students API",
        "graphql_endpoint": "/graphql",
        "status": "running"
    }

@app.get("/health")
async def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)
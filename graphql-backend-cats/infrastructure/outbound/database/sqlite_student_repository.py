import aiosqlite
from typing import List
from domain.entities.student import Student
from domain.ports.student_repository import StudentRepository


class SQLiteStudentRepository(StudentRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path

    async def get_all_students(self) -> List[Student]:
        """Obtiene todos los estudiantes de la base de datos SQLite"""
        students = []
        
        try:
            async with aiosqlite.connect(self.db_path) as db:
                # CAMBIO AQUÍ: students -> usuarios
                async with db.execute(
                    "SELECT id, nombre, edad, correo, carrera, facultad FROM usuarios"
                ) as cursor:
                    rows = await cursor.fetchall()
                    
                    for row in rows:
                        student = Student(
                            id=row[0],
                            nombre=row[1],
                            edad=row[2],
                            correo=row[3],
                            carrera=row[4],
                            facultad=row[5]
                        )
                        students.append(student)
            
            return students
        except Exception as e:
            print(f"Error al consultar estudiantes: {e}")
            return []
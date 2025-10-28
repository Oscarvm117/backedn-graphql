from mangum import Mangum
import sys
import os
from pathlib import Path

# Agregar el directorio raíz al path
root_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, root_dir)

# Asegurarse de que la ruta de la BD sea correcta
db_path = os.path.join(root_dir, 'mi_base_de_datos.db')
os.environ['DATABASE_URL'] = db_path

print(f"🔍 Root dir: {root_dir}")
print(f"🔍 DB path: {db_path}")
print(f"🔍 DB exists: {os.path.exists(db_path)}")

# Importar la app
from main import app

# Handler para Vercel con lifespan off
handler = Mangum(app, lifespan="off")
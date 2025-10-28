from mangum import Mangum
import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Importar la app
from main import app

# Handler para Vercel
handler = Mangum(app, lifespan="off")
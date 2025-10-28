import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from main import app

# Vercel espera que la app se llame 'app' o se exporte como handler
handler = app
import eel
import os
import sys

if getattr(sys, 'frozen', False):
    base_path = os.path.dirname(sys.executable)
    ui_path = sys._MEIPASS 
else:
    base_path = os.path.dirname(os.path.abspath(__file__))
    ui_path = base_path

os.chdir(base_path)
eel.init(ui_path)

# FUNCIÓN PUENTE: Lee el archivo del disco real y lo envía al HTML
@eel.expose
def leer_datos_disco():
    ruta = os.path.join(base_path, 'datos.js')
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            contenido = f.read()
            # Limpiamos el texto para quedarnos solo con el JSON
            json_str = contenido.replace('var datosMuelles = ', '').strip().rstrip(';')
            return json_str
    except Exception as e:
        return None

def cerrar_proceso(route, websockets):
    if not websockets:
        sys.exit()

try:
    eel.start('index.html', 
              size=(1200, 800), 
              port=0, 
              close_callback=cerrar_proceso)
except (SystemExit, MemoryError, KeyboardInterrupt):
    sys.exit()
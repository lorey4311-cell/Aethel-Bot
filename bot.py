import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from threading import Thread

# 1. Este pequeño servidor abre el puerto que Render exige
def run_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    server.serve_forever()

# 2. Aquí iniciamos el servidor en segundo plano
Thread(target=run_server, daemon=True).start()

# 3. AQUÍ VA TU CÓDIGO DEL BOT (lo que tenías antes)
print("Aethel-Bot encendido y operando bajo el modo servidor.")
import time
while True:
    time.sleep(60)

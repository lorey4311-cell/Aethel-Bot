import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Esto hace que Render detecte un puerto
port = int(os.environ.get("PORT", 8080))
def run_server():
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    server.serve_forever()

# Aquí iría el inicio de tu bot de Telegram
# ... (tu código actual de bot sigue aquí abajo) ...

run_server()

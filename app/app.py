from services.server import initialize_server

APP_PORT = 3000

app = initialize_server()
from services.server.routes import *

if __name__ == "__main__":
    app.run(host='localhost', port=APP_PORT, debug=False)
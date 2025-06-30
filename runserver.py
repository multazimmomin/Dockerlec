from os import environ
from FlaskWebProject1 import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(environ.get('PORT', '8000'))  # <-- Use PORT env var, default 8000
    except ValueError:
        PORT = 5555
    app.run(host=HOST, port=PORT)

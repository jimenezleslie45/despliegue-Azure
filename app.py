from flask import Flask
import os

app = Flask(__name__)

# Get the port from environment variable (Azure provides this)
port = int(os.environ.get('PORT', 8080))

@app.route('/')
def hello_world():
    return '<h1>¡ Bienvenidos a Despliegue Exitoso Leslie Garcia!</h1><p>Hola Leslie, tu aplicación está funcionando en Azure.</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)

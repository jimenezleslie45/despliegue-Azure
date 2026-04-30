from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>¡ Bienvenidos a Despliegue Exitoso Leslie Garcia!</h1><p>Hola Leslie, tu aplicación está funcionando en Azure.</p>'

if __name__ == '__main__':
    app.run()
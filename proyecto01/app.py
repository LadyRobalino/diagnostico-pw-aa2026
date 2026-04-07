from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Servidor corriendo en el puerto 5000"

if __name__ == '__main__':
    # Es crucial usar 0.0.0.0 para que sea accesible externamente
    app.run(host='0.0.0.0', port=5000)

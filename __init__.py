import os

from flask import Flask


def create_app():
    app = Flask(__name__)

    
    from . import cuadroRecursos
    app.register_blueprint(cuadroRecursos.bp)


    @app.route('/hola')
    def hola():
        return 'Hola buen hombre, que hace aca?'

    return app
    


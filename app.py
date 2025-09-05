import os
import sys
import flask
from controle.controle import *
from controle.task import *

# Adiciona o diretório pai ao caminho do sistema para permitir imports relativos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = Flask(__name__, template_folder=os.path.join('view', 'templates'))

app.register_blueprint(url)
app.register_blueprint(url2)

app.add_url_rule('/', 'index', TaskController.index)
app.add_url_rule('/contact', 'contact', TaskController.contact, methods=['GET', 'POST'])

from swagger import swaggerinit
from swagger.swaggerconfig import configure_swagger
configure_swagger(app)

if __name__ == "__main__":
    app.run(debug=True)
from controle.controle import *
from controle.task import *
import flask

app = flask.Flask(__name__)

app.register_blueprint(url)
app.register_blueprint(url2)

if __name__ == "__main__":
    app.run(debug=True)
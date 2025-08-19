from controle.controle import *
import flask

app = flask.Flask(__name__)

app.register_blueprint(url)

if __name__ == "__main__":
    app.run(debug=True)
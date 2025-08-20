import flask 
from models import model

url = flask.Blueprint("app_pb", __name__)

@url.route("/users",methods=["GET"])
def get_users():
        response = model.listaUsuario()
        return response


@url.route("/user/<int:id>",methods=["GET"])
def get_user(id):
        response = model.pegaUsuario(id)
        return response


@url.route("/user",methods=["POST"])
def post_user():
        response = model.insereUsuario()
        return response

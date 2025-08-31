import flask 
from models import model

url = flask.Blueprint("app_pb", __name__)

@url.route("/teste",methods=["GET"])
def teste():
       return {"TESTE":"TESTE"}

@url.route("/users",methods=["GET"])
def get_users():
        response = model.listaUsuarioSQL()
        return response


@url.route("/user/<int:id>",methods=["GET"])
def get_user(id):
        response = model.pegaUsuarioSQL(id)
        return response


@url.route("/user",methods=["POST"], strict_slashes=False)
def post_user():
        name = flask.request.args.get("nome")
        email = flask.request.args.get("email")
        response = model.insereUsuarioSQL(name, email)
        return response

@url.route("/users", methods=["PUT"], strict_slashes=False)
def update_user():
    name = flask.request.args.get("nome")
    email = flask.request.args.get("email")
    user_id = flask.request.args.get("user_id")
    response = model.atualizarUsuarioSQL(user_id, name, email)
    return response
        
@url.route("/users",methods=["DELETE"], strict_slashes=False)
def delete_user():
        user_id = flask.request.args.get("user_id")
        response = model.deletarUsuarioSQL(user_id)
        return response
        
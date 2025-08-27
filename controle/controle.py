import flask 
from models import model

url = flask.Blueprint("app_pb", __name__)

@url.route("/teste",methods=["GET"])
def teste():
       return {"TESTE":"TESTE"}

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
        name = flask.request.args.get("nome")
        email = flask.request.args.get("email")
        response = model.insereUsuario(name, email)
        return response

@url.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    name = flask.request.args.get("nome")
    email = flask.request.args.get("email")
    response = model.atualizaUsuario(user_id, name, email)
    return response
        
@url.route("/users/<int:user_id>",methods=["DELETE"])
def delete_user(user_id):
        response = model.deletaUsuario(user_id)
        return response
        
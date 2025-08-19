import flask 
from models import model

url = flask.Blueprint("app_pb", __name__)

@url.route("/user",methods=["GET"])
def get_user():
        return model.teste()
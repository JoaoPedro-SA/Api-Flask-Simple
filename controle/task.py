import flask 
from models import task

url2 = flask.Blueprint("app_pb2", __name__)

@url2.route("/tasks",methods=["GET"])
def get_tasks():
        response = task.listaTarefa()
        return response


@url2.route("/task/<int:id>",methods=["GET"])
def get_task(id):
        response = task.pegaTarefa(id)
        return response


@url2.route("/tasks",methods=["POST"])
def post_task():
        title = flask.request.args.get("title")
        description = flask.request.args.get("description")
        status = flask.request.args.get("status")
        user_id = flask.request.args.get("user_id")
        response = task.insereTarefa(title, description, status, user_id)
        return response

@url2.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
        response = task.atualizaTarefa(task_id)
        return response
        
@url2.route("/tasks/<int:task_id>",methods=["DELETE"])
def delete_task(task_id):
        response = task.deletaTarefa(task_id)
        return response
        
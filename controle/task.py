import flask 
from models import task

url2 = flask.Blueprint("app_pb2", __name__)

@url2.route("/list_tasks",methods=["GET"])
def get_tasks():
        response = task.listaTarefaSQL()
        return response


@url2.route("/task",methods=["GET"], strict_slashes=False)
def get_task():
        id = flask.request.args.get("id")
        response = task.pegaTarefaSQL(id)
        return response


@url2.route("/create_task",methods=["POST"], strict_slashes=False)
def post_task():
        title = flask.request.args.get("title")
        description = flask.request.args.get("description")
        status = flask.request.args.get("status")
        user_id = flask.request.args.get("user_id")
        response = task.insereTarefaSQL(title, description, status, user_id)
        return response

@url2.route("/upadate_task_status", methods=["PUT"], strict_slashes=False)
def update_task():
        task_id = flask.request.args.get("task_id")
        response = task.atualizaTarefaSQL(task_id)
        return response
        
@url2.route("/delete_task",methods=["DELETE"])
def delete_task():
        task_id = flask.request.args.get("task_id")
        response = task.deletaTarefaSQL(task_id)
        return response
        
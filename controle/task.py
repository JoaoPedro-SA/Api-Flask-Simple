from flask import *
import flask 
from models.bancoSQL import Task, session

url2 = flask.Blueprint("app_pb2", __name__)

class TaskController:
        @staticmethod
        def index():
                tasks = session.query(Task).all()
        
                return render_template('index.html', tasks=tasks)

        @staticmethod
        def contact():
                if request.method == 'POST':
                        title = request.form['title']
                        description = request.form['description']
                        status = request.form.get('status', 'pending')  # default 'pending'
                        user_id = request.form['user_id']

                        # Criar a Task
                        nova_task = Task(title=title, description=description, status=status, user_id=user_id)
                        session.add(nova_task)
                        session.commit()

                        return redirect(url_for('index'))

                return render_template('contact.html')
        
        
        
@url2.route("/list_tasks",methods=["GET"])
def get_tasks():
        response = Task.listaTarefaSQL()
        return response


@url2.route("/task",methods=["GET"], strict_slashes=False)
def get_task():
        id = flask.request.args.get("id")
        response = Task.pegaTarefaSQL(id)
        return response


@url2.route("/create_task",methods=["POST"], strict_slashes=False)
def post_task():
        title = flask.request.args.get("title")
        description = flask.request.args.get("description")
        status = flask.request.args.get("status")
        user_id = flask.request.args.get("user_id")
        response = Task.insereTarefaSQL(title, description, status, user_id)
        return response

@url2.route("/upadate_task_status", methods=["PUT"], strict_slashes=False)
def update_task():
        task_id = flask.request.args.get("task_id")
        response = Task.atualizaTarefaSQL(task_id)
        return response
        
@url2.route("/delete_task",methods=["DELETE"])
def delete_task():
        task_id = flask.request.args.get("task_id")
        response = Task.deletaTarefaSQL(task_id)
        return response
        
from flask_restx import Namespace, Resource, fields
from models import task

api = Namespace('tarefas', description='Operações com tarefas')

tarefa_model = api.model('Tarefa', {
    'id': fields.Integer(readonly=True),
    'title': fields.String(required=True),
    'description': fields.String,
    'status': fields.String,
    'user_id': fields.Integer
})


@api.route('/')
class TarefaList(Resource):
    @api.marshal_list_with(tarefa_model)
    def get(self):
        """Lista todas as tarefas"""
        return task.listaTarefaSQL().json

    @api.expect(tarefa_model)
    @api.marshal_with(tarefa_model, code=201)
    def post(self):
        """Cria uma nova tarefa"""
        data = api.payload
        return task.insereTarefaSQL(
            data['title'], data['description'], data['status'], data['user_id']
        ).json, 201


@api.route('/<int:id>')
@api.response(404, 'Tarefa não encontrada')
class Tarefa(Resource):
    @api.marshal_with(tarefa_model)
    def get(self, id):
        """Busca uma tarefa pelo ID"""
        return task.pegaTarefaSQL(id).json

    @api.marshal_with(tarefa_model)
    def put(self, id):
        """Alterna o status da tarefa"""
        return task.atualizaTarefaSQL(id).json

    @api.response(204, 'Tarefa deletada')
    def delete(self, id):
        """Deleta uma tarefa"""
        return task.deletaTarefaSQL(id).json, 204

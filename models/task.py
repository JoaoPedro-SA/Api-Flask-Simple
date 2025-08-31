from flask import jsonify, request
import models.bancoSQL as banco
from flask_sqlalchemy import SQLAlchemy

def geradorDeId(dados):
    if len(dados["tarefas"]) == 0:
        return 1
    else:
        return dados["tarefas"][-1]["id"] + 1


def listaTarefaSQL():
    response = []
    try: 
        tarefas = banco.session.query(banco.Task).all()
        for t in tarefas:
            response.append({"id": t.id, "title": t.title , "description": t.description, "status": t.status, "user_id": t.user_id})
    except Exception as e:
        response = {"erro": str(e)}
    finally:
        banco.session.close()
    return jsonify(response)
    
def pegaTarefaSQL(idBuscado):
    try:
        tarefa = banco.session.query(banco.Task).filter_by(id=idBuscado).first()     
        response = {"id": tarefa.id, "title": tarefa.title , "description": tarefa.description, "status": tarefa.status, "user_id": tarefa.user_id} 
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
    finally:
        banco.session.close()
    return jsonify(response) 
    
    


def insereTarefaSQL(title, description, status, user_id):
    try: 
        nova_tarefa = banco.Task(title=title, description=description, status=status, user_id=user_id)
        banco.session.add(nova_tarefa)
        banco.session.commit()
        response = {"id": nova_tarefa.id, "title" : nova_tarefa.title ,  "description": nova_tarefa.description, "status": nova_tarefa.status, "user_id": nova_tarefa.user_id}
    except Exception as e:
        response = {"erro": str(e)}
    finally:
        banco.session.close()
    return jsonify(response)


def atualizaTarefaSQL(id):
    try:
        tarefa = banco.session.query(banco.Task).filter_by(id=id).first()
        if tarefa:
            if tarefa.status == "completo":
                tarefa.status = "incompleto"
            elif tarefa.status == "incompleto":
                tarefa.status = "completo"
            else: 
                tarefa.status = "incompleto"
            banco.session.commit()
            response = {"id": tarefa.id, "title": tarefa.title , "description": tarefa.description, "status": tarefa.status, "user_id": tarefa.user_id}
        else:
            return jsonify({"message": "Tarefa não encontrada"}), 404
    except Exception as e:
        response = {"erro": str(e)}
    finally:
        banco.session.close()
    return jsonify(response)

def deletaTarefaSQL(id):
    try:
        tarefa = banco.session.query(banco.Task).filter_by(id=id).delete()
        if tarefa:
            banco.session.commit()
            response = jsonify({"message": "Tarefa deletada com sucesso"})
        else:
            response = jsonify({"message": "Tarefa não encontrada"}), 404
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
    finally:
        banco.session.close()
    return response
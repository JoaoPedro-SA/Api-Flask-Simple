from flask import jsonify, request

dados = { 
    "tarefas": [
        {"id": 1, "title": "Estudar", "Description": "Estudar coisas", "status": "completo", "user_id":"3"},
        {"id": 2, "title": "Andar", "Description": "Andar em coisas", "status": "incompleto", "user_id":"2"},
    ]
}

def geradorDeId(dados):
    if len(dados["tarefas"]) == 0:
        return 1
    else:
        return dados["tarefas"][-1]["id"] + 1


def listaTarefa(): 
    return jsonify(dados["tarefas"])

def pegaTarefa(idBuscado):
    for i in dados["tarefas"]:
        if i["id"] == idBuscado:
            return jsonify(i)
        
def insereTarefa(title, description, status, user_id):
    novaTarefa = {
        "id": geradorDeId(dados),
        "title": title,
        "description": description,
        "status": status,
        "user_id": user_id
    }
    dados["tarefas"].append(novaTarefa)
    return jsonify(novaTarefa)

def atualizaTarefa(id):
    for i in dados["tarefas"]:
        if i["id"] == id:
            if i["status"] == "completo" :
                i["status"] = "incompleto"

            elif i["status"] == "incompleto":
                i["status"] = "completo"

            return jsonify(i)
    return jsonify({"message": "Tarefa não encontrada"}), 404

def deletaTarefa(id):
    for i, tarefa in enumerate(dados["tarefas"]):
        if  tarefa["id"] == id:
            del dados["tarefas"][i]
            return jsonify({"message": "Tarefa deletada com sucesso"})
    return jsonify({"message": "Tarefa não encontrado"}), 404
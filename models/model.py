from flask import jsonify, request

dados = { 
    "usuarios": [
        {"id": 1, "nome": "Antônio", "email": "antonio@email.com"},
        {"id": 2, "nome": "Maria", "email": "maria@email.com"},
        {"id": 3, "nome": "João", "email": "joao@email.com"},
        {"id": 4, "nome": "Ana", "email": "ana@email.com"},
        {"id": 5, "nome": "Pedro", "email": "pedro@email.com"},
        {"id": 6, "nome": "Lucas", "email": "lucas@email.com"},
        {"id": 7, "nome": "Carla", "email": "carla@email.com"},
        {"id": 8, "nome": "Fernanda", "email": "fernanda@email.com"},
        {"id": 9, "nome": "Roberto", "email": "roberto@email.com"},
        {"id": 10, "nome": "Juliana", "email": "juliana@email.com"}
    ]
}

def geradorDeId(dados):
    if len(dados["usuarios"]) == 0:
        return 1
    else:
        return dados["usuarios"][-1]["id"] + 1


def teste():
    return {"message": "Hello from the model!"} 

def listaUsuario(): 
    return jsonify(dados["usuarios"])

def pegaUsuario(idBuscado):
    for i in dados["usuarios"]:
        if i["id"] == idBuscado:
            return jsonify(i)
        
def insereUsuario(name, email):
    novoUsuario = {
        "id": geradorDeId(dados),
        "nome": name,
        "email": email
    }
    dados["usuarios"].append(novoUsuario)
    return jsonify(novoUsuario)

def atualizaUsuario(id, name, email):
    for i in dados["usuarios"]:
        if i["id"] == id:
            i["nome"] = name
            i["email"] = email
            return jsonify(i)
    return jsonify({"message": "Usuário não encontrado"}), 404

def deletaUsuario(id):
    for i, usuario in enumerate(dados["usuarios"]):
        if usuario["id"] == id:
            del dados["usuarios"][i]
            return jsonify({"message": "Usuário deletado com sucesso"})
    return jsonify({"message": "Usuário não encontrado"}), 404
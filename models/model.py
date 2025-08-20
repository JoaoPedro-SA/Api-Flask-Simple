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
    maiorID = 0
    for i in dados["usuarios"]:
        if i["id"] > maiorID:
            maiorID = i
    return maiorID+1


def teste():
    return {"message": "Hello from the model!"} 

def listaUsuario(): 
    return jsonify(dados["usuarios"])

def pegaUsuario(idBuscado):
    for i in dados["usuarios"]:
        if i["id"] == idBuscado:
            return jsonify(i)
        
def insereUsuario(usuario):
    idNovo = geradorDeId(dados)
    usuario = request.get_json()
    
    dados["usuarios"].append(usuario)
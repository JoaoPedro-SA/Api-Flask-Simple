from flask import jsonify, request
import models.bancoSQL as banco

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

def listaUsuarioSQL(): 
    response = []
    try: 
        usuario = banco.session.query(banco.User).all()
        for u in usuario: 
            response.append({"id": u.id, "nome": u.name, "email": u.email})
    except Exception as e:
        response = {"erro": str(e)}
    finally:
        banco.session.close()
    return jsonify(response)

def pegaUsuario(idBuscado):
    for i in dados["usuarios"]:
        if i["id"] == idBuscado:
            return jsonify(i)
        
def pegaUsuarioSQL(idBuscado):
    usuario = banco.session.query(banco.User).filter_by(id=idBuscado).first()
    try:
        if usuario.id == idBuscado:
            response = {"id": usuario.id, "nome": usuario.name, "email": usuario.email}
    except Exception as e: 
        response = {"erro": str(e)}
    finally:
        banco.session.close()
    return jsonify(response)
        
def insereUsuario(name, email):
    novoUsuario = {
        "id": geradorDeId(dados),
        "nome": name,
        "email": email
    }
    dados["usuarios"].append(novoUsuario)
    return jsonify(novoUsuario)

def insereUsuarioSQL(name,email):
    novo_usuario = banco.User(name=name, email=email)
    try:
        banco.session.add(novo_usuario)
        banco.session.commit()
        response = {"id": novo_usuario.id, "nome": novo_usuario.name, "email": novo_usuario.email}
    except Exception as e:
        banco.session.rollback()
        response = {"erro": str(e)}
    finally:
        banco.session.close()
    return jsonify(response)

def atualizaUsuario(id, name, email):
    for i in dados["usuarios"]:
        if i["id"] == id:
            i["nome"] = name
            i["email"] = email
            return jsonify(i)
    return jsonify({"message": "Usuário não encontrado"}), 404

def atualizarUsuarioSQL(id,name,email):
    try:
        usuario = banco.session.query(banco.User).filter_by(id=id).first()
        if usuario:
            usuario.name = name
            usuario.email = email
            banco.session.commit()
            response = {"id": usuario.id, "nome": usuario.name, "email": usuario.email}
        else:
            response = {"message": "Usuário não encontrado"}
    except Exception as e:
        banco.session.rollback()
        response = {"erro": str(e)}
    finally:
        banco.session.close()
    return jsonify(response)
         
def deletaUsuario(id):
    for i, usuario in enumerate(dados["usuarios"]):
        if usuario["id"] == id:
            del dados["usuarios"][i]
            return jsonify({"message": "Usuário deletado com sucesso"})
    return jsonify({"message": "Usuário não encontrado"}), 404

def deletarUsuarioSQL(id):
    try: 
        status = banco.session.query(banco.User).filter_by(id=id).delete()
        banco.session.commit()
        if status:
            response = {"message": "Usuário deletado com sucesso"}
        else:
            response = {"message": "Usuário não encontrado"}
    except Exception as e:
        banco.session.rollback()
        response = {"erro": str(e)}
    finally:
        banco.session.close()
    return jsonify(response)    

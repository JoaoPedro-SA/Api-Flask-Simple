from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Task(Base):
     __tablename__ = 'tasks'
     id = Column(Integer, primary_key=True)
     title = Column(String, nullable=False)
     description = Column(String, nullable=False)
     status = Column(String, default='pendente')
     user_id = Column(Integer, nullable=False)
     

class User(Base):
     __tablename__ = 'users'
     id = Column(Integer, primary_key=True)
     name = Column(String, nullable=False)
     email = Column(String, nullable=False)

engine = create_engine("sqlite:///meubanco.db", echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

teste = True
try:
     if teste:
          # Inserir um usuário
               novo_usuario = User(name="Nome Usuario ", email=f"email@example.com ")
               session.add(novo_usuario)
               session.commit()

          # Inserir uma tarefa
               nova_task = Task(title= f"Titulo teste " ,description=f"Estudar SQLAlchemy  ", user_id=novo_usuario.id)
               session.add(nova_task)
               session.commit()
               teste = False
          
except Exception as e:
     erro = str(e)

# Consultar usuários
# usuarios = session.query(User).all()
# for u in usuarios:
#     print(u.id, u.name, u.email)

# Consultar tarefas
# tarefas = session.query(Task).all()
# for t in tarefas:
#     print(t.id, t.description, t.status, t.user_id)
    
session.close()
from flask_restx import Api

api = Api(
    title="API de dados",
    version="1.0",
    description="Operações com usuários",
    doc="/docs",        #acessar a interface Swagger
    prefix="/api",      #base da api
)
.
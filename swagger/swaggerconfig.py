from .swaggerinit import api

def configure_swagger(app):
    from .namespace.usuarionamespace import api as usuarios_ns
    from .namespace.tasknamespace import api as tarefas_ns
    
    api.init_app(app)  
  
    api.add_namespace(usuarios_ns, path="/usuarios")
    api.add_namespace(tarefas_ns, path="/tarefas")

    api.mask_swagger = False

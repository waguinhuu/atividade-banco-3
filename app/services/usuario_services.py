from models.usuario import Usuario
from repositores.usuario_repositories import UsuarioRepository

class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository
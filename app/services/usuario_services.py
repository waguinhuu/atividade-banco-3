from models.usuario import Usuario
from repositores.usuario_repositories import UsuarioRepository

class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def criar_usuario(self, nome: str, email: str, senha: str):
        try:
            usuario = Usuario(nome=nome, email=email, senha=senha)
            self.repository.salvar_usuario(usuario)
            print("Usuario salvo com sucesso!")
        except TypeError as erro:
            print("Erro ao salvar o arquivo.")
        except Exception as erro:
            print("Ocorreu um erro inesperado.")
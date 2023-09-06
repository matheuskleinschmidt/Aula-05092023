class Biblioteca():
  livros = []

  def adicionar_livro(self, livro):
    self.livros.append(livro)

  def remover_livro(self, index):
    del self.livros[index]

  def listar_livros(self):
    return self.livros

class Livro():
  def __init__(self, titulo):
        self.titulo = titulo
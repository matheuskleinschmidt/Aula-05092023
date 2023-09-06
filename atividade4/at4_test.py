from at4 import Biblioteca, Livro

def test_biblioteca():
  biblioteca = Biblioteca()

  livro1 = Livro("The Lord Of The Rings")
  livro2 = Livro("The Witcher")

  biblioteca.adicionar_livro(livro1)

  assert biblioteca.listar_livros() == [livro1]

  biblioteca.adicionar_livro(livro2)

  assert biblioteca.listar_livros() == [livro1, livro2]

  biblioteca.remover_livro(1)

  assert biblioteca.listar_livros() == [livro1]
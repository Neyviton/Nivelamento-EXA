"""API de exemplo da Aula 8: uma biblioteca com os dados na memória.

    python ferramentas/biblioteca.py

Sobe em http://127.0.0.1:8001 e mostra no terminal cada requisição recebida. Os dados voltam
ao começo sempre que o servidor reinicia (Ctrl+C e o comando de novo).

Na Aula 8, ela é uma caixa-preta para praticar HTTP. Na Aula 9, o código serve de exemplo de
FastAPI: compare com secretaria/api.
"""

from typing import Annotated

import uvicorn
from fastapi import FastAPI, HTTPException, Path, Response, status
from pydantic import BaseModel, Field

Isbn = Annotated[str, Field(pattern=r"^\d{13}$", examples=["9780000000001"])]


class DadosLivro(BaseModel):
    titulo: str = Field(min_length=1)
    autor: str = Field(min_length=1)
    ano: int = Field(ge=1450, le=2100)


class Livro(BaseModel):
    isbn: Isbn
    titulo: str = Field(min_length=1)
    autor: str = Field(min_length=1)
    ano: int = Field(ge=1450, le=2100)


class LivroSaida(Livro):
    disponivel: bool


class Emprestimo(BaseModel):
    isbn: Isbn
    leitor: str = Field(min_length=1)


app = FastAPI(
    title="API da biblioteca", description="Exemplo da Aula 8, com os dados na memória."
)

LIVROS: dict[str, Livro] = {}
EMPRESTIMOS: dict[str, str] = {}  # isbn -> leitor


def recomecar() -> None:
    """Os quatro livros de exemplo, todos disponíveis (ISBNs fictícios)."""
    LIVROS.clear()
    EMPRESTIMOS.clear()
    for isbn, titulo, autor, ano in (
        ("9780000000001", "Dom Casmurro", "Machado de Assis", 1899),
        ("9780000000002", "Memórias Póstumas de Brás Cubas", "Machado de Assis", 1881),
        ("9780000000003", "O Cortiço", "Aluísio Azevedo", 1890),
        ("9780000000004", "Iracema", "José de Alencar", 1865),
    ):
        LIVROS[isbn] = Livro(isbn=isbn, titulo=titulo, autor=autor, ano=ano)


def saida(livro: Livro) -> LivroSaida:
    return LivroSaida(**livro.model_dump(), disponivel=livro.isbn not in EMPRESTIMOS)


def livro_existente(isbn: str) -> Livro:
    if isbn not in LIVROS:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"livro {isbn} não encontrado")
    return LIVROS[isbn]


IsbnDoCaminho = Annotated[str, Path(pattern=r"^\d{13}$")]


@app.get("/livros")
def listar(autor: str | None = None) -> list[LivroSaida]:
    """Todos os livros, ou só os do autor (?autor=Machado de Assis)."""
    return [
        saida(livro)
        for livro in LIVROS.values()
        if autor is None or livro.autor == autor
    ]


@app.get("/livros/{isbn}")
def buscar(isbn: IsbnDoCaminho) -> LivroSaida:
    return saida(livro_existente(isbn))


@app.post("/livros", status_code=status.HTTP_201_CREATED)
def cadastrar(livro: Livro, resposta: Response) -> LivroSaida:
    if livro.isbn in LIVROS:
        raise HTTPException(
            status.HTTP_409_CONFLICT, f"o livro {livro.isbn} já está cadastrado"
        )
    LIVROS[livro.isbn] = livro
    resposta.headers["Location"] = f"/livros/{livro.isbn}"
    return saida(livro)


@app.put("/livros/{isbn}")
def substituir(isbn: IsbnDoCaminho, dados: DadosLivro) -> LivroSaida:
    livro_existente(isbn)
    LIVROS[isbn] = Livro(isbn=isbn, **dados.model_dump())
    return saida(LIVROS[isbn])


@app.delete("/livros/{isbn}", status_code=status.HTTP_204_NO_CONTENT)
def remover(isbn: IsbnDoCaminho) -> None:
    livro_existente(isbn)
    if isbn in EMPRESTIMOS:
        raise HTTPException(status.HTTP_409_CONFLICT, f"o livro {isbn} está emprestado")
    del LIVROS[isbn]


@app.post("/emprestimos", status_code=status.HTTP_201_CREATED)
def emprestar(emprestimo: Emprestimo) -> Emprestimo:
    livro_existente(emprestimo.isbn)
    if emprestimo.isbn in EMPRESTIMOS:
        raise HTTPException(
            status.HTTP_409_CONFLICT, f"o livro {emprestimo.isbn} já está emprestado"
        )
    EMPRESTIMOS[emprestimo.isbn] = emprestimo.leitor
    return emprestimo


@app.delete("/emprestimos/{isbn}", status_code=status.HTTP_204_NO_CONTENT)
def devolver(isbn: IsbnDoCaminho) -> None:
    if isbn not in EMPRESTIMOS:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, f"o livro {isbn} não está emprestado"
        )
    del EMPRESTIMOS[isbn]


recomecar()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)

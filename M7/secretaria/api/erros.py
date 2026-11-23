"""Respostas de erro da API (Aula 10).

Toda resposta de erro tem o mesmo formato, o schema Erro: um código curto para programas, uma
mensagem para pessoas e, nos erros de entrada, a lista de problemas por campo. Os serviços
continuam levantando as exceções de secretaria/erros.py, sem saber de HTTP: é este arquivo que
decide o código de status de cada uma.
"""

from typing import Any

from fastapi import FastAPI, Request, status  # noqa: F401 (usado nas práticas)
from fastapi.exceptions import RequestValidationError  # noqa: F401 (usado nas práticas)
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from secretaria.erros import (
    BancoIndisponivelError,  # noqa: F401 (usado nas práticas)
    NaoEncontradoError,  # noqa: F401 (usado nas práticas)
    RegraDeNegocioError,  # noqa: F401 (usado nas práticas)
)


class DetalheErro(BaseModel):
    """Um problema de entrada: onde está (body, path ou query), o campo e a mensagem."""

    local: str
    campo: str
    mensagem: str


class Erro(BaseModel):
    """O corpo de toda resposta de erro da API."""

    erro: str
    mensagem: str
    detalhes: list[DetalheErro] = []


def resposta(
    codigo: int, erro: str, mensagem: str, detalhes: list[DetalheErro] | None = None
) -> JSONResponse:
    """Monta a resposta de erro no formato do schema Erro."""
    corpo = Erro(erro=erro, mensagem=mensagem, detalhes=detalhes or [])
    return JSONResponse(status_code=codigo, content=corpo.model_dump())


# Mensagens em português para os tipos de erro de validação do Pydantic.
TRADUCOES = {
    "missing": "é obrigatório",
    "extra_forbidden": "não faz parte do contrato",
    "json_invalid": "o corpo não é um JSON válido",
    "float_parsing": "deve ser um número, como 8.5",
    "int_parsing": "deve ser um número inteiro",
    "greater_than_equal": "deve ser no mínimo {ge}",
    "less_than_equal": "deve ser no máximo {le}",
}


def detalhe(item: dict[str, Any]) -> DetalheErro:
    """Um item de erro.errors() como DetalheErro.

    item["loc"] é uma tupla como ("body", "nota") ou ("path", "semestre"): o primeiro elemento
    é o local, e o campo é o último elemento que for texto (no JSON inválido, o último é um
    número: a posição do erro). A mensagem vem de TRADUCOES (com item["ctx"] para preencher
    {ge} e {le}); sem tradução, use item["msg"] sem o prefixo "Value error, ".
    """
    raise NotImplementedError("TODO Aula 10, Prática 2")


async def nao_encontrado(request: Request, erro: Exception) -> JSONResponse:
    """NaoEncontradoError: 404, com a mensagem da exceção."""
    raise NotImplementedError("TODO Aula 10, Prática 1")


async def entrada_invalida(request: Request, erro: Exception) -> JSONResponse:
    """RequestValidationError: 422, com um DetalheErro para cada problema."""
    raise NotImplementedError("TODO Aula 10, Prática 2")


async def regra_de_negocio(request: Request, erro: Exception) -> JSONResponse:
    """RegraDeNegocioError: 409, o pedido conflita com o estado da escola."""
    raise NotImplementedError("TODO Aula 10, Prática 3")


async def banco_indisponivel(request: Request, erro: Exception) -> JSONResponse:
    """BancoIndisponivelError: 503. A mensagem é genérica: o endereço do banco não sai daqui."""
    raise NotImplementedError("TODO Aula 10, Prática 3")


async def erro_inesperado(request: Request, erro: Exception) -> JSONResponse:
    """Qualquer outra exceção: 500, sem mostrar detalhes internos a quem chamou."""
    raise NotImplementedError("TODO Aula 10, Prática 3")


# Para a documentação (/docs): os erros que as rotas podem devolver, com o schema Erro.
RESPOSTAS: dict[int | str, dict[str, Any]] = {
    404: {"model": Erro, "description": "Aluno, turma ou matrícula não encontrados"},
    409: {"model": Erro, "description": "O pedido conflita com uma regra da escola"},
    422: {"model": Erro, "description": "Entrada fora do formato do contrato"},
    503: {"model": Erro, "description": "Banco de dados indisponível"},
}


def registrar(app: FastAPI) -> None:
    """Liga cada exceção ao seu tratador. app.py chama esta função uma vez."""
    # TODO Aula 10: uma linha app.add_exception_handler(Excecao, tratador) por tratador pronto.

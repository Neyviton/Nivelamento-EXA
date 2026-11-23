"""Dependências das rotas (Aula 9): parâmetros que várias rotas compartilham.

O FastAPI chama a dependência antes da rota e entrega o resultado a ela. Uma dependência pode
pedir os seus próprios parâmetros (aqui, os do caminho), que o FastAPI lê e valida.
"""

from dataclasses import dataclass
from typing import Annotated

from fastapi import Depends

from secretaria.schemas import CodigoDisciplina, Semestre


@dataclass(frozen=True, slots=True)
class ChaveTurma:
    """O que identifica uma turma na URL: /turmas/{codigo}/{semestre}."""

    codigo: str
    semestre: str


def chave_turma(codigo: CodigoDisciplina, semestre: Semestre) -> ChaveTurma:
    """Lê e valida o código (cc201 vira CC201) e o semestre do caminho."""
    return ChaveTurma(codigo, semestre)


# Nas rotas: turma: TurmaDoCaminho. O FastAPI chama chave_turma e entrega a ChaveTurma.
TurmaDoCaminho = Annotated[ChaveTurma, Depends(chave_turma)]

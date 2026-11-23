"""Camada de acesso a dados com o SQLAlchemy ORM.

No M5, esta camada entrou no lugar da versão com sqlite3 mantendo a mesma interface (Aula 7).
Funciona com qualquer banco da DATABASE_URL, inclusive o PostgreSQL. Os serviços usam só o que
está listado em __all__.
"""

from .alunos import buscar_aluno
from .conexao import Conexao, abrir
from .matriculas import (
    apagar_matricula,
    buscar_matricula,
    gravar_nota,
    inserir_matricula,
    matriculas_da_turma,
    matriculas_do_aluno,
    matriculas_do_curso,
)
from .turmas import buscar_turma

__all__ = [
    "Conexao",
    "abrir",
    "apagar_matricula",
    "buscar_aluno",
    "buscar_matricula",
    "buscar_turma",
    "gravar_nota",
    "inserir_matricula",
    "matriculas_da_turma",
    "matriculas_do_aluno",
    "matriculas_do_curso",
]

"""Rotas do recurso curso: /cursos/{sigla}."""

from typing import Annotated  # noqa: F401 (usado nas práticas)

from fastapi import APIRouter, Query  # noqa: F401 (usado nas práticas)

from secretaria.schemas import Semestre, SiglaCurso  # noqa: F401 (usado nas práticas)
from secretaria.servicos import consultas  # noqa: F401 (usado nas práticas)

from ..schemas import RankingSaida, ranking_saida  # noqa: F401 (usado nas práticas)

rotas = APIRouter(prefix="/cursos", tags=["cursos"])

# TODO Aula 9, Prática 2: GET /cursos/{sigla}/ranking?semestre=2026.1&top=3 -> RankingSaida
#   * semestre: parâmetro de consulta obrigatório, do tipo Semestre;
#   * top: parâmetro de consulta opcional, de 1 a 10, 3 se não vier.

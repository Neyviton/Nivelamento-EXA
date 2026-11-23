"""Rotas do recurso aluno: /alunos."""

from fastapi import APIRouter

from secretaria.schemas import MatriculaAluno  # noqa: F401 (usado nas práticas)
from secretaria.servicos import consultas  # noqa: F401 (usado nas práticas)

from ..schemas import BoletimSaida, boletim_saida  # noqa: F401 (usado nas práticas)

rotas = APIRouter(prefix="/alunos", tags=["alunos"])

# TODO Aula 9, Prática 1: GET /alunos/{matricula}/boletim
#   * a matrícula vem do caminho, com o tipo MatriculaAluno;
#   * chama consultas.consultar_boletim e devolve boletim_saida(...): BoletimSaida.

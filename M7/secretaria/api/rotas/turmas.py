"""Rotas do recurso turma: /turmas/{codigo}/{semestre} e as matrículas dentro dela."""

from fastapi import APIRouter, Response, status  # noqa: F401 (usado nas práticas)

from secretaria.schemas import LancamentoNota, MatriculaAluno, NovaMatricula  # noqa: F401 (usado nas práticas)
from secretaria.servicos import consultas, matriculas, notas  # noqa: F401 (usado nas práticas)

from ..dependencias import TurmaDoCaminho  # noqa: F401 (usado nas práticas)
from ..schemas import (
    MatriculaEntrada,  # noqa: F401 (usado nas práticas)
    MatriculaSaida,  # noqa: F401 (usado nas práticas)
    NotaEntrada,  # noqa: F401 (usado nas práticas)
    RelatorioTurmaSaida,  # noqa: F401 (usado nas práticas)
    matricula_saida,  # noqa: F401 (usado nas práticas)
    relatorio_saida,  # noqa: F401 (usado nas práticas)
)

rotas = APIRouter(prefix="/turmas", tags=["turmas"])

# TODO Aula 9, Prática 2 (leitura), com turma: TurmaDoCaminho:
#   GET /turmas/{codigo}/{semestre}                         -> RelatorioTurmaSaida
#   GET /turmas/{codigo}/{semestre}/matriculas/{matricula}  -> MatriculaSaida
#
# TODO Aula 9, Prática 3 (escrita):
#   PUT    /turmas/{codigo}/{semestre}/matriculas/{matricula}/nota  corpo NotaEntrada
#          -> 200, MatriculaSaida
#   POST   /turmas/{codigo}/{semestre}/matriculas  corpo MatriculaEntrada
#          -> 201, MatriculaSaida e o cabeçalho Location com o endereço da matrícula nova
#   DELETE /turmas/{codigo}/{semestre}/matriculas/{matricula}  -> 204, sem corpo

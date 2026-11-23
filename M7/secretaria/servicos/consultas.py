"""Serviços de consulta: boletim, relatório da turma, matrícula e ranking."""

from secretaria import acesso_orm as dados
from secretaria.dominio import Boletim, Linha, PosicaoRanking, RelatorioTurma
from secretaria.managers import avaliacao, relatorios

from .buscas import aluno_existente, matricula_existente, turma_existente


def consultar_boletim(matricula: str) -> Boletim:
    with dados.abrir() as con:
        aluno = aluno_existente(con, matricula)
        matriculas = dados.matriculas_do_aluno(con, aluno.id)
        return relatorios.montar_boletim(aluno, matriculas)


def relatorio_turma(codigo: str, semestre: str) -> RelatorioTurma:
    with dados.abrir() as con:
        turma = turma_existente(con, codigo, semestre)
        matriculas = dados.matriculas_da_turma(con, turma.id)
        return relatorios.montar_relatorio_turma(turma, matriculas)


def ranking(curso: str, semestre: str, top: int) -> list[PosicaoRanking]:
    with dados.abrir() as con:
        matriculas = dados.matriculas_do_curso(con, curso, semestre)
        return relatorios.ranking(matriculas, top)


def consultar_matricula(matricula: str, codigo: str, semestre: str) -> Linha:
    """Uma matrícula, com a situação calculada (M7: o recurso de uma matrícula na API)."""
    with dados.abrir() as con:
        aluno = aluno_existente(con, matricula)
        turma = turma_existente(con, codigo, semestre)
        atual = matricula_existente(con, aluno, turma)
        return avaliacao.classificar([atual])[0]

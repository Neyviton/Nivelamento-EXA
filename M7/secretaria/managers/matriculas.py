"""Regras de matrícula (Aula 7)."""

from secretaria.config import SEMESTRE_ATUAL
from secretaria.dominio import Aluno, Matricula, Turma
from secretaria.erros import RegraDeNegocioError


def conferir_matricula(aluno: Aluno, turma: Turma, ja_matriculado: bool) -> None:
    """Regras da matrícula, nesta ordem:

    * só no semestre em andamento (SEMESTRE_ATUAL);
    * a disciplina tem de ser do curso do aluno;
    * o aluno não pode estar matriculado na turma (ja_matriculado).

    Regra não atendida: RegraDeNegocioError com as mensagens do enunciado.
    """
    if turma.semestre != SEMESTRE_ATUAL:
        raise RegraDeNegocioError(
            f"matrículas só no semestre em andamento ({SEMESTRE_ATUAL})"
        )
    if turma.curso != aluno.curso:
        raise RegraDeNegocioError(
            f"{turma.codigo} é uma disciplina de {turma.curso}, e o aluno é de {aluno.curso}"
        )
    if ja_matriculado:
        raise RegraDeNegocioError(
            f"{aluno.matricula} já está matriculado em {turma.codigo} ({turma.semestre})"
        )


def conferir_cancelamento(matricula: Matricula) -> None:
    """Desafio da Aula 7: só se cancela matrícula do semestre em andamento e sem nota."""
    if matricula.turma.semestre != SEMESTRE_ATUAL:
        raise RegraDeNegocioError(
            f"o semestre {matricula.turma.semestre} está encerrado; "
            "a matrícula não pode ser cancelada"
        )
    if matricula.nota is not None:
        raise RegraDeNegocioError("a matrícula já tem nota e não pode ser cancelada")

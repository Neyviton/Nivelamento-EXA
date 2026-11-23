"""Serviços de matrícula (Aula 7)."""

from secretaria import acesso_orm as dados
from secretaria.dominio import Linha, Matricula, Situacao
from secretaria.managers import matriculas as regras
from secretaria.schemas import NovaMatricula

from .buscas import aluno_existente, matricula_existente, turma_existente


def matricular(pedido: NovaMatricula) -> Linha:
    """Matricula o aluno na turma, numa transação:

    1. busca aluno e turma e confere se a matrícula já existe (dados.buscar_matricula);
    2. pede ao manager que confira as regras (regras.conferir_matricula);
    3. insere pelo acesso a dados e devolve a Linha da matrícula nova, sem nota.
    """
    with dados.abrir() as con:
        aluno = aluno_existente(con, pedido.matricula)
        turma = turma_existente(con, pedido.codigo, pedido.semestre)
        ja_matriculado = dados.buscar_matricula(con, aluno.id, turma.id) is not None
        regras.conferir_matricula(aluno, turma, ja_matriculado)
        dados.inserir_matricula(con, aluno.id, turma.id)
        return Linha(Matricula(aluno, turma, None), Situacao.CURSANDO)


def cancelar_matricula(pedido: NovaMatricula) -> Matricula:
    """Desafio da Aula 7."""
    with dados.abrir() as con:
        aluno = aluno_existente(con, pedido.matricula)
        turma = turma_existente(con, pedido.codigo, pedido.semestre)
        matricula = matricula_existente(con, aluno, turma)
        regras.conferir_cancelamento(matricula)
        dados.apagar_matricula(con, aluno.id, turma.id)
        return matricula

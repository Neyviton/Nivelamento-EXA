"""Serviço de lançamento de nota."""

from secretaria import acesso_orm as dados
from secretaria.dominio import Linha, Matricula
from secretaria.managers import avaliacao
from secretaria.schemas import LancamentoNota

from .buscas import aluno_existente, matricula_existente, turma_existente


def lancar_nota(pedido: LancamentoNota) -> Linha:
    """Aula 7: recebe o pedido já validado pelo schema."""
    with dados.abrir() as con:
        aluno = aluno_existente(con, pedido.matricula)
        turma = turma_existente(con, pedido.codigo, pedido.semestre)
        atual = matricula_existente(con, aluno, turma)
        nota_final = avaliacao.preparar_nota(atual, pedido.nota)
        dados.gravar_nota(con, aluno.id, turma.id, nota_final)
        gravada = Matricula(aluno, turma, nota_final)
        return Linha(gravada, avaliacao.situacao(nota_final))

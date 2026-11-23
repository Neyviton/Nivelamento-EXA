"""Regras de avaliação: situação, média e lançamento de nota."""

from collections.abc import Iterable

from secretaria.config import SEMESTRE_ATUAL
from secretaria.dominio import Linha, Matricula, Situacao
from secretaria.erros import RegraDeNegocioError

NOTA_APROVACAO = 6.0


def situacao(nota: float | None) -> Situacao:
    """Sem nota: cursando. Nota a partir de 6: aprovado. Abaixo de 6: reprovado."""
    if nota is None:
        return Situacao.CURSANDO
    return Situacao.APROVADO if nota >= NOTA_APROVACAO else Situacao.REPROVADO


def media(notas: Iterable[float | None]) -> float | None:
    """Média das notas lançadas, com duas casas. None se nenhuma nota foi lançada."""
    lancadas = [nota for nota in notas if nota is not None]
    if not lancadas:
        return None
    return round(sum(lancadas) / len(lancadas), 2)


def classificar(matriculas: Iterable[Matricula]) -> list[Linha]:
    """Uma Linha para cada matrícula, com a situação calculada."""
    return [Linha(m, situacao(m.nota)) for m in matriculas]


def preparar_nota(matricula: Matricula, nota: float) -> float:
    """Regras do lançamento: só no semestre em andamento, com uma casa decimal.

    O intervalo de 0 a 10 é formato e passou para o schema LancamentoNota (Aula 7).
    """
    if matricula.turma.semestre != SEMESTRE_ATUAL:
        raise RegraDeNegocioError(
            f"o semestre {matricula.turma.semestre} está encerrado; "
            f"notas só podem ser lançadas em {SEMESTRE_ATUAL}"
        )
    return round(nota, 1)

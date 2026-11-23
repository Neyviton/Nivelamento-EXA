"""Montagem dos relatórios: boletim do aluno e relatório da turma."""

from collections import Counter
from collections.abc import Iterable

from secretaria.dominio import (
    Aluno,
    Boletim,
    Matricula,
    PosicaoRanking,
    RelatorioTurma,
    Situacao,
    Turma,
)

from .avaliacao import classificar, media


def montar_boletim(aluno: Aluno, matriculas: list[Matricula]) -> Boletim:
    return Boletim(aluno, classificar(matriculas), media(m.nota for m in matriculas))


def montar_relatorio_turma(turma: Turma, matriculas: list[Matricula]) -> RelatorioTurma:
    """Linhas classificadas, média da turma e quantos alunos em cada situação.

    A contagem tem as três situações, mesmo as que ficam com zero:
    {Situacao.CURSANDO: 0, Situacao.APROVADO: 8, Situacao.REPROVADO: 3}.
    Dica: collections.Counter, como na Aula 2.
    """
    linhas = classificar(matriculas)
    contagem = Counter(linha.situacao for linha in linhas)
    return RelatorioTurma(
        turma,
        linhas,
        media(m.nota for m in matriculas),
        {s: contagem[s] for s in Situacao},
    )


def ranking(matriculas: Iterable[Matricula], top: int) -> list[PosicaoRanking]:
    """Desafio da Aula 6: os `top` alunos de maior média; empate pelo nome."""
    notas: dict[int, list[float | None]] = {}
    alunos: dict[int, Aluno] = {}
    for m in matriculas:
        notas.setdefault(m.aluno.id, []).append(m.nota)
        alunos[m.aluno.id] = m.aluno
    medias = [
        (valor, alunos[aluno_id])
        for aluno_id, lista in notas.items()
        if (valor := media(lista)) is not None
    ]
    medias.sort(key=lambda par: (-par[0], par[1].nome))
    return [
        PosicaoRanking(posicao, aluno, valor)
        for posicao, (valor, aluno) in enumerate(medias[:top], start=1)
    ]

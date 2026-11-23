"""Tela do ranking de um curso (desafio da Aula 6).

python -m secretaria.apresentacao.ranking CC 2026.1
"""

from secretaria.servicos import consultas

from .terminal import executar, ler_argumentos

TOP = 3


def mostrar_ranking(curso: str, semestre: str) -> None:
    posicoes = consultas.ranking(curso.upper(), semestre, TOP)
    print(f"Ranking {curso.upper()}, {semestre}")
    for p in posicoes:
        print(f"{p.posicao:>2}  {p.aluno.nome:<22} {p.media:.2f}")
    if not posicoes:
        print("nenhum aluno com nota nesse curso e semestre")


def main() -> None:
    curso, semestre = ler_argumentos("curso", "semestre")
    executar(lambda: mostrar_ranking(curso, semestre))


if __name__ == "__main__":
    main()

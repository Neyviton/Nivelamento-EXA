"""Mostra o JSON de cada schema de saída, com dados do banco (Aula 8, Prática 3).

    python -m secretaria.api.exemplos                  (todos)
    python -m secretaria.api.exemplos matricula ranking  (só os escolhidos)

É um script de conferência: chama os serviços, como a API vai chamar, e imprime o JSON que a
API vai devolver. Enquanto falta uma conversão, ele avisa e segue para a próxima.
"""

import sys
from collections.abc import Callable

from pydantic import BaseModel

from secretaria.servicos import consultas

from . import schemas

EXEMPLOS: list[tuple[str, str, Callable[[], BaseModel]]] = [
    (
        "boletim",
        "boletim de 2025001",
        lambda: schemas.boletim_saida(consultas.consultar_boletim("2025001")),
    ),
    (
        "matricula",
        "matrícula de 2025001 em CC101 (2026.1)",
        lambda: schemas.matricula_saida(
            consultas.consultar_matricula("2025001", "CC101", "2026.1")
        ),
    ),
    (
        "ranking",
        "ranking de CC em 2026.1",
        lambda: schemas.ranking_saida(
            "CC", "2026.1", consultas.ranking("CC", "2026.1", 3)
        ),
    ),
    (
        "relatorio",
        "relatório de ES202 (2026.1)",
        lambda: schemas.relatorio_saida(consultas.relatorio_turma("ES202", "2026.1")),
    ),
]


def main() -> None:
    escolhidos = set(sys.argv[1:])
    for nome, titulo, gerar in EXEMPLOS:
        if escolhidos and nome not in escolhidos:
            continue
        print(f"### {titulo}")
        try:
            print(gerar().model_dump_json(indent=2))
        except NotImplementedError as falta:
            print(f"ainda não implementado ({falta})")
        print()


if __name__ == "__main__":
    main()

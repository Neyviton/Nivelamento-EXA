"""Tela de lançamento de nota.

python -m secretaria.apresentacao.lancar_nota 2025001 CC201 2026.2 8.5
"""

from secretaria.schemas import LancamentoNota
from secretaria.servicos import notas

from .terminal import descrever, executar, formatar_nota, ler_argumentos


def lancar(matricula: str, codigo: str, semestre: str, nota: str) -> None:
    """Aula 7: o schema confere e converte o que foi digitado, antes do serviço."""
    pedido = LancamentoNota.model_validate(
        {"matricula": matricula, "codigo": codigo, "semestre": semestre, "nota": nota}
    )
    linha = notas.lancar_nota(pedido)
    nota_gravada = formatar_nota(linha.matricula.nota)
    print(f"Nota {nota_gravada} lançada: {descrever(linha)}, {linha.situacao}")


def main() -> None:
    matricula, codigo, semestre, nota = ler_argumentos(
        "matricula", "codigo", "semestre", "nota"
    )
    executar(lambda: lancar(matricula, codigo, semestre, nota))


if __name__ == "__main__":
    main()

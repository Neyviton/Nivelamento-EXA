"""Tela de cancelamento de matrícula (desafio da Aula 7).

python -m secretaria.apresentacao.cancelar_matricula 2026005 CC102 2026.2
"""

from secretaria.schemas import NovaMatricula
from secretaria.servicos import matriculas

from .terminal import executar, ler_argumentos


def cancelar(matricula: str, codigo: str, semestre: str) -> None:
    pedido = NovaMatricula.model_validate(
        {"matricula": matricula, "codigo": codigo, "semestre": semestre}
    )
    m = matriculas.cancelar_matricula(pedido)
    print(
        f"Matrícula cancelada: {m.aluno.matricula} {m.aluno.nome}, "
        f"{m.turma.codigo} {m.turma.disciplina} ({m.turma.semestre})"
    )


def main() -> None:
    matricula, codigo, semestre = ler_argumentos("matricula", "codigo", "semestre")
    executar(lambda: cancelar(matricula, codigo, semestre))


if __name__ == "__main__":
    main()

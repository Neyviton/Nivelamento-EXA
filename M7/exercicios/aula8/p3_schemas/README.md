# Aula 8, Prática 3: os schemas de saída

Em `secretaria/api/schemas.py`, as classes de saída já estão escritas: elas são o contrato, o
JSON que a API vai devolver. Compare com a sua `CONTRATO.md` antes de começar.

O que falta é a ponte entre as camadas: funções que recebem os tipos de `dominio.py` (o que os
serviços devolvem) e montam os schemas de saída. `aluno_saida`, `turma_saida` e `boletim_saida`
estão prontas e servem de modelo. Procure `TODO Aula 8, Prática 3` e implemente:

1. `relatorio_saida`: uma `LinhaTurma` por linha do relatório, e a turma com `turma_saida`;
2. `matricula_saida`: uma `Linha` do domínio no formato de `MatriculaSaida`;
3. `ranking_saida`: o curso e o semestre do pedido, e uma `PosicaoSaida` por posição.

Para conferir, sem servidor nenhum, o script `exemplos.py` chama os serviços e imprime o JSON de
cada schema, como a API vai fazer:

```text
$ python -m secretaria.api.exemplos
### boletim de 2025001
{
  "aluno": {
    "matricula": "2025001",
    "nome": "Ana Beatriz Souza",
    "curso": "CC"
  },
  "disciplinas": [
    {
      "semestre": "2026.1",
      "codigo": "CC101",
      "disciplina": "Algoritmos",
      "nota": 9.9,
      "situacao": "aprovado"
    },
    {
      "semestre": "2026.1",
      "codigo": "CC102",
      "disciplina": "Estruturas de Dados",
      "nota": 4.5,
      "situacao": "reprovado"
    },
    {
      "semestre": "2026.1",
      "codigo": "CC202",
      "disciplina": "Redes de Computadores",
      "nota": 5.6,
      "situacao": "reprovado"
    },
    {
      "semestre": "2026.2",
      "codigo": "CC102",
      "disciplina": "Estruturas de Dados",
      "nota": null,
      "situacao": "cursando"
    },
    {
      "semestre": "2026.2",
      "codigo": "CC201",
      "disciplina": "Banco de Dados",
      "nota": null,
      "situacao": "cursando"
    }
  ],
  "media": 6.67
}

### matrícula de 2025001 em CC101 (2026.1)
ainda não implementado (TODO Aula 8, Prática 3)

### ranking de CC em 2026.1
ainda não implementado (TODO Aula 8, Prática 3)

### relatório de ES202 (2026.1)
ainda não implementado (TODO Aula 8, Prática 3)
```

Com as três funções prontas, a matrícula e o ranking ficam assim (os nomes depois do comando
escolhem quais exemplos rodar; sem nomes, rodam todos):

```text
$ python -m secretaria.api.exemplos matricula ranking
### matrícula de 2025001 em CC101 (2026.1)
{
  "aluno": {
    "matricula": "2025001",
    "nome": "Ana Beatriz Souza",
    "curso": "CC"
  },
  "turma": {
    "codigo": "CC101",
    "disciplina": "Algoritmos",
    "semestre": "2026.1",
    "professor": "Helena Prado",
    "curso": "CC"
  },
  "nota": 9.9,
  "situacao": "aprovado"
}

### ranking de CC em 2026.1
{
  "curso": "CC",
  "semestre": "2026.1",
  "posicoes": [
    {
      "posicao": 1,
      "matricula": "2025003",
      "nome": "Diego Ramos",
      "media": 8.53
    },
    {
      "posicao": 2,
      "matricula": "2025002",
      "nome": "Bruno Costa",
      "media": 8.1
    },
    {
      "posicao": 3,
      "matricula": "2026004",
      "nome": "Lucas Martins",
      "media": 8.0
    }
  ]
}
```

O relatório de ES202 segue o mesmo formato: a turma, uma linha por aluno, a média 6.51 e a
contagem `{"aprovado": 5, "reprovado": 3}`.

## Para pensar

* `LinhaBoletim` e `LinhaTurma` vêm da mesma `Linha` do domínio, mas cada uma mostra campos
  diferentes. Por que não devolver a `Linha` inteira nos dois casos?
* A situação aparece como texto (`"aprovado"`) porque `Situacao` é um `StrEnum`. O que quem usa
  a API ganha com isso, em vez de um número como `1`?
* Se o nome de um campo do domínio mudar no M8, o JSON da API muda? Qual arquivo absorve a
  mudança?

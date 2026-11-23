# Aula 9, Prática 2: rotas de leitura

Procure `TODO Aula 9, Prática 2` em `secretaria/api/rotas/turmas.py` e
`secretaria/api/rotas/cursos.py`.

1. **Relatório da turma**: `GET /turmas/{codigo}/{semestre}`, devolvendo `RelatorioTurmaSaida`.
   Use a dependência pronta em `secretaria/api/dependencias.py`: o parâmetro
   `turma: TurmaDoCaminho` lê e valida o código e o semestre do caminho e entrega uma
   `ChaveTurma`.
2. **Uma matrícula**: `GET /turmas/{codigo}/{semestre}/matriculas/{matricula}`, devolvendo
   `MatriculaSaida`, com `consultas.consultar_matricula`. A mesma dependência, e a matrícula como
   parâmetro de caminho.
3. **Ranking**: `GET /cursos/{sigla}/ranking`, devolvendo `RankingSaida`. A sigla vem do caminho
   (`SiglaCurso`); o semestre e o top, da consulta: `Annotated[Semestre, Query()]` para o semestre
   obrigatório, e `Annotated[int, Query(ge=1, le=10)] = 3` para o top.

## Respostas esperadas

Com o servidor no ar, envie os pedidos de `leitura.http`:

```text
GET /turmas/es202/2026.1

HTTP/1.1 200 OK

{
  "turma": {
    "codigo": "ES202",
    "disciplina": "DevOps",
    "semestre": "2026.1",
    "professor": "Fernando Gomes",
    "curso": "ES"
  },
  "alunos": [
    {
      "matricula": "2025021",
      "nome": "Felipe Azevedo",
      "nota": 6.4,
      "situacao": "aprovado"
    },
    {
      "matricula": "2025023",
      "nome": "Isabela Farias",
      "nota": 8.0,
      "situacao": "aprovado"
    },
    {
      "matricula": "2025024",
      "nome": "Júlio César Reis",
...
    "reprovado": 3
  }
}

GET /turmas/CC101/2026.1/matriculas/2025001

HTTP/1.1 200 OK

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

GET /cursos/cc/ranking?semestre=2026.1&top=2

HTTP/1.1 200 OK

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
    }
  ]
}

GET /cursos/CC/ranking

HTTP/1.1 422 Unprocessable Content

{
  "detail": [
    {
      "type": "missing",
      "loc": [
        "query",
        "semestre"
      ],
      "msg": "Field required",
      "input": null
    }
  ]
}

GET /turmas/CC201/2026.3

HTTP/1.1 422 Unprocessable Content

{
  "detail": [
    {
      "type": "value_error",
      "loc": [
        "path",
        "semestre"
      ],
      "msg": "Value error, deve estar no formato AAAA.1 ou AAAA.2, como 2026.2",
      "input": "2026.3",
      "ctx": {
        "error": {}
      }
    }
  ]
}
```

## Para pensar

* A dependência `chave_turma` é usada pelas cinco rotas de turma. O que você teria de repetir em
  cada rota sem ela?
* No pedido 1, o código foi enviado em minúsculas. Em que linha ele virou `ES202`?
* Por que o semestre do ranking é parâmetro de consulta, e o da turma é parte do caminho?

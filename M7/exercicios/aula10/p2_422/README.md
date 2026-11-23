# Aula 10, Prática 2: o 422 em português, campo a campo

O FastAPI já responde 422 quando a entrada foge do formato, mas no formato dele: uma lista em
`detail`, em inglês, com `type`, `loc`, `msg`, `input` e `ctx`. Útil para depurar, pouco útil
para mostrar a uma pessoa. Nesta prática, a API passa a responder no formato `Erro`, com um
`DetalheErro` por problema.

Procure `TODO Aula 10, Prática 2` em `secretaria/api/erros.py`:

1. `detalhe(item)`: transforma um item de `erro.errors()` num `DetalheErro`. O local é o primeiro
   elemento de `item["loc"]` (`body`, `path` ou `query`), e o campo é o último elemento que for
   texto. A mensagem vem do dicionário `TRADUCOES`, com `item["ctx"]` para preencher `{ge}` e
   `{le}`; sem tradução, use `item["msg"]` sem o prefixo `Value error, `.
2. `entrada_invalida`: 422, o código `entrada_invalida`, a mensagem
   `a requisição tem N problema(s) de formato` e os detalhes.
3. Em `registrar`: `app.add_exception_handler(RequestValidationError, entrada_invalida)`.

## Respostas esperadas

```text
GET /alunos/20251/boletim

HTTP/1.1 422 Unprocessable Content

{
  "erro": "entrada_invalida",
  "mensagem": "a requisição tem 1 problema de formato",
  "detalhes": [
    {
      "local": "path",
      "campo": "matricula",
      "mensagem": "deve ter 7 dígitos, como 2025001"
    }
  ]
}

GET /cursos/CC/ranking?top=50

HTTP/1.1 422 Unprocessable Content

{
  "erro": "entrada_invalida",
  "mensagem": "a requisição tem 2 problemas de formato",
  "detalhes": [
    {
      "local": "query",
      "campo": "semestre",
      "mensagem": "é obrigatório"
    },
    {
      "local": "query",
      "campo": "top",
      "mensagem": "deve ser no máximo 10"
    }
  ]
}

PUT /turmas/CC201/2026.2/matriculas/2025001/nota

HTTP/1.1 422 Unprocessable Content

{
  "erro": "entrada_invalida",
  "mensagem": "a requisição tem 2 problemas de formato",
  "detalhes": [
    {
      "local": "body",
      "campo": "nota",
      "mensagem": "deve ser no máximo 10"
    },
    {
      "local": "body",
      "campo": "observacao",
      "mensagem": "não faz parte do contrato"
    }
  ]
}

POST /turmas/CC102/2026.2/matriculas

HTTP/1.1 422 Unprocessable Content

{
  "erro": "entrada_invalida",
  "mensagem": "a requisição tem 1 problema de formato",
  "detalhes": [
    {
      "local": "body",
      "campo": "body",
      "mensagem": "o corpo não é um JSON válido"
    }
  ]
}
```

## Para pensar

* O pedido 2 tem dois problemas, e os dois aparecem. Por que isso é melhor do que parar no
  primeiro?
* A tela do terminal do M5 (`apresentacao/terminal.py`) tem uma tradução parecida. Onde ela
  poderia morar para servir às duas apresentações?
* O campo `observacao` foi recusado porque `NotaEntrada` não aceita campos fora do contrato
  (`extra="forbid"`). Que erro passaria despercebido se ele fosse aceito em silêncio?

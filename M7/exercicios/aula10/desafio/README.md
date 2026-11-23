# Desafio da Aula 10: todo erro no mesmo formato

Depois das práticas, os erros da secretaria seguem o schema `Erro`. Mas o próprio FastAPI ainda
responde no formato dele em dois casos:

```text
GET /professores                  -> 404 {"detail": "Not Found"}
PATCH /alunos/2025001/boletim     -> 405 {"detail": "Method Not Allowed"}
```

1. Trate também esses erros, com o formato `Erro`: o FastAPI os levanta como
   `starlette.exceptions.HTTPException`, com o código em `status_code`. Use os códigos
   `rota_inexistente` (404) e `metodo_nao_permitido` (405), com mensagens que digam a rota e o
   método recebidos.
2. Escreva `aceite.http` nesta pasta: um pedido para cada resposta que a API sabe dar (200, 201,
   204, 404, 405, 409 e 422), com um comentário em cada um dizendo o código esperado. É o roteiro
   de aceite da API: quem mudar o código depois roda o arquivo inteiro e confere.

Respostas esperadas para os dois casos:

```text
GET /professores

HTTP/1.1 404 Not Found

{
  "erro": "rota_inexistente",
  "mensagem": "não existe a rota /professores",
  "detalhes": []
}

PATCH /alunos/2025001/boletim

HTTP/1.1 405 Method Not Allowed

{
  "erro": "metodo_nao_permitido",
  "mensagem": "a rota /alunos/2025001/boletim não aceita o método PATCH",
  "detalhes": []
}
```

Entrega: o tratador novo e o `aceite.http`. Confira com `ruff check .` e
`mypy --strict secretaria`.

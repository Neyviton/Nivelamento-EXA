# Aula 8, Prática 1: conversando com uma API

A pasta `ferramentas` traz uma API pronta, de uma biblioteca, com os dados na memória. Nesta
prática ela é uma caixa-preta: você conversa com ela só por HTTP, como faria com uma API de
outra empresa, e observa método, caminho, corpo e código de status de cada conversa.

## Preparação

1. Siga a seção "Preparação" do `README.md` da pasta `M7` e instale a extensão REST Client.
2. Num terminal, na pasta `M7`, suba a biblioteca e deixe o terminal aberto:

   ```bash
   python ferramentas/biblioteca.py
   ```

   Cada pedido recebido aparece nesse terminal, com o método, o caminho e o código da resposta.
3. Abra `exercicios/aula8/p1_http/biblioteca.http` e clique em "Send Request" acima do pedido 1.

## Parte A: os pedidos prontos

Envie os pedidos 1 a 7, nesta ordem, e observe a linha de status, os cabeçalhos e o corpo de
cada resposta. As respostas esperadas, com os corpos encurtados:

```text
GET /livros

HTTP/1.1 200 OK

[
  {
    "isbn": "9780000000001",
    "titulo": "Dom Casmurro",
    "autor": "Machado de Assis",
    "ano": 1899,
    "disponivel": true
  },
  {
    "isbn": "9780000000002",
    "titulo": "Memórias Póstumas de Brás Cubas",
    "autor": "Machado de Assis",
    "ano": 1881,
    "disponivel": true
  },
  {
    "isbn": "9780000000003",
    "titulo": "O Cortiço",
    "autor": "Aluísio Azevedo",
    "ano": 1890,
...
    "disponivel": true
  }
]

GET /livros/9780000000003

HTTP/1.1 200 OK

{
  "isbn": "9780000000003",
  "titulo": "O Cortiço",
  "autor": "Aluísio Azevedo",
  "ano": 1890,
  "disponivel": true
}

GET /livros/9780000000099

HTTP/1.1 404 Not Found

{
  "detail": "livro 9780000000099 não encontrado"
}

POST /livros

HTTP/1.1 201 Created
location: /livros/9780000000005

{
  "isbn": "9780000000005",
  "titulo": "A Moreninha",
  "autor": "Joaquim Manuel de Macedo",
  "ano": 1844,
  "disponivel": true
}

POST /livros

HTTP/1.1 409 Conflict

{
  "detail": "o livro 9780000000005 já está cadastrado"
}

POST /livros

HTTP/1.1 422 Unprocessable Content

{
  "detail": [
    {
      "type": "string_pattern_mismatch",
      "loc": [
        "body",
        "isbn"
      ],
      "msg": "String should match pattern '^\\d{13}$'",
      "input": "123",
      "ctx": {
        "pattern": "^\\d{13}$"
      }
    },
    {
      "type": "string_too_short",
      "loc": [
        "body",
        "titulo"
      ],
...
    }
  ]
}
```

## Parte B: os seus pedidos

Escreva os pedidos 8 a 12 no mesmo arquivo, no lugar dos `TODO`, e envie um por vez. Os códigos
esperados: 8 responde 200; 9 responde 201; 10 responde 409; 11 responde 204; 12 responde 204 na
remoção e 404 no GET seguinte.

Se algo der errado no meio, reinicie o servidor (`Ctrl+C` e o comando de novo): os dados voltam
ao começo.

## Parte C: perguntas

Responda numa folha ou num arquivo de anotações:

1. Quais pedidos mudaram alguma coisa no servidor? Quais só consultaram?
2. Envie o pedido 8 duas vezes seguidas. O resultado muda? E se enviar o pedido 9 duas vezes?
   Qual dos dois métodos é idempotente?
3. O 404 do pedido 4 e o 409 do pedido 6 trazem a mensagem em `detail`. O 422 do pedido 7 traz
   uma lista. Quem usa a API consegue mostrar essas mensagens a uma pessoa? O que falta?
4. Qual cabeçalho da resposta do pedido 5 diz onde está o livro novo?

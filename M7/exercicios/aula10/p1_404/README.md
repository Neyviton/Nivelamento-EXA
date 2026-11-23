# Aula 10, Prática 1: o schema Erro e o 404

Hoje, um aluno que não existe derruba a rota: o serviço levanta `NaoEncontradoError`, ninguém
trata, e a API responde 500 com o texto `Internal Server Error`. Quem usa a API não sabe se o
erro foi dele ou do servidor.

Em `secretaria/api/erros.py`, já estão prontos:

* o schema `Erro` (código curto, mensagem e detalhes) e `DetalheErro`;
* a função `resposta(codigo, erro, mensagem, detalhes)`, que monta a resposta nesse formato;
* `RESPOSTAS`, para a documentação (Prática 3), e `registrar(app)`, que `app.py` já chama.

Procure `TODO Aula 10, Prática 1`:

1. Implemente o tratador `nao_encontrado`: 404, o código `nao_encontrado` e a mensagem da
   exceção (`str(erro)`).
2. Em `registrar`, ligue a exceção ao tratador:
   `app.add_exception_handler(NaoEncontradoError, nao_encontrado)`.

Os serviços não mudam: continuam levantando a mesma exceção, sem saber de HTTP.

## Respostas esperadas

Com o servidor no ar, envie os pedidos de `nao_encontrado.http`:

```text
GET /alunos/1999999/boletim

HTTP/1.1 404 Not Found

{
  "erro": "nao_encontrado",
  "mensagem": "aluno 1999999 não encontrado",
  "detalhes": []
}

GET /turmas/CC301/2026.1

HTTP/1.1 404 Not Found

{
  "erro": "nao_encontrado",
  "mensagem": "turma CC301 (2026.1) não encontrada",
  "detalhes": []
}

GET /turmas/ES201/2026.2/matriculas/2025001

HTTP/1.1 404 Not Found

{
  "erro": "nao_encontrado",
  "mensagem": "2025001 não está matriculado em ES201 (2026.2)",
  "detalhes": []
}
```

## Para pensar

* O tratador fica em `api/erros.py`, e não em cada rota. Quantas rotas passaram a responder 404
  com essas duas linhas?
* E se a tela do terminal (M5) e a API precisassem de mensagens diferentes para o mesmo erro?
  Onde cada uma seria escrita?

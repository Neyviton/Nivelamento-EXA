# Desafio da Aula 9: a lista paginada de alunos

Implemente o contrato que você propôs no desafio da Aula 8: a lista dos alunos de um curso, com
filtro opcional pelo ano de ingresso e paginação, em ordem de matrícula.

```text
GET /cursos/CC/alunos?ingresso=2026&pagina=1&tamanho=2
```

Desta vez a funcionalidade atravessa todas as camadas, como os desafios do M5:

1. **Acesso a dados** (`acesso_orm/alunos.py`): contar os alunos do curso (com o filtro) e buscar
   uma fatia deles, com `offset` e `limit`. Acrescente as funções à interface da camada.
2. **Domínio** (`dominio.py`): um tipo para a página.
3. **Serviço** (`servicos/consultas.py`): curso que não existe levanta `NaoEncontradoError`;
   página além do fim devolve a lista vazia.
4. **API**: a conversão para o schema do desafio da Aula 8, uma dependência para a paginação
   (página a partir de 1; tamanho de 1 a 50, 10 se não vier) e a rota em `rotas/cursos.py`.

Respostas esperadas, com o banco recém-criado:

```text
GET /cursos/CC/alunos?ingresso=2026&pagina=1&tamanho=2  -> 200, total 5, Carla Mendes e Fábio Nunes
GET /cursos/CC/alunos?ingresso=2026&pagina=3&tamanho=2  -> 200, total 5, só Olívia Santos
GET /cursos/CC/alunos?ingresso=2026&pagina=4&tamanho=2  -> 200, total 5, lista vazia
GET /cursos/si/alunos                                   -> 200, total 15, os 10 primeiros de SI
GET /cursos/CC/alunos?pagina=0                          -> 422 (por enquanto, o formato do FastAPI)
GET /cursos/XX/alunos                                   -> 500 (por enquanto; a Aula 10 resolve)
```

Entrega: o código nas quatro camadas e um arquivo `desafio.http` com esses pedidos. Confira com
`ruff check .` e `mypy --strict secretaria`.

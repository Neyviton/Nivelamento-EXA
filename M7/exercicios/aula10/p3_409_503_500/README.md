# Aula 10, Prática 3: regras (409), banco fora do ar (503), erro inesperado (500) e /docs

Procure `TODO Aula 10, Prática 3` em `secretaria/api/erros.py`:

1. `regra_de_negocio`: 409 (conflito com o estado da escola), código `regra_de_negocio` e a
   mensagem da exceção.
2. `banco_indisponivel`: 503, código `banco_indisponivel` e uma mensagem genérica,
   `o banco de dados está indisponível; tente de novo mais tarde`. A mensagem da exceção traz o
   endereço do banco, e isso não deve sair do servidor.
3. `erro_inesperado`: 500, código `erro_interno` e a mensagem
   `erro inesperado no servidor; tente de novo mais tarde`, sem detalhes.
4. Em `registrar`, uma linha para cada um, com `Exception` para o erro inesperado.
5. Para a documentação, passe `responses=erros.RESPOSTAS` aos três `APIRouter` (em
   `rotas/alunos.py`, `turmas.py` e `cursos.py`) e confira em /docs que cada rota mostra as
   respostas de erro com o schema `Erro`.

## Respostas esperadas

Recrie o banco e envie os pedidos de `conflitos.http`:

```text
PUT /turmas/CC101/2026.1/matriculas/2025001/nota

HTTP/1.1 409 Conflict

{
  "erro": "regra_de_negocio",
  "mensagem": "o semestre 2026.1 está encerrado; notas só podem ser lançadas em 2026.2",
  "detalhes": []
}

POST /turmas/ES201/2026.2/matriculas

HTTP/1.1 409 Conflict

{
  "erro": "regra_de_negocio",
  "mensagem": "ES201 é uma disciplina de ES, e o aluno é de CC",
  "detalhes": []
}

PUT /turmas/CC201/2026.2/matriculas/2025001/nota

HTTP/1.1 200 OK

{
  "aluno": {
    "matricula": "2025001",
    "nome": "Ana Beatriz Souza",
    "curso": "CC"
  },
  "turma": {
    "codigo": "CC201",
    "disciplina": "Banco de Dados",
    "semestre": "2026.2",
    "professor": "Juliana Teixeira",
    "curso": "CC"
  },
  "nota": 8.5,
  "situacao": "aprovado"
}

DELETE /turmas/CC201/2026.2/matriculas/2025001

HTTP/1.1 409 Conflict

{
  "erro": "regra_de_negocio",
  "mensagem": "a matrícula já tem nota e não pode ser cancelada",
  "detalhes": []
}
```

Para ver o 503, pare o servidor e suba de novo apontando para um banco que não existe (um
PostgreSQL numa porta sem nada):

```bash
# Linux e macOS
DATABASE_URL=postgresql+psycopg://escola:escola@127.0.0.1:5999/escola uvicorn secretaria.api.app:app --reload
# Windows (PowerShell)
$env:DATABASE_URL = "postgresql+psycopg://escola:escola@127.0.0.1:5999/escola"; uvicorn secretaria.api.app:app --reload
```

```text
GET /alunos/2025001/boletim

HTTP/1.1 503 Service Unavailable

{
  "erro": "banco_indisponivel",
  "mensagem": "o banco de dados está indisponível; tente de novo mais tarde",
  "detalhes": []
}
```

Depois, volte ao terminal normal (no PowerShell, `Remove-Item Env:DATABASE_URL`).

O 500 não tem pedido pronto: ele cobre o que ninguém previu. Para vê-lo, ponha por um instante
`1 / 0` na primeira linha da rota do boletim, envie o pedido e desfaça a mudança. O terminal do
servidor continua mostrando o traceback completo; quem chamou recebe só a mensagem genérica.

## Para pensar

* Por que 409 para as regras da escola, e não 422? O que o cliente faz diferente em cada caso?
* Quem precisa do traceback do erro 500: quem chamou a API ou quem mantém o servidor? Onde ele
  deve aparecer?

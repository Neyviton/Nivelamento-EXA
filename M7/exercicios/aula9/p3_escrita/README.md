# Aula 9, Prática 3: rotas de escrita

Procure `TODO Aula 9, Prática 3` em `secretaria/api/rotas/turmas.py`. Os corpos das requisições
já têm schema em `secretaria/api/schemas.py`: `NotaEntrada` e `MatriculaEntrada`.

1. **Lançar nota**: `PUT /turmas/{codigo}/{semestre}/matriculas/{matricula}/nota`, com o corpo
   `corpo: NotaEntrada`. Monte o `LancamentoNota` do M5 com o que veio do caminho e do corpo, e
   chame `notas.lancar_nota`. Responde 200 com `MatriculaSaida`.
2. **Matricular**: `POST /turmas/{codigo}/{semestre}/matriculas`, com `corpo: MatriculaEntrada`.
   Responde 201 (`status_code=status.HTTP_201_CREATED` no decorador) com `MatriculaSaida` e o
   cabeçalho `Location` apontando para a matrícula nova. Para escrever o cabeçalho, receba
   `resposta: Response` como parâmetro e use `resposta.headers["Location"] = ...`.
3. **Cancelar**: `DELETE /turmas/{codigo}/{semestre}/matriculas/{matricula}`. Responde 204, sem
   corpo: `status_code=status.HTTP_204_NO_CONTENT` e retorno `None`.

## Respostas esperadas

Recrie o banco (`python ../M4/ferramentas/criar_banco.py escola.db`, com o servidor no ar mesmo)
e envie os pedidos de `escrita.http`, nesta ordem:

```text
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

POST /turmas/CC102/2026.2/matriculas

HTTP/1.1 201 Created
location: /turmas/CC102/2026.2/matriculas/2026005

{
  "aluno": {
    "matricula": "2026005",
    "nome": "Olívia Santos",
    "curso": "CC"
  },
  "turma": {
    "codigo": "CC102",
    "disciplina": "Estruturas de Dados",
    "semestre": "2026.2",
    "professor": "Ricardo Moura",
    "curso": "CC"
  },
  "nota": null,
  "situacao": "cursando"
}

GET /turmas/CC102/2026.2/matriculas/2026005

HTTP/1.1 200 OK

{
  "aluno": {
    "matricula": "2026005",
    "nome": "Olívia Santos",
    "curso": "CC"
  },
  "turma": {
    "codigo": "CC102",
    "disciplina": "Estruturas de Dados",
    "semestre": "2026.2",
    "professor": "Ricardo Moura",
    "curso": "CC"
  },
  "nota": null,
  "situacao": "cursando"
}

DELETE /turmas/CC102/2026.2/matriculas/2026005

HTTP/1.1 204 No Content

PUT /turmas/CC201/2026.2/matriculas/2025001/nota

HTTP/1.1 422 Unprocessable Content

{
  "detail": [
    {
      "type": "less_than_equal",
      "loc": [
        "body",
        "nota"
      ],
      "msg": "Input should be less than or equal to 10",
      "input": 11,
      "ctx": {
        "le": 10
      }
    }
  ]
}

POST /turmas/CC201/2026.2/matriculas

HTTP/1.1 500 Internal Server Error

Internal Server Error
```

O pedido 5 é recusado pelo schema `NotaEntrada` com 422. O pedido 6 quebra uma regra da escola:
o serviço levanta `RegraDeNegocioError`, e a API ainda responde 500. A Aula 10 resolve.

## Para pensar

* No pedido 1, a nota enviada foi 8.46 e a resposta trouxe 8.5. Qual camada arredondou?
* Envie o pedido 1 de novo. A resposta muda? E o pedido 2, enviado de novo?
* A rota de matrícula monta um `NovaMatricula`, o mesmo schema que a tela do terminal monta no
  M5. O que isso diz sobre onde ficam as regras da escola?

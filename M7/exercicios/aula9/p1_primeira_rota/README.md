# Aula 9, Prática 1: a primeira rota

## 1. Subir a API

Num terminal, na pasta `M7`, com o `.venv` ativo e o `escola.db` criado:

```bash
uvicorn secretaria.api.app:app --reload
```

O terminal mostra `Uvicorn running on http://127.0.0.1:8000`. Deixe-o aberto: cada pedido
recebido aparece ali. Abra `exercicios/aula9/p1_primeira_rota/boletim.http` e envie o pedido 1,
que já funciona (a rota `/saude` está pronta em `app.py`).

Abra também http://127.0.0.1:8000/docs no navegador: a documentação que o FastAPI gera a partir
das rotas. Por enquanto, só a rota de saúde.

## 2. A rota do boletim

Em `secretaria/api/rotas/alunos.py`, procure `TODO Aula 9, Prática 1` e escreva a rota
`GET /alunos/{matricula}/boletim`:

* o decorador `@rotas.get(...)`, com o caminho relativo ao prefixo `/alunos` do router;
* a matrícula como parâmetro da função, com o tipo `MatriculaAluno`, de `secretaria.schemas`;
* o tipo de retorno `BoletimSaida`: o FastAPI usa a anotação para validar e documentar a saída;
* uma docstring curta: ela vira a descrição da rota em /docs;
* o corpo: chame `consultas.consultar_boletim` e devolva `boletim_saida(...)`.

Salve: o `--reload` reinicia o servidor. Envie os pedidos 2 a 4 e recarregue /docs.

## Respostas esperadas

```text
GET /saude

HTTP/1.1 200 OK

{
  "status": "ok"
}

GET /alunos/2025001/boletim

HTTP/1.1 200 OK

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
...
  ],
  "media": 6.67
}

GET /alunos/20251/boletim

HTTP/1.1 422 Unprocessable Content

{
  "detail": [
    {
      "type": "value_error",
      "loc": [
        "path",
        "matricula"
      ],
      "msg": "Value error, deve ter 7 dígitos, como 2025001",
      "input": "20251",
      "ctx": {
        "error": {}
      }
    }
  ]
}

GET /alunos/1999999/boletim

HTTP/1.1 500 Internal Server Error

Internal Server Error
```

O pedido 4 responde 500, e o terminal do servidor mostra o traceback com
`NaoEncontradoError: aluno 1999999 não encontrado`. O serviço fez a parte dele; falta a API
traduzir a exceção para HTTP. Isso fica para a Aula 10.

## Para pensar

* Quem respondeu 422 no pedido 3: a sua rota, o serviço ou o FastAPI? Em que momento?
* Em /docs, abra a rota do boletim e clique em "Try it out". De onde o FastAPI tirou o formato
  da resposta que aparece em "Responses"?
* A rota tem três linhas. Onde está a regra da média, e onde está o SQL?

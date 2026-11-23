# Contrato da API da secretaria

## Casos de uso

| Caso de uso | Método | Caminho | Caminho e consulta | Corpo (JSON) | Sucesso | Erros |
|---|---|---|---|---|---|---|
| Boletim de um aluno | | | | | | |
| Relatório de uma turma | | | | | | |
| Uma matrícula de uma turma | | | | | | |
| Lançar a nota de um aluno | | | | | | |
| Matricular um aluno numa turma | | | | | | |
| Cancelar uma matrícula | | | | | | |
| Ranking de um curso num semestre | | | | | | |

## O JSON de sucesso do boletim

Escreva um exemplo da resposta de `GET` do boletim de 2025001 (a tela do terminal, que continua
funcionando, mostra as notas: `python -m secretaria.apresentacao.boletim 2025001`):

```json
```

## Perguntas

1. Lançar nota: por que PUT, e não POST?
2. Matricular: o que a resposta deve dizer, além do código 201, para quem quiser consultar a
   matrícula nova depois?
3. Cancelar: o que vai no corpo da resposta de um DELETE que deu certo?

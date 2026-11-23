# Aula 8, Prática 2: o contrato da API da secretaria

O sistema da secretaria já sabe fazer tudo pelos serviços do M5. Falta decidir como cada caso de
uso aparece em HTTP: o contrato da API. É isso que você propõe nesta prática, antes de qualquer
código, como nas propostas do M5.

Os serviços disponíveis, em `secretaria/servicos`:

| Serviço | Recebe | Devolve |
|---|---|---|
| `consultas.consultar_boletim` | matrícula | `Boletim` |
| `consultas.relatorio_turma` | código e semestre | `RelatorioTurma` |
| `consultas.consultar_matricula` | matrícula, código e semestre | `Linha` |
| `consultas.ranking` | sigla do curso, semestre e quantos | `list[PosicaoRanking]` |
| `notas.lancar_nota` | `LancamentoNota` (matrícula, código, semestre e nota) | `Linha` |
| `matriculas.matricular` | `NovaMatricula` (matrícula, código e semestre) | `Linha` |
| `matriculas.cancelar_matricula` | `NovaMatricula` | `Matricula` |

**Antes de abrir `secretaria/api/schemas.py`**, preencha `CONTRATO.md`: para cada caso de uso, o
método, o caminho, o que vem no caminho, na consulta e no corpo, o código de sucesso e os códigos
de erro que você espera.

Critérios para o caminho, vistos na aula:

* recursos são substantivos no plural (`/alunos`, `/turmas`), e não verbos (`/lancarNota`);
* o que identifica um recurso vai no caminho; filtros e opções vão na consulta (`?semestre=`);
* o método diz a ação: GET consulta, POST cria, PUT substitui, DELETE remove;
* uma turma é identificada pelo código da disciplina e pelo semestre.

No fim, compare a sua proposta com a tabela "O contrato da API" do `README.md` da pasta `M7`.
Anote as diferenças e o motivo de cada uma: a discussão em aula parte delas.

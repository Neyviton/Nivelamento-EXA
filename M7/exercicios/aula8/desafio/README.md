# Desafio da Aula 8: a lista de alunos de um curso, com filtro e paginação

A coordenação quer listar os alunos de um curso pela API, com um filtro opcional pelo ano de
ingresso. São 15 alunos por curso hoje, e serão muitos mais: a lista precisa vir em páginas.

Desta vez o desafio é só de contrato, sem rota. Na Aula 9, você implementa o que propuser aqui.

1. Acrescente à sua `CONTRATO.md` uma linha para esse caso de uso: método, caminho, parâmetros
   de consulta (o filtro, a página e o tamanho da página, com os valores padrão e os limites),
   código de sucesso e códigos de erro.
2. Escreva em `secretaria/api/schemas.py` o schema de saída da página: além dos alunos, o que
   quem usa a API precisa saber para pedir a próxima página e para mostrar "página 1 de 3"?
3. Escreva na `CONTRATO.md` um exemplo do JSON da primeira página dos ingressantes de 2026 do
   curso CC, com 2 alunos por página, em ordem de matrícula. São cinco ingressantes, de
   2026001 (Carla Mendes) a 2026005 (Olívia Santos).

Entrega: a `CONTRATO.md` com a linha e o exemplo, e o schema novo. Confira estilo e tipos com
`ruff check .` e `mypy --strict secretaria`.

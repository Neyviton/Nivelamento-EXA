"""Camada de apresentação HTTP: a API da secretaria (M7).

Regras desta camada, as mesmas da apresentação do terminal:
* recebe o pedido HTTP, monta os schemas de entrada e chama um serviço por rota;
* transforma o resultado do serviço num schema de saída, que vira o JSON da resposta;
* transforma as exceções das camadas de baixo em respostas de erro (Aula 10).

Não abre o banco e não tem regra de negócio: isso continua nos serviços e nos managers.
"""

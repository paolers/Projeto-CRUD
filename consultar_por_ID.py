import json

def consultar_transacao_por_ID():
    """
    Consulta uma transação específica pelo seu UUID.
    """

    uuid_escolhido = input('Insira o UUID da transação que deseja consultar:\n')

    #abrindo o arquivo json pra leitura
    with open('data/transactions.json', 'r', encoding='utf-8') as json_file:
        transacoes = json.load(json_file) ## na biblioteca Json, leitura chama load

     # itera sobre a lista de transações
    for transacao in transacoes:
         #verifica se o valor da chave é igual ao uuid dado no input
         if transacao['UUID'] == uuid_escolhido:
            #acessa os valores do dicionário  
            valor = transacao['valor']
            categoria = transacao['categoria']
            print(f"Valor: {valor}, Categoria: {categoria}")
            break
    
consultar_transacao_por_ID()
    
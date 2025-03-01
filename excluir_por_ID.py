import json

def excluir_transacao():
    """
    Exclui uma transação específica pelo UUID.
    """

    with open('data/teste.json', 'r', encoding='utf-8') as json_file:
            transacoes = json.load(json_file)

    while True:
        try:
            uuid_escolhido = input('Insira o UUID da transação que deseja excluir:\n')
            break
        except ValueError:
            print('Entrada inválida.')

    for transacao in transacoes:
        if transacao['UUID'] == uuid_escolhido:
            print(f'A transação a ser removida é: {transacao}')

    for transacao in transacoes:
        if transacao['UUID'] == uuid_escolhido:
            transacoes.remove(transacao)
            break
    
    with open('data/teste.json', 'w', encoding='utf-8') as json_file:
        json.dump(transacoes, json_file, ensure_ascii=False, indent=4)

    print('Transação removida com sucesso!')

excluir_transacao()
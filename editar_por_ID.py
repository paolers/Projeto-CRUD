import json

def editar_transacao_por_ID():
    """
    Edita uma transação específica pelo seu UUID.
    """

    with open('data/teste.json', 'r', encoding='utf-8') as json_file:
        transacoes = json.load(json_file)

    while True:
        try:
            uuid_escolhido = input('Insira o UUID da transação que deseja editar:\n')
            break
        except ValueError:
            print('Entrada inválida.')

    for transacao in transacoes:
         if transacao['UUID'] == uuid_escolhido:
            print(f'A transação a ser modificada é a seguinte:\n {transacao}.')
            break

    while True:
        try:
            novo_valor = float(input('Insira o novo valor para a transação escolhida:\n'))
            break
        except ValueError:
            print('Entrada inválida, insira um valor numérico.')  

    while True:
        try:
            categoria = int(input('Insira a nova categoria da transação:\n'
                            '1 - Casa\n'
                            '2 - Lazer\n'
                            '3 - Viagens\n'
                            '4 - Investimentos\n'
                            '5 - Transferências\n'
                            '6 - Saúde\n'
                            '7 - Alimentação\n'                
                            ))
            if categoria in range(1,8):
                break
            else:
                print("Valor inválido, insira um dos índices informados.")
        except ValueError:
            print("Valor inválido, insira uma entrada numérica.")

    match categoria:
        case 1:
            categoria_nova = 'casa'
        case 2:
            categoria_nova = 'lazer'
        case 3:
            categoria_nova = 'viagens'
        case 4:
            categoria_nova = 'investimentos'
        case 5:
            categoria_nova = 'transferencias'
        case 6:
            categoria_nova = 'saude'
        case 7:
            categoria_nova = 'alimentação'

    for transacao in transacoes:
         if transacao['UUID'] == uuid_escolhido:
            #modificando os valores do dicionário  
            transacao['valor'] = novo_valor
            transacao['categoria'] = categoria_nova
            break
    
    with open('data/teste.json', 'w', encoding='utf-8') as json_file:
        json.dump(transacoes, json_file, ensure_ascii=False, indent=4)
        
    print(f"A transação foi modificada com sucesso!\n {transacao}")
    
editar_transacao_por_ID()    
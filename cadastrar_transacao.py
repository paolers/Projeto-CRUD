import json
import uuid

def cadastrar_transacao():

    """
    Cadastra uma nova transação.
    \nObs:Para gerar um novo uuid, veja como é feito na função `criar_transacoes`.
    """

    while True:
        try:
            categoria = int(input('Insira a categoria da transação:\n'
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
    
    while True:
        try:   
            valor = float(input('Insira o valor da transação:\n'))
            break
        except ValueError:
            print("Valor inválido, insira uma entrada numérica.")

    with open('data/teste.json', 'r', encoding='utf-8') as json_file:
        transacoes = json.load(json_file)

    #definindo o dicionario da nova transação, com um valor de uuid gerado
    #e valor e categoria definidos pelo usuário
    transacao = {
                "UUID": str(uuid.uuid4()),
                "valor": valor, 
                "categoria": categoria_nova
                }
    transacoes.append(transacao)

    # grava a nova transação no arquivo JSON
    with open('data/teste.json', 'w', encoding='utf-8') as json_file:
        json.dump(transacoes, json_file, ensure_ascii=False, indent=4)

    print('Transação adicionada com sucesso!')
    return transacoes

print(cadastrar_transacao())
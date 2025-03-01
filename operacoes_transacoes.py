import json

def calcular_total_transacoes(arquivo):
    """
    Calcula o valor total de transações da conta.
    Utilize essa mesma função para o caso `por categoria`
    """
    total = 0

    for transacao in arquivo:
        valor = transacao['valor']
        total += valor

    total = round(total, 2)
    return total

def calcular_media(arquivo):
    total = 0

    for transacao in arquivo:
        valor = transacao['valor']
        total += valor
    media = total/len(arquivo)
    media = round(media, 2)
    return media

def mostrar_m5_transacoes(m):
    """
    Mostra as m5 transações realizadas, sendo m parâmetro que deve ser adicionada à função.
    \nm : 'max','min','median', sendo 
    \n\t'max' mostra os top 5 maior valor,
    \n\t'min' mostra os top 5 menor valor,
    \n\t'mean' mostra os top 5 valores próximos a média
    
    Utilize essa mesma função para o caso `por categoria`
    """

    with open('data/teste.json', 'r', encoding='utf-8') as json_file:
        transacoes = json.load(json_file)

    if m == 'max':
        resultado = m5('max', transacoes)
    elif m == 'min':
        resultado = m5('min', transacoes)
    elif m == 'mean':
        resultado = m5('mean', transacoes)
    return resultado

def m5(m, arquivo):
    if m == 'max':
        dados = sorted(arquivo, key=lambda x: x['valor'], reverse=True)
        max_5 = dados[:5]
        valores = [{"valor": item['valor']} for item in max_5]
        print(f'Os 5 maiores valores de transação são: {valores}')
        return valores
    elif m == 'min':
        dados = sorted(arquivo, key=lambda x: x['valor'])
        min_5 = dados[:5]
        valores = [{"valor": item['valor']} for item in min_5]
        print(f'Os 5 menores valores de transação são: {valores}')
        return valores
    elif m == 'mean':
        media = calcular_media(arquivo)
        dados = sorted(arquivo, key=lambda x: x['valor'] - media)
        mean_5 = dados[:5]
        valores = [{"valor": item['valor']} for item in mean_5]
        print(f'Os 5 valores de transação mais próximos da média ({media}) são: {valores}')
        return valores
    
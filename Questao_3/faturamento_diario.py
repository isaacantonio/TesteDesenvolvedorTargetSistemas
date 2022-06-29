import json

with open("dados.json", encoding='utf-8') as faturamento_json:
    dados = json.load(faturamento_json)


def menorValor(dados):
    menor = dados[0]['valor']
    for i in dados:
        if i['valor'] > 0.0 and i['valor']<menor:
            menor = i['valor']
    return menor

def maiorValor(dados):
    maior = dados[0]['valor']
    for i in dados:
        if i['valor'] > 0.0 and i['valor']>maior:
            maior = i['valor']
    return maior

def mediaMensal(dados):
    sum = 0
    contador = 0
    for i in dados:
        if i['valor'] > 0.0:
            sum += i['valor']
            contador +=1
    return sum/contador

def superiores_a_media(dados):
    contador = 0
    for i in dados:
        if i['valor'] > mediaMensal(dados):
            contador +=1
    return contador

print('Menor valor de faturamento ocorrido em um dia do mês: ',menorValor(dados))

print('Maior valor de faturamento ocorrido em um dia do mês: ', maiorValor(dados))

print('Numero de dias no mês em que o valor de faturamento diário foi superior à média mensal: ', superiores_a_media(dados))

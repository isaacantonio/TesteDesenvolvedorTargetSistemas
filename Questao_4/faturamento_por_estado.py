dados_faturamento  = [
    {
    'estado': 'SP', 'faturamento' : 67836.43
        },
    {
    'estado': 'RJ', 'faturamento' : 36678.66
        },

    {
    'estado': 'MG', 'faturamento' : 29229.88
        },
    {
    'estado':'ES', 'faturamento' : 27165.48
        },
    {
    'estado': 'Outros', 'faturamento' : 19849.53
        }
]
#Escreva um programa na linguagem que desejar onde calcule o percentual de representação
#que cada estado teve dentro do valor total mensal da distribuidora.


def soma_faturamento(dados):
    soma = 0
    for i in dados:
        soma += i['faturamento']
    return soma

def calcular_percentual(dados):
    print(' Valor total mensal da distribuidora = R$', soma_faturamento(dados), '\n', 'Percentual por estado: ')
    for i in dados:
         print(i['estado'], ' - ', (i['faturamento']*100)/soma_faturamento(dados), '%')

calcular_percentual(dados_faturamento)
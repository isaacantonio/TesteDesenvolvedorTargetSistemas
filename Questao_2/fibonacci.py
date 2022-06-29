# Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci
# e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def verificar(num):
    contador = 1
    while True:
        if num == fibo(contador):
            return "Pertence a sequencia"
        elif num < fibo(contador):
            return "O numero não pertence a sequencia"
        contador+=1
aux = 1
while True:
    aux = int(input("Informe um numero para verificar se esta na sequencia de fibonacci (OU DIGITE 0 PARA SAIR): "))
    if aux == 0:
        print("----------------------------------------------FIM----------------------------------------------")
        break
    print(verificar(aux))


#Escreva um programa que inverta os caracteres de um string.
palavra = str(input("Informe uma palavra: "))
tam = len(palavra)
reverse = ""
while True:
    tam -= 1
    if tam == -1:
        break
    reverse+=palavra[tam]

print(reverse)
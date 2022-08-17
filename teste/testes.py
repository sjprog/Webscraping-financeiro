from time import sleep


frase = input('Digite uma frase:')
letras = 0
palavras = 1

for i in frase:
    if i == ' ':
        palavras = palavras + 1
    else:
        letras = letras + 1
print(f'{letras} Letras: ')
print(f'{palavras} Palavras:')
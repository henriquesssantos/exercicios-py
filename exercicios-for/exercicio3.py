''' Escreva um algoritmo que leia um valor inicial A e imprima a sequência de
valores do cálculo de A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120
'''

fatorial= int(input('digite o fatorial que deseja: '))
resultado = 1
saida = ""

for i in range(fatorial, 0, -1):
    if fatorial == i:
        saida = f'{fatorial}! = {i} x'
    elif i == 1:
        saida = saida + f' {i} = {resultado}'
    else:
        saida = saida + f' {i} x '
    resultado = resultado * i 

print(saida)
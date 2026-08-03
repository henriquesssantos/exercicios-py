''' Escrever um algoritmo que gera e escreve os números ímpares entre 100 e
200.
'''

contador = 1

for i in range(100, 201):
    if i % 2 != 0:  
        print(f'{contador}° numero ímpar = {i}')
        contador = contador + 1
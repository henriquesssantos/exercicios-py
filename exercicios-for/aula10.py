#exemplo contador
from time import sleep


#while 
'''
contador = 0

while contador < 10:
    print(contador)
    contador += 1
    sleep(1) #pausa de 1 segundo

'''

#for
'''
for i in range(1, 11): #star, stop, step
    print(i)
    sleep(1) #pausa de 1 segundo, biblioteca time
'''


#regressiva
'''
for i in range(10, 0, -1): #star, stop, step
    print(i)
    sleep(1) #pausa de 1 segundo, biblioteca time

'''
#soma
'''
soma = 0
pares = 0
impares = 0 

for n in range(1, 501):
    soma += n
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
print(soma)
print(f'Quantidade de números pares: {pares}')
print(f'Quantidade de números ímpares: {impares}')
'''

#multiplos de três
'''
multiplos = 0

for n in range(1, 501):
    if n % 3 == 0:
        multiplos += 1

print(f'Quantidade de múltiplos de 3: {multiplos}')
'''

#tabuada
'''
num = int(input('Digite um número para ver a tabuada: '))

for i in range(1, 11):
    resultado = num * i
    print(f'{num} x {i} = {resultado}')
    sleep(1)
'''

#tabuada personalizada
num = int(input('Digite um número para ver a tabuada: '))
inicio = int(input('Digite em qual numero a tabuada inicia:'))
termino = int(input('Digite em qual numero a tabuada termina:'))

for i in range(inicio, termino):
    resultado = num * 

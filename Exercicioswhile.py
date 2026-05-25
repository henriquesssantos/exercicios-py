# exercicios 1

"""
Escrever um algoritmo que leia um número n que indica quantos valores
devem ser lidos a seguir. Para cada número lido, mostre uma tabela
contendo o valor lido e o fatorial deste valor.


f = int(input('numeros para fatorar:'))

while f > 0:
    fat = 1
    fatorial = int(input('numero para fatorar:'))
    for i in range(1, fatorial + 1):
        fat = fat * i
    print(f'{fatorial}! = {fat}')
    f = f - 1
"""  

#exercicios 2

'''   Escrever um algoritmo que leia uma quantidade de números que deve ser
lidos e conte quantos deles estão nos seguintes intervalos: [0.25], [26,50],
[51,75] e [76,100].


quant = int(input('quantidade de numeros:'))
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0

while quant > 0:
    num + int(input('quais numeros serão analisisados: '))
    if num >= 0 and num <= 25:
        cont1 += 1
    elif num >= 26 and num <= 50:
        cont2 += 1
    elif num >= 51 and num <= 75:
        cont3 += 1
    elif num >= 76 and num <= 100:
        cont4 += 1
    quant -= 1

print(f'Números no intervalo [0,25]: {cont1}')
print(f'Números no intervalo [26,50]: {cont2}')
print(f'Números no intervalo [51,75]: {cont3}')
print(f'Números no intervalo [76,100]: {cont4}')
'''

#exercicios 3

''' Faça um algoritmo que leia 10 números inteiros e calcule o somatório dos
números negativos.

numeros = 10
soma_negativos  = 0

while numeros > 0:
    num = int(input('Digite um número inteiro: '))
    if num < 0:
        soma_negativos += num
    numeros -= 1

print(f'O somatório dos números negativos é: {soma_negativos}')'''

#exercicios 4

''' Chico tem 1,50m e cresce 2 centímetros por ano, enquanto Juca tem 1,10m e
cresce 3 centímetros por ano. Construir um algoritmo que calcule e imprima
quantos anos serão necessários para que Juca seja maior que Chico.  

chico = 1.50
juca = 1.10
anos = 0
while juca < chico:
     chico += 0.02
     juca += 0.03 
     anos += 1

print(f'Juca será maior que Chico em {anos} anos. O tamano de Chico será {chico:.2f} metros e o tamanho de Juca será {juca:.2f} metros.')
'''

#exercicios 5  

''' Faça um algoritmo que leia vários números e informe quantos desses
números entre 100 e 200 foram digitados. Quando o valor 0 (zero) for lido o
algoritmo deverá cessar sua execução.

cont = 0
i = None

while i != 0:
    i = int(input('digite um numero(0 para parar): '))
    if i >= 100 and i <= 200:
        cont += 1

print(f'Quantidade de números entre 100 e 200: {cont}')'''

#exercicios 6  

'''Uma rainha requisitou os serviços de um monge, o qual exigiu o pagamento
em grãos de trigo da seguinte maneira: os grãos de trigo seriam dispostos em
um tabuleiro de xadrez, de tal forma que a primeira casa do tabuleiro tivesse
um grão, e as casas seguintes o dobro da anterior. Construa um algoritmo
que calcule quantos grãos de trigo a Rainha deverá pagar ao monge. Um
tabuleiro tem 64 casas.

grãos = 1
total_grãos = 0

for i in range(64):
    total_grãos = grãos + total_grãos
    grãos = grãos * 2

print(f'Quantidade total de grãos de trigo: {total_grãos}')'''

#exercicios 7 

'''Construa um algoritmo que leia uma quantidade indeterminada de números
inteiros positivos e identifique qual foi o maior número digitado. O final da
série de números digitada deve ser indicado pela entrada de –1.

maior = 0
i = 0
 
while i != -1:
    i = int(input('Digite um número inteiro positivo (-1 para parar): '))
    if i > maior:
        maior = i
    
print(f'O maior número digitado foi: {maior}')'''
'''

i = 1
soma = 0

while i <= 10:
    soma = soma + i
    i = i +1 
    print(soma)

===================================================================================
exemplo com for 

for i in range(1,501):
    soma = soma + i 

===================================================================================

n = int(input("informe o numero:"))
soma = 0
somaPR= 0
somaIM = 0
i = 1

while i <= n:
    soma = soma + i
    print (f'ciclo {i}, a soma sem condições é {soma}')
    if i % 2 == 0:
        somaPR = somaPR + i
        print(f'ciclo {i}, a soma dos numeros pares de 1 a {n}, é {somaPR}')
    else: 
        somaIM = somaIM + i
        print(f'ciclo {i}, a soma dos numeros impares de 1 a {n}, é {somaIM}')
    
    i = i + 1

===================================================================================

inicial = int(input("informe o numero de inicio:"))
final = int(input("informe o numero final:"))
i = 0
soma = 0
valorInicial = inicial
multi = 0

while valorInicial <= final:
    if valorInicial % 3 == 0:
        soma = soma + valorInicial
        multi = multi +  1
    else:
        pass
    valorInicial = valorInicial + 1
    

print(f'A quantidade de multiplos de 3, apartir de {inicial} até {final}, é {multi}')


===================================================================================

tabuada = int(input("qual tabuada você deseja?"))
i = 1

while i <= 10:
    r = tabuada * i
    print(f'{tabuada} X {i} = {r}')
    i = i + 1

===================================================================================

tabuada = int(input("qual tabuada você deseja?"))
inicio = int(input("onde inicia:"))
fim = int(input("onde acaba:"))
i = inicio

while i <= fim:
    r = tabuada * i
    print(f'{inicio} X {i} = {r}') 
    i = i + 1

===================================================================================
'''
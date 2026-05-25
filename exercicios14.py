'''
A prefeitura de uma cidade fez uma pesquisa entre seus habitantes,
coletando dados sobre o salário e número de filhos. A prefeitura deseja
saber:
a. média do salário da população;
b. média do número de filhos;
c. maior salário;
d. percentual de pessoas com salário até R$100,00. 

salario = 0
somaSalarios = 0
mediaSalarios = 0

filhos = 0
somaFilhos = 0
mediaFilhos = 0

maiorSalario = 0
contHabitantes = 0
cont_pessoas_1500 = 0
percentualHabitantes = 0

while salario >= 0 :
    salario = float(input("digite seu salário: "))
    somaSalarios += salario

    if salario < 0:
        break
    
    filhos = int(input("Digite quantos filhos possui:"))
    somaFilhos += filhos

    if salario > maiorSalario:
        maiorSalario = salario
    
    if salario >= 0 and salario <= 1500:
        contHabitantes1500 += 1

    contHabitantes += 1 

mediaSalarios = somaSalarios / contHabitantes
mediaFilhos = somaFilhos / contHabitantes
percentualHabitantes = contHabitantes * 100 / cont_pessoas_1500

print(f"No total, {contHabitantes} habitantes foram consultados.")
print(f"A média salarial é de R${round(mediaSalarios,2)} ")
print(f"A média de filhos é de {round(mediaFilhos,2)} filhos ")
print(f"O maior salário é de R${maiorSalario}")
print(f"{round(percentualHabitantes,2)}% dos habitantes possuem um salário até R$1500.00")

print("FIM!")'''

#EXERCICIO 2

'''Faça um programa que calcule e escreva a seguinte soma: soma = 1/1 + 3/2
+ 5/3 + 7/4 + Desenvolver um algoritmo que efetue a soma de todos os
números ímpares que são múltiplos de três e que se encontram no conjunto
do... + 99/50


soma = 0
num = 1

for i in range(1,51):
    soma = soma + (num/i)
    num = num + 2
'''

#EXERCICIO 3

'''Liste os números de 1 até 500.'''

for i in range(1, 501):
    print(f'{i}')
    i += 1




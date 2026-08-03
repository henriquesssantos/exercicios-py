# exercicio 1 
'''
moeda1 = int(input("digite a quantidade de moedas de 1 centavo:"))
moeda5 = int(input("digite a quantidade de moedas de 5 centavo:"))
moeda10 = int(input("digite a quantidade de moedas de 10 centavo:"))
moeda25 = int(input("digite a quantidade de moedas de 25 centavo:"))
moeda50 = int(input("digite a quantidade de moedas de 50 centavo:"))
moeda1Real = int(input("digite a quantidade de moedas de 1 real"))

total= (moeda1 * 0.01) + (moeda5 * 0.05) + (moeda10 * 0.1) + (moeda25 * 0.25) + (moeda50 * 0.50) + moeda1Real
print(f'o total de moedas em reais foi de {total}')
'''


#exercicio 2
'''
agua = 8/10
suco = 2/10

litrosSuco = float(input("digite quantos litros de suco você precisa:"))

quantidadeAgua = litrosSuco * 0.8
quantidadeSuco = litrosSuco * 0.2

print(f'A quantidade de agua necessária será de {quantidadeAgua}L, e de suco sera de {quantidadeSuco}L')
'''

#exercicio 3
'''
preco = float(input('digite o antigo preço do produto'))

desconto = preco * 0.1
precoNovo = preco - desconto

print(f'o novo preço é de R${precoNovo}')
'''

#exercicio 4
'''
SalarioFIxo = float(input('digite seu salario fixo:'))
vendasRealizadas = float(input('digite o valor vendido deste mes:'))

salarioFinal = ( vendasRealizadas * 0.4) + SalarioFIxo

print(f'Seu salario total foi de {salarioFinal}')
'''
#exercicio 5
'''
peso = float(input('digite seu peso atual:'))

pesoEngordar = (peso * 0.15) + peso
pesoEmagrecer = peso - (peso * 0.20) 

print(f'com sei peso atual sendo {peso}\n caso você engorde seu peso será de {pesoEngordar}\n caso emagreça seu peso será de {pesoEmagrecer}')
'''
#exercicio 6
'''
salarioMinino = float(input('digite o valor do salário minimo:'))
salarioFuncionario = float(input('digite o seu salario:'))

salarios = salarioFuncionario / salarioMinino
print(f'a quantidade de salarios minimos que você recebe é de {salarios}')
'''
#exercicio 7
'''
numero = int(input('de qual nunemo deseja saber a tabuada?'))
print(f'A tabuada de {numero} é:\n {numero * 1}\n{numero *2}\n{ numero *3}\n{ numero *4}\n{ numero *5}\n{ numero *6}\n{ numero *7}\n{ numero *8}\n{ numero *9}\n{ numero *10}')
'''
#exercicio 8
anoNascimento = int(input('digite o ano que você nasceu:'))
anoAtual = int(input('digite o ano atual:'))

idadeAnos = anoAtual - anoNascimento
print(f'sua idade em anos é:{idadeAnos}')

idadeMeses = idadeAnos * 12
print(f'sua idade em meses é de:{idadeMeses}')

idadeDias = idadeAnos * 365
print(f'Sua idade em dias é de:{idadeDias}')

idadeSemanas = idadeDias / 7
idadeSemanas = round(idadeSemanas, 1)
print(f'Sua idade em semanas é de:{idadeSemanas}')

#exercicio 9
'''
salarioJoao = 1200
c1 = 200
c2 = 120

c1Atrasada = (c1 * 0.02)+c1
C2Atrasada = (c2 * 0.02)+c2

print(f'recebendo o salario de {salarioJoao}, tendo o valor da conta 1 com o atraso sendo {c1Atrasada}\nTendo a conta 2 com o atraso sendo {C2Atrasada}\nO restante do salario sera de {salarioJoao - c1Atrasada - C2Atrasada} ')
'''

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

'''Liste os números de 1 até 500.

for i in range(1, 501):
    print(f'{i}')
    i += 1
'''
#EXERCICIO 4

'''Foi feita uma pesquisa entre os habitantes de uma região e coletados os
dados de altura e sexo (0=masc, 1=fem) das pessoas. Faça um programa
que leia 50 dados diferentes e informe:
a. a maior e a menor altura encontradas;
b. a média de altura das mulheres;
c. a média de altura da população;
d. o percentual de homens na população.

altura =0
sexo = None

contPessoas=0

maiorAltura =0
menorAltura =0

somaAltFeminino = 0
contFeminino =0
mediaFeminino =0
mediaPessoas =0

somaAltHomens =0
contHomens =0
percentualHomens =0

for i in range(1,51):
    altura = float(input('digite sua altura: '))

    if i == 1:
        maiorAltura = altura
        menorAltura = altura
    if altura > maiorAltura:
        maiorAltura = altura
    elif altura < menorAltura:
        menorAltura = altura

    sexo = int(input('Digite seu sexo(0 = masculino / 1 = feminino): '))

    if sexo == 1:
        somaAltFeminino = somaAltFeminino + altura
        contFeminino += 1

    elif sexo == 0:
        somaAltHomens = somaAltHomens + altura
        contHomens += 1
         
    else:
        continue


mediaFeminino = somaAltFeminino / contFeminino
mediaPessoas = (somaAltFeminino + somaAltHomens) / (contFeminino + contHomens)
percentualHomens = contHomens * 100 / (contHomens + contFeminino)

print(maiorAltura)
print(menorAltura)
print(mediaFeminino)
print(mediaPessoas)        
'''

#EXERCICIO 5    

'''Criar um algoritmo que leia os limites inferior e superior de um intervalo e
imprima todos os números pares no intervalo aberto e seu somatório.
Suponha que os números digitados são um intervalo crescente.
Exemplo:
- Limite inferior: 3
- Limite superior: 12
- Saída: 4 6 8 10
- Soma: 28

limInf = int(input("Informe o limite inferior do intervalo: "))
limSup = int(input("Informe o limite superior do intervalo: "))
saida = str()
soma = 0

for i in range(limInf, limSup):
    if i % 2 == 0:
        soma += i
        saida = saida + " " + str(i)
   
   

print(f"Limite inferior: {limInf}")
print(f"Limite superior: {limSup}")
print(f"Saída:{saida}")
print(f"Soma: {soma}")

print("FIM!")''' 

#EXERCICIO 6

'''6. Faça um algoritmo que leia tantos números quanto o usuário desejar e
imprima a soma deles.

soma = 0
controle = 1

while controle == 1:
    controle = int(input('Deseja continuar? (digite 1 se sim)'))

    if controle == 1:
        numero = int(input(Informe um numero: ))
        soma = soma + numero
    else:
        controle = 0

print(soma)'''

#EXERCICIO 7

'''Faça um algoritmo que permita ao usuário informar a idade de quantas
pessoas ele desejar. Após isso o algoritmo deve informar a soma das
pessoas maiores de idade e a média de idade das pessoas maiores de idade
informadas'''

idade = 0
somaIdade = 0
mediaIdade = 0
controle = 1
totalPessoas = 1

while controle == 1:
    controle = int(input('deseja continuar? (digite 1 para sim): '))
    if controle == 1:
        idade = int(input('informe a idade:'))
        if idade >= 18:
            somaIdade = somaIdade + idade
            totalPessoas += 1
        else:
            continue
    

mediaIdade = somaIdade / totalPessoas

print(f'com o total de pessoas sendo {totalPessoas}, a media das idades foi de {mediaIdade}')

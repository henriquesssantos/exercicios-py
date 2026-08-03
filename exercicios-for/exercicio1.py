''' 1. Desenvolver um algoritmo que leia a altura de 15 pessoas. Este programa
deverá calcular e mostrar :
a. A menor altura do grupo;
b. A maior altura do grupo; 
'''

maior = None
menor = None
alt = None

for i in range (1,16):
    altura = float(input("Informe a altura: "))
    if i == 1:
        maior = altura
        menor = altura
   
    if altura < menor:
        menor = altura
    elif altura > maior:
        maior = altura

print("---")
print(f"A maior altura é: {maior}")
print(f"A menor altura é: {menor}")
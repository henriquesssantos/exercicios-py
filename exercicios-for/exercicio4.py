''' Escrever um algoritmo que lê 5 valores para a, um de cada vez, e conta
quantos destes valores são negativos.
'''

a = None
contNegativos = 0

for i in range(1,6):
    a = int(input(f"digite o valor {i}:"))
    if a < 0:
        contNegativos = contNegativos + 1
print(contNegativos)
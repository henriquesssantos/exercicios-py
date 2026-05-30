num = 0
num1 = 0
num2 = 0
qntOperacao = 0
soma = 0
subtracao = 0
multiplicacao = 0

while True:
    operacao = int(input('Digite o numero da operação que deseja (1- Soma, 2- Subtrair, 3- Multiplicar, 4- Sair): '))
    if operacao == 1:
        qntOperacao = int(input('digite a quantidade de numeros que deseja operar: '))
        for i in range(qntOperacao +1):
            num = int(input('Digite o numero que deseja operar: '))
            num += num
            qntOperacao = qntOperacao -1
    elif operacao == 2:
        qntOperacao = int(input('digite a quantidade de numeros uqe deseja operar'))
        for i in range(qntOperacao +1):
            num = int(input('digite quantos numeros deseja subtrair'))
            

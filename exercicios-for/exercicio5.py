'''
Em uma eleição presidencial existem quatro candidatos. Os votos são
informados através de códigos. Os dados utilizados para a contagem dos
votos obedecem à seguinte codificação:
a. 1,2,3,4 = voto para os respectivos candidatos;
b. 5 = voto nulo;
c. 6 = voto em branco;
d. Elabore um algoritmo que leia o código do candidato em um voto.
Calcule e escreva:
e. total de votos para cada candidato;
f. total de votos nulos;
g. total de votos em branco;
Faça um algoritmo para ler pelo menos 100 votos.
'''


cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
branco = 0
nulo = 0

for i in range(1,4):
    a = int(input("Informe seu voto: "))
    if a == 1:
        cand1 += 1
    elif a == 2:
        cand2 += 1
    elif a == 3:
        cand3 += 1
    elif a == 4:
        cand4 += 1
    elif a == 6:
        branco += 1
    else:
        nulo += 1
   
print("Apuração dos votos")
print(f"Candidato 1: {cand1}")
print(f"Candidato 2: {cand2}")
print(f"Candidato 3: {cand3}")
print(f"Candidato 4: {cand4}")
print(f"Votos brancos: {branco}")
print(f"Votos nulos: {nulo}")

'''
cand1 = cand2= nulo =branco = None

for i in range(1,101):
    voto = ('voto: ')

    match voto:
        case "1":
          cand1 + cand1 + 1
          break
        case "2":
          cand2 = cand2 + 1
          break
        case " ":
          branco = branco + 0
          break

'''
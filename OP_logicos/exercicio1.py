n = 5 - 10
c1 = -10 > n #variavel boleana falsa
c2 = -15 > n #variavel boleana falsa

r1 = c1 or c2 #compativo "ou" entre duas boleanas, umas ou outra precisa ser true para que o resultado
# true
#false or false = false

r2 = c1 and c2 #compativo "e" entre duas boleanas, umas e a outra precisa ser true para que o resultado
# true
#false and false = false

print(c1, c2) 
print(r1, r2)


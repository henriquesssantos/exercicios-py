n = 10 % 2 #% é o resto da divisão

c1 = 9 > n
c2 = 0 > n
r1 = not c1 and c2
''' not c1' resolve primeiro o not. o c1 era verdadeiro, porem o not o inverte, e passa a ser false 
o c2 é false e passa a ser true. porem no "and", as duas saidas precisam ser true para que a resposta seja
true'''
 
r2 = c1 or not c2
''' c1 continua sendo true, o c2 era false, porem com o not na frente a resposta dele passa a ser true. OR
basta que um dos dois sejam verdadeiros para que o resultado seja verdadeiro. '''

print(c1, c2)
print(r1, r2)
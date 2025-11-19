import os
os.system('cls')

def somar(a=0,b=0,c=0):
    s= a+b+c
    return s

r1= somar(3,4,5)#guardando o resultado da soma na variável r1
r2= somar(3,4)#guardando o resultado da soma na variável r2
r3= somar(3)#guardando o resultado da soma na variável r3
print(f'Os resultados são {r1}, {r2} e {r3}')
print(f'as somas deram {somar(3,4,5)}, {somar(3,4)} e {somar(3)}')#pode usar caso voccê não precise guardar o resultado em uma variável
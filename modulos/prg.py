import os
import calc
os.system('cls')

num = int(input('Digite aqui-->'))

fat=calc.fatorial(num)
dob=calc.dobro(num)
tri=calc.triplo(num)

print(f'O fatorial de {num} é {fat}')
print(f'O fatorial de {num} é {dob}')
print(f'O fatorial de {num} é {tri}')
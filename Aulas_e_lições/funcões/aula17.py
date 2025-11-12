def parimpar(num=0):
    if num % 2 ==0:
        return True
    else:
        return False

n= int(input('Digite um número-->'))
if parimpar(n):
    print(f'o número {n} é par')
else:
    print(f'o número {n} é ímpar')
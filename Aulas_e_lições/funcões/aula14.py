def teste(b):#b é um parametro da função teste
    a=2
    b +=3#modifica o valor de b somando 3
    print(f'na função teste a vale {a}')
    print(f'na função teste bb vale {b}')
    '-------------------------------------------'
a=5
teste(a)#chama a função teste e passa o valor de a como argumento para o parametro b
print(f'no programa principal a vale {a}')#mostra o valor de a no programa principal
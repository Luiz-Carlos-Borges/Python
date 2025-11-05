#uma função faz uma tarefa específica, pode ou não retornar um valor como por exemplo usar o print varias vezes
def linha():
    print(50*'-')

    linha()
    print('sistema de alunos')
    linha()


    '-----------------------'

    def titulo(msg):
        print(30*'-')
        print(msg)
        print(30*'-')

        '-----------------------'

        def soma(a, b):
            print(f'A = {a} e B = {b}')
            s = a + b
            print(f'A + B = {s}')
            soma(4, 5)

            print('-----------------------')

            def contador(* num):
                print(num)
                for valor in num:
                    print(f'{valor} ', end='')
                
                contador(2, 1, 7)
                contador(8, 0)
                contador(4, 4,7,6,2)
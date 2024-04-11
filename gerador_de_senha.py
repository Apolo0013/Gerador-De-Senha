from time import sleep
from fucional import *


# Programa principal
linha(2)
print('\033[1;34mGerador De Senha\033[m'.center(55))
linha(2)

#o while vai repetir isso tudo, quando ele chega no final o programa vai pergunta se o usario deseja repetir

while True:
    # Menu de escolha disponivel para o usuario.
    print('\033[1;33mEscolha')
    sleep(0.5)
    print('[1] - Numeros e Letras') # exbir a senha com numeros e letras juntos.
    sleep(0.5)
    print('[2] - Simbolos e Letras') # exbir a senha com simbolos e letras.
    sleep(0.5)
    print('[3] - Numeros e Simbolos') # exbir a senha com numeros e simbolos.
    sleep(0.5)
    print('[4] - Letras') # exbir a Senha com letra maiuculas e miniculas.
    sleep(0.5)
    print('[5] - Numeros')  # exbir a senha com numeros de 1 a 9.
    sleep(0.5)
    print('[6] - Simbolos') # exbir a senha com simbolos.
    sleep(0.5)
    print('[7] - Todas as opções. ') # irar exbir todas as senha anteriores.
    sleep(0.5)
    print('[8] - Cancelar Programa.\033[m') # cancelar o programa.
    print('\033[1;36m▃\033[m'*50)
    #o op(opcao) sera de 1 ate 6, seis opcoes
    op = int(input('\033[1;33mEscolha:\033[m '))
    if op == 8:
        print('\033[1;36m▃\033[m'*50)
        break
    print('\033[1;36m▃\033[m'*50)
    # Nessa opcao vai pedir ao usuario o tamanho da senha. Lembrando que so aceitar numeros pares.
    while True:
        print('\033[1;31mAPENAS NUMEROS PARES*\033[m')
        v = int(input('\033[1;32mQUAL SERIA O TAMANHO DA SENHA?:\033[m '))
        if v % 2 == 0:
            break
    
    numpar = (v%2)
    c = int(v/2)

    linha(2)
    if numpar == 1 or numpar >= 1:
        print('\033[1;32mprocessando...\033[m')
        linha(2)
        sleep(3)
        print('\033[1;31mNumero não é par!!!\033[m')

    if numpar == 0:
        print('\033[1;32mprocessando...\033[m')
        print('\033[1;36m▃\033[m'*50)
        sleep(3)
        senha(op = op , v = v , c = c)
        sleep(3)
    else:
        print('\033[1;31m*INFORMACÕES QUE VOCÉ FORNECEU AO PROGRAMA, DEU UM ERRO DESCONHECIDO\033[m')
        print('\033[1;31m*TENTE NOVAMENTE E LEIA OQUE ESTA ESCRITO!!!\033[m')
    linha(2)
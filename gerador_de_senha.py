from time import sleep
from fucional import *


# Programa principal
for dig in range(1, 3+1):
    print('\033[1;36m▃\033[m'*50)
print('{:▃^60}'.format(' \033[1;34mGerador De Senha\033[m '))
for dig in range(1, 3+1):
    print('\033[1;36m▃\033m'*50)


#o while vai repetir isso tudo, quando ele chega no final o programa vai pergunta se o usario deseja repetir

while True:
    print('\033[1;33mEscolha')
    sleep(0.3)
    print('[1] - Numeros e Letras')
    sleep(0.3)
    print('[2] - Simbolos e Letras')
    sleep(0.3)
    print('[3] - Numeros e Simbonlos')
    sleep(0.3)
    print('[4] - Letras')
    sleep(0.3)
    print('[5] - Numeros')
    sleep(0.3)
    print('[6] - SIMBOLOS')
    sleep(2)
    print('[7] - Todas as opções. ')
    sleep(0.7)
    print('[8] - PRA CANCELAR O PROGRAMA\033[m')
    print('\033[1;36m▃\033[m'*50)
    #o op(opcao) sera de 1 ate 6, seis opcoes
    op = int(input('\033[1;33mESCOLHA!!!:\033[m '))
    if op == 8:
        print('\033[1;36m▃\033[m'*50)
        break
    print('\033[1;36m▃\033[m'*50)
    # aqui é as opcoes de da quantidade de caracteres anark no caso 4,6,8,10
    while True:
        print('\033[1;31mAPENAS NUMEROS PARES*\033[m')
        v = int(input('\033[1;32mQUAL SERIA O TAMANHO DA SENHA?:\033[m '))
        if v % 2 == 0:
            break
    numpar = (v%2)
    for dig3 in range(1, 3+1):
        print('\033[1;36m▃\033[m'*50)
    c = int(v/2)

    if numpar == 1 or numpar >= 1:
        print('\033[1;32mprocessando...\033[m')
        for dig in range(1,3+1):
            print('\033[1;36m▃\033[m'*50)
        sleep(3)
        print('\033[1;31mNumero não é par!!!\033[m')

    if numpar == 0:
        print('\033[1;32mprocessando...\033[m')
        print('\033[1;36m▃\033[m'*50)
        sleep(3)
        senha(op = op , v = v , c = c)
    else:
        print('\033[1;31m*INFORMACÕES QUE VOCÉ FORNECEU AO PROGRAMA, DEU UM ERRO DESCONHECIDO\033[m')
        print('\033[1;31m*TENTE NOVAMENTE E LEIA OQUE ESTA ESCRITO!!!\033[m')
    for dig5 in range(1,2+1):
        print()
        print('\033[1;36m▃\033[m'*50)
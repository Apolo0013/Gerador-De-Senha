from time import sleep
from random import randint , seed , choice
from string import  punctuation , ascii_lowercase , ascii_uppercase
#from gerador_de_senha import c , v , op


def linha(vezes = 1):
    '''
    --> printa uma linha e repete isso.
    parametro vezes(opcional): vem com padrão 1 vai repetir uma vez, o usuario tem esse poder
    de fala quantas vez, vai se repetir essa linha.
    '''
    for c in range(0,vezes):
        print('\033[1;36m▃\033[m'*50)


def senha(op, c , v):
    '''
    --> essa funcao faz todas as senha.
    parametro op: vai receber a opção de senha do usuario
    paramentro c: esse outra variavel que vai dizer quantas vezes vai se repetir dependedo da opção
    do usuario na variavel v.
    parametro v: vai receber a quantidade de vez que a senha vai se repetir.
    '''
    if op == 1 or op == 7:
        print(end ='' 'Senha: ')
        for c0 in range(1 , c+1):
            seed()
            le = choice(letras)
            n  = randint(1, 9)
            print(end = '' f'{le}')
            print(end = '' f'{n}')
        print()
    sleep(1)
    if op == 2 or op == 7:
        print(end='' 'Senha: ')
        for c1 in range(1 , c+1):
            seed()
            sim = choice(simbolos)
            letra = choice(letras)
            print(end = '' f'{sim}')
            print(end = '' f'{letra}')
        print()
    sleep(1)
    if op == 3 or op == 7:
        print(end = '' 'Senha: ')
        for c2 in range(1 , c+1):
            seed()
            n = randint(1,9)
            sim = choice(simbolos)
            print(end = '' f'{n}')
            print(end = '' f'{sim}')
        print()
        sleep(1)
    if op == 4 or op == 7:
        print(end = '' 'Senha: ')
        for c3 in range(1 , v+1):
            seed()
            letra = choice(letras)
            print(end = '' f'{letra}')
        print()
        sleep(1)
    if op == 5 or op == 7:
        print(end = '' 'Senha: ')
        for c4 in range(1, v+1):
            seed()
            n =  randint(1 , 9)
            print(end = '' f'{n}')
        print()
        sleep(1)
    if op ==  6 or  op == 7:
        print(end = '' 'Senha: ')
        for c5 in range(1 , c+1):
            seed()
            letra = choice(letras)
            sim =  choice(simbolos)
            print(end = '' f'{letra}')
            print(end = '' f'{sim}')
        print()
        sleep(1)
    


letras = ascii_lowercase+ascii_uppercase # letras maiuculas e minucuslas
simbolos = punctuation # uma ruma de simbolos doidão

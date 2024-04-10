from time import sleep
from random import randint , seed , choice
from string import  punctuation , ascii_lowercase , ascii_uppercase
#from gerador_de_senha import c , v , op


def senha(op, c , v):
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

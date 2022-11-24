from data import ido,nevek
from os import system

fajlnev='data.csv'

def menu():
    system('cls')
    print('----------menü----------')
    print('0 - kilépés')
    print('1 -  Az összes versenyző kiírása')
    print('2 - új versenyző felvétele')
    print('3 - Versenyző törlése')
    print('4 - A leggyorsabb időt futó versenyző')
    print('5 - A leglasabb időt futó versenyző ')
    print('6 - leghosszabb nevű ló')
    return input('Választás: ')

def versenyzok():
    file=open(fajlnev,'r',encoding='utf-8')
    for row in file:
        darabolt=row.strip().split(';')
        print(darabolt)
        nevek.append(darabolt[0])
        ido.append(float(darabolt[1]))
    file.close()

    system('cls')
    print('----------versenyzők----------')
    for i in range(len(nevek)):
        print(f'\t{nevek[i]}')
    input('...')








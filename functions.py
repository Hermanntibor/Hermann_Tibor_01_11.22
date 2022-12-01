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
    nevek.clear()
    ido.clear()
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

def ujversenyzo():
    file=open(fajlnev,'r',encoding='utf-8')
    for row in file:
        darabolt=row.strip().split(';')
        print(darabolt)
        nevek.append(darabolt[0])
        ido.append(float(darabolt[1]))
    file.close()

    system('cls')
    print('Új autó')
    nevek.append(input('versenyző neve: '))
    ido.append(input('idő: '))
    eredmenymentes(nevek[len(nevek)-1],ido[len(ido)-1])
    input('versenyző felvétele. Tovább (Enter)...')

def eredmenymentes(nev,ido):
    file=open(fajlnev,'a',encoding='utf-8')
    file.write(f'\n{nev};{ido}')
    file.close()

def versenyzotorlese():
    file=open(fajlnev,'r',encoding='utf-8')
    for row in file:
        darabolt=row.strip().split(';')
        print(darabolt)
        nevek.append(darabolt[0])
        ido.append(darabolt[1])
    file.close()

    system('cls')
    print('----------eredmény-törlése----------')
    versenyzok
    sSz=int(input('\nKit töröljünk?: '))
    nevek.pop(sSz-1)
    ido.pop(sSz-1)
    input('sikeres törlés.')
    mentesfajlba()

def mentesfajlba():
    file=open(fajlnev,'w',encoding='utf-8')
    for i in range(len(nevek)):
        if i>0:
            file.write('\n')
        file.write(f'{nevek[i]};{ido[i]}')
    file.close()


def leggyorsabb():
    minpoz=0
    for i in range(len(ido)):
        if ido[i]<ido[minpoz]:
            minpoz=i
    print(minpoz)
    print("A leggyorsabb versenyző(k):")
    for i in range(len(ido)):
        if int(ido[i])==minpoz:
            print(f"{nevek[i]} {ido[i]}")
    input('...')









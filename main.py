from functions import menu, versenyzok
from os import system



valasztas =""
while valasztas !='0':
    valasztas = menu()
    if valasztas=='1':
        versenyzok()
    
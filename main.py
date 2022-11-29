from functions import *
from os import system



valasztas =""
while valasztas !='0':
    valasztas = menu()
    if valasztas=='1':
        versenyzok()
    elif valasztas=='2':
        ujversenyzo()
    elif valasztas=='3':
        versenyzotorlese()
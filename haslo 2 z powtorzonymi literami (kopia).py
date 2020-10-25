

import os
import time
import datetime

d = ["""
   ________
   |    |
   |    |
   |    O
   |   /|\\
   |   / \\
   |
   |
   |
======="""
    ,
     """
   ________
   |    |
   |    |
   |    O
   |   /|\\
   |   /
   |
   |
   |
======="""
    ,
     """
   ________
   |    |
   |    |
   |    O
   |   /|\\
   |
   |
   |
   |
======="""
    ,
     """
   ________
   |    |
   |    |
   |    O
   |   /|
   |
   |
   |
   |
======="""
    ,
     """
   ________
   |    |
   |    |
   |    O
   |    |
   |
   |
   |
   |
======="""
    ,
     """
   ________
   |    |
   |    |
   |    O
   |
   |
   |
   |
   |
======="""
    ,
     """________
   |    |
   |    |
   |
   |
   |
   |
   |
   |
======="""
    ,
     """ ________
   |     |
   |
   |
   |
   |
   |
   |
   |
======="""
    ,
     """
   ________
   |
   |
   |
   |
   |
   |
   |
   |
=======
"""
     ]
lis = []
def zapisywanie(x):
    global runda
    file = open("historia.txt", "a")
    file.write(f"runda nr: {runda} \n")
    file.write(x)
    file.write("\n\n")
    file.close()
    runda = runda + 1


def funkcja(x, y):
    global wynik_gracz1
    global wynik_gracz2
    haslo = input(f"{x} podaj haslo i pamiętaj {y} nie widział/a ")
    s = list(haslo)
    os.system("cls")
    szansa = 8
    w = []

    for g in s:
        if g != ' ':
            w.extend('_')
        else:
            w.extend(' ')

    lis = []

    while s != w:

        for i in w:
            print(i, end=" ")
        print()

        if (len(set(lis)) != 0):
            print("literi które użyłeś: ", set(lis))
        odp = input("  Podaj literkę: ")

        while (len(odp) != 1):
            odp = input("Złe dane - podaj JEDNĄ literkę: ")
        os.system("cls")

        if odp in s:
            a = 0
            for l in s:
                if l in odp:
                    w[a] = odp
                    os.system("cls")
                    print("Zostało: %d szans" % szansa)
                    print(d[szansa])
                a = a + 1

        else:
            os.system("cls")
            print("Tej literki nie ma w haśle. Zostało: %d szans" % szansa)
            lis.append(odp)
            print(d[szansa])
            szansa = szansa - 1

        if szansa == -1:
            print("przegrałeś spróbujj jeszcze raz")
            wynik_gracz1 = wynik_gracz1 + 1
        else:
            if s == w:
                print("Wygrałeś hasło to \t>>", haslo, "<<")
                wynik_gracz2 = wynik_gracz2 + 1


# koniec funkccji
runda = 1
wynik_gracz1 = 0
wynik_gracz2 = 0
odpowiedz = input("czy chcesz zagrać wpisz - 'tak' lub 'nie' ")
os.system("cls")

while odpowiedz != "tak" and odpowiedz != "nie":
    odpowiedz = input("złe dane wejsciowe - wpisz 'tak' lub 'nie' ")
    os.system("cls")

if odpowiedz == "tak":
    gracz1 = input("podaj nick gracza 1")
    gracz2 = input("podaj nick gracza 2")
    os.system("cls")

    while odpowiedz == "tak":

        #if odpowiedz == "tak":
        funkcja(gracz1,gracz2)
        date = datetime.datetime.now()
        print(f"data: {date}\n\twyniki:\n\t\t{gracz1} : {wynik_gracz1}\n\t\t{gracz2} : {wynik_gracz2}")
        zapisywanie(f"\tdata: {date}\n\t\twyniki:\n\t\t\t{gracz1} : {wynik_gracz1}\n\t\t\t{gracz2} : {wynik_gracz2}")

        odpowiedz = input("czy dalej chcesz grać - odpowiedz 'tak' lub 'nie' ?")
        os.system("cls")

        while odpowiedz != "tak" and odpowiedz != "nie":
            odpowiedz = input("złe dane wejsciowe - wpisz 'tak' lub 'nie' ")
            os.system("cls")

        if odpowiedz == "nie":
           print("zapraszamy innym razem")
           time.sleep(3)

else:
    print("zapraszamy innym razem")
    time.sleep(3)

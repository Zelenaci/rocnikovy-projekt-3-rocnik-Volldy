win = False
pole = []


def setup():                                          #udělá mi to pole
    global pole
    spatne = True
    while spatne:                                     #když napíšu blbost tak mi to řekne "POČET - musí být číslo, pokud ti to neni jasny"
        try:
            pocet = int(input("Počet disků:"))
            for i in range(0, pocet):                 #přidá počet x pole
                pole.append([0, 0, 0])                #3 sloupce automaticky
                I = 1                                 #vždycky do 1sloupce se zapíše od 1 do počtu
                for a in pole:
                    a[0] = I
                    I += 1
                spatne = False
        except:
            print("POČET - musí být číslo, pokud ti to neni jasny")


def tah():                                            #vezme si pole přesune pole disk ze stratu do cíle pokud je to možné
    global pole
    pohyb = input("-->").split()
    try:                                              #když napíšu blbost tak aby nenastala chyba
        start = int(pohyb[0]) - 1
        cil = int(pohyb[1]) - 1
    except:
        start = 5
        cil = 5
    moznosti = (0, 1, 2)
    if start in moznosti and cil in moznosti:         #když napíšu jiné číslo než je možné, tak se neprovede tah
        for y in range(0, len(pole)):                 #vezme první nejvhodnější disk ze sloupce start
            if pole[y][start] == 0:
                pass
            else:
                zapis = pole[y][start]
                pozice = y
                break

        for y in range(0, len(pole)):                 #provede tah pokud je to možné
            if pole[y][cil] == 0:
                pass
            else:
                if pole[y][cil] > zapis:
                    pole[pozice][start] = 0
                    pole[y - 1][cil] = zapis
                    break
                else:
                    print("nelze položit větší na menší")
                    break

        else:                                         #pokud ve sloupci není nic tak to položí na dno sloupce
            pole[len(pole) - 1][cil] = zapis
            pole[pozice][start] = 0
    else:
        print("Pouze:1,2,3!")


while True:                                           #hlavní herní smyčka
    setup()

    while not win:
        for a in range(0, len(pole)):
            print(pole[a])
        tah()
        if pole[0][2] == 1:
            win = True

    print("Vyhrál jsi!")

    if input("Hrát znovu[A/N]?:") == "N" or input("Hrát znovu[A/N]?:") == "n":
        quit()
#Zrobimy program do szyfrowania
#Funkcja szyfrowanie, deszyfrowanie i jakieś menu


# funkcja szyfrująca tekst
def szyfrowanie(tekst):
    for i in range(len(tekst)):
        if (tekst[i] == "a"):
            tekst[i] = "y"
        elif (tekst[i] == "e"):
            tekst[i] = "i"
        elif (tekst[i] == "i"):
            tekst[i] = "o"
        elif (tekst[i] == "o"):
            tekst[i] = "a"
        elif (tekst[i] == "y"):
            tekst[i] = "e"

#funkcja deszyfrująca

def deszyfrowanie(tekst):
    for i in range(len(tekst)):
        if (tekst[i] == "y"):
            tekst[i] = "a"
        elif (tekst[i] == "i"):
            tekst[i] = "e"
        elif (tekst[i] == "o"):
            tekst[i] = "i"
        elif (tekst[i] == "a"):
            tekst[i] = "o"
        elif (tekst[i] == "e"):
            tekst[i] = "y"

    tekst = ''.join(tekst)
    return(tekst)

#menu

x = 0
while (x == 0):
    operacja = str(input("Wybierz operacje (szyfrowanie,deszyfrowanie,wyjscie): "))
    if (operacja == "szyfrowanie"):
        tekst = list(str(input("Podaj tekst: ")))
        tekst = szyfrowanie(tekst)
        print(tekst)
    elif (operacja == "deszyfrowanie"):
        tekst = list(str(input("Podaj tekst: ")))
        tekst = deszyfrowanie(tekst)
        print(tekst)
    elif (operacja == "wyjscie"):
        x = 1
    else:
        print("Bledna operacja!")
#działa
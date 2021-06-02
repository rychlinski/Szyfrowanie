#Zrobimy program do szyfrowania
#Funkcja szyfrowanie, deszyfrowanie i jakieś menu

def szyfrowanie(tekst,klucz):

    for i in range(len(tekst)):
        x = ord(tekst[i]) + klucz
        tekst[i] = chr(x)

    # wyświetlenie zaszyfrowanego tekstu
    tekst = ''.join(tekst)
    return(tekst)

def deszyfrowanie (tekst, klucz):
    for i in range(len(tekst)):
        x = ord(tekst[i]) - klucz
        tekst[i] = chr(x)

    tekst = ''.join(tekst)
    return(tekst)

#menu

x = 0
while (x == 0):
    operacja = str(input("Wybierz operacje (1,2 lub 3): \n 1.Szyfrowanie \n 2.Deszyfrowanie \n 3.Wyjście \n Wybierz: "))
    if (operacja == "1"):
        klucz = int(input("Podaj klucz od 1 do 10: "))
        tekst = list(str(input("Podaj tekst: ")))
        tekst = szyfrowanie(tekst,klucz)
        print(tekst)
    elif (operacja == "2"):
        klucz = int(input("Podaj klucz od 1 do 10: "))
        tekst = list(str(input("Podaj tekst: ")))
        tekst = deszyfrowanie(tekst,klucz)
        print(tekst)
    elif (operacja == "3"):
        x = 1
    else:
        print("Bledna operacja!")
#działa
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
#wiktoria zrób deszyfrowanie
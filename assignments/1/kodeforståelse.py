x = 5
y = 8

def main ():
    # Redefinerer variablene i vårt lokale scope. I denne funksjonen er det altså disse definisjonene som nå gjelder.
    x = 7
    y = 3

    # Vil nå printe ut 7 og 3, da dette er hva variablene er redefinert som i funksjonen main
    print ("i main :", x, y)

    # Bruker et Python-triks for å bytte om de to variablene.
    # I den samme funksjonen printer vi også ut de to variablene. De to variablene blir kun swappet lokalt i
    # swap-scopet. Printer 3 og 7.
    swap(x, y)

    # De to variablene er fortsatt definert som 7 og 3.
    print ("i main :", x, y)

    # Funksjonen printglobals har fortsatt den gamle/globale definisjonen av x og y, så dette printer ut 5 og 8
    printglobals ()

    # Til slutt printer vi ut de lokalt definerte variablene igjen, som fortsatt er 7 og 3.
    print ("i main :", x, y)

def swap (x, y):
    x,y = y,x # Python triks for å bytte om to variabler .
    print (" ---> i swap :", x, y)

def printglobals ():
    print (" ---> i printglobals :", x, y)

main ()

import math

def main():
    # Informer brukeren om programmet og spør om sidelengde.
    print("Dette programmet finner overflatearealet og volumet til et regulært tetraeder gitt sidelengden.")
    sidelengde = float(input("Sidelengde: "))

    # Formler for å regne ut overflateareal og volum.
    a = 3 / math.sqrt(6) * sidelengde
    overflateAreal = math.sqrt(3)* math.pow(a, 2)
    volum = 1 / 12 * math.sqrt(2) * math.pow(a, 3)

    # Skriv ut resultatet til brukeren
    print("Overflateareal: ", overflateAreal)
    print("Volum: ", volum)

if __name__ == "__main__":
    main()

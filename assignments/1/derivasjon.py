import math

def main():
    print("Skriv inn en x-verdi og en h-verdi for å få en tilnærming av den deriverte til sin(x).")
    x = float(input("x: "))
    h = float(input("h: ")) # må manuelt skrive 0.001, kan ikke bruke ^ eller **

    # Tilnærm den deriverte vha definisjonen av den deriverte.
    f1 = math.sin(x)
    f2 = math.sin(x + h)
    approx = (f2 - f1) / h

    print("Tilnærming: {0:.2f}".format(approx))

if __name__ == "__main__":
    main()

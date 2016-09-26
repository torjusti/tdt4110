def main():
    a = float(input("Skriv inn et tall: "))
    b = float(input("Skriv inn enda et tall: "))

    if a == b and a in (0, 2):
        print("Begge tall lik 0 eller 2 gir at a * b = a + b")
    elif a * b < (a + b):
        print("a * b =", a*b, "er minst av a * b og a + b")
    else:
        print("a + b =", a+b, "er minst av a * b og a + b")

    forslag = int(input("Hva er 3*4? Svar: "))
    if forslag == (3 * 4):
        print("Stemmer bra")
    else:
        print("Stemmer ikke")

if __name__ == "__main__":
    main()

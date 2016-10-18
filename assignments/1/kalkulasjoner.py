def main():
    # lag et program som skriver hello world til konsoll
    print("hello world")
    # utvid slik at det også tar inn to tall og returnerer sunmmen
    print("Skriv inn to tall og få summen.")
    sumTall1 = input("Tall 1:")
    sumTall2 = input("Tall 2:")
    print("Summen av de to tallene er", sumTall1 + sumTall2)
    # utvid slik at programmet også returnerer modulo av to tall
    print("Skriv inn to tall og få modulo av de to tallene.")
    modTall1 = input("Tall 1:")
    modTall2 = input("Tall 2:")
    print("Modulo av de to tallene er" % modTall1 % modTall2)

if __name__ == "__main__":
    main()

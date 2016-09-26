from math import pow

def main():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    d = pow(b, 2)-4*a*c

    defString = "Andregradsligningen " + str(a) + "x^2+" + str(b) + "x+" + str(c) + " har "

    if d < 0:
        print(defString + "to imaginære løsninger")
    elif d > 0:
        print(defString + "to reelle løsninger")
    elif d == 0:
        print(defString + "en reell dobbelrot")


if __name__ == "__main__":
    main()

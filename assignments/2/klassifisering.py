def wholeNumber(num):
    if num == int(num):
        return 1
    return 0

def evenNumber(num):
    return not (num % 2)

def isPositive(num):
    return num > 0

def compareNr(a, b):
    return not bool(a - b)

def main():
    num = float(input("Number: "))

    if wholeNumber(num):
        print("Dette er et heltall.")
    else:
        print("Dette er ikke et heltall")

    if evenNumber(num):
        print("Dette er et partall.")
    else:
        print("Dette er ikke et partall.")

    if isPositive(num):
        print("Dette er et positivt tall.")
    else:
        print("Dette er et negativt tall.")

    a = float(input("a: "))
    b = float(input("b: "))

    if compareNr(a, b):
        print("The numbers are equal")
    else:
        print("The numbers are not equal")

if __name__ == "__main__":
    main()

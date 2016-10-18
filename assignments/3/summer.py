import math

def main():
    iterations = int(input("Skriv inn antall iterasjoner:"))

    res = 0

    for i in range(1, iterations + 1):
        res += 1 / math.pow(i, 2)

    print("Etter", iterations, "iterasjoner ble summen", round(res, 2))

    treshold = float(input("Skriv inn ønsket toleranseverdi:"))

    i = 0
    prev = 0
    res = 0

    while True:
        i += 1
        res += 1 / math.pow(i, 2)
        diff = abs(prev - res)
        prev = res

        if diff <= treshold:
            break

    print("Med toleranseverdi", treshold, "ble summen", round(res, 2))

main()

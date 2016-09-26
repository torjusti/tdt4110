def main():
    pointsInput = input("Skriv inn din poengsum: ")
    pointsFloat = float(pointsInput)
    points = int(pointsFloat)

    if points != pointsFloat:
        print("Poengsummen må være et heltall")
    elif points > 100 or points < 0:
        print("Poengsummen må våre innenfor [0, 100]")
    elif points > 88:
        print("Du fikk A")
    elif points > 76:
        print("Du fikk B")
    elif points > 64:
        print("Du fikk C")
    elif points > 52:
        print("Du fikk D")
    elif points > 40:
        print("Du fikk E")
    else:
        print("Du fikk F")

if __name__ == "__main__":
    main()

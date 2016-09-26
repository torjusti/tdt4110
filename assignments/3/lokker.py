def main():
    print("1-5 for loop")
    for a in range(1, 6):
        print(a)

    print("1-5 while loop")
    b = 1
    while b <= 5:
        print(b)
        b += 1

    print("15-1 for loop")
    for c in range(15, 0, -1):
        print(c)

    print("15-1 while loop")
    d = 15
    while d >= 1:
        print(d)
        d -= 1

if __name__ == "__main__":
    main()

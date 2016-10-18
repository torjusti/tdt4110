def main():
    n = int(input("n: "))

    x = 0
    y = 1
    totalSum = 0
    i = 0

    while i < n:
        print(x)
        i += 1
        totalSum += x
        x, y = y, x + y

        # xOld = x
        # x = y
        # y = xOld + y


    print("sum:", totalSum)

if __name__ == "__main__":
    main()

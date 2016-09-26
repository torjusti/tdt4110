def main():
    n = int(input("n: "))

    x = 0
    y = 1
    s = 0
    i = 0

    while i < n:
        print(x)
        i += 1
        s += x
        x, y = y, x + y

    print("sum:", s)
    
if __name__ == "__main__":
    main()

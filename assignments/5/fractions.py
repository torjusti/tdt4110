def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def reduceFraction(a, b):
    factor = gcd(a, b)
    return (a / factor), (b / factor)

def main():
    while True:
        a = int(input('a:'))
        b = int(input('b:'))
        teller, nevner = reduceFraction(a, b)
        print(teller, '/', nevner, sep='')

main()

import math

def f(x):
    # Finn ut: Bør man bruke funksjonen eller dobbelt stjernetegn.
    return (x - 12) * math.exp(5 * x) - 8 * math.pow(x + 2, 2)

def g(x):
    return -x - 2*x**2 - 5*x**3 + 6*x**4

def derivate(h, x, func):
    return (func(x + h / 2) - f(x - h / 2)) / h

def newtons_method(h, x, func, tol):
    prev = x + tol
    while abs(prev - x) >= tol:
        prev = x
        x -= func(x) / derivate(h, x, func)
    return x

def printmsg(h, x, func, tol):
    approximation = newtons_method(h, x, func, tol)
    print('funksjonen nærmer seg et nullpunkt når x =', approximation, 'da er y =', func(approximation))

printmsg(0.00000001,-2,f,0.0000000001)
printmsg(0.00000001,1,g,0.0000000001)
printmsg(0.00001,-1,g,0.00001)

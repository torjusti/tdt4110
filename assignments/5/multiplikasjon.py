def produkt(tol):
    previous = 0
    approximation = 1
    i = 1

    while abs(previous - approximation) >= tol:
        previous = approximation
        approximation *= 1 + 1 / i**2
        i += 1

    return approximation, i

approx, level = produkt(0.01)

print("approx:", round(approx, 2), "level:", level)

def product_recursive(tol, previous=1, level=1):
    approximation = previous * (1 + 1 / level**2)
    if abs(previous - approximation) >= tol:
        return product_recursive(tol, approximation, level + 1)
    else:
        return approximation, level

approx, level = product_recursive(0.01)

print("approx:", round(approx, 2), "level:", level)

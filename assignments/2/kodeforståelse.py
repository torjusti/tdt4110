# 1: Variabler

# 2: Oppdatert versjon under.
# Feil med apostrof i funksjon
#
# Syntaksfeil - unexpected indent

x = 2
y = int(input("Skriv inn et tall: "))
z = x // y
print(z)


# definerer variabler
# sjekker om b er mindre enn a, det er den ikke
# 2%3 = 1, 1 er truth-aktig => not 1 => false, så vi går videre til false
# a = a*b, printer dermed 3 og 6
a = 2
b = 3
if (b<a or not b%a):
    b = a+b
else:
    a = a*b
print("a: ",a)
print("b: ",b)

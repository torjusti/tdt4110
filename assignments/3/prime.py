n = 100

# Loop through all numbers [2, n]
for i in range(2, n + 1):
    prime = True

    # Check if the number is divisible by any number except 1 and itself
    for j in range(2, i):
        if i % j == 0:
            prime = False
            break

    if prime:
        print(i)

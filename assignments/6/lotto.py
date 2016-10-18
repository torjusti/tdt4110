import random

# Ikke ferdig

numbers = list(range(1, 35))

myGuess = [1, 2, 3, 4, 5, 6, 7]

def take_n(n):
    return [numbers.pop(random.randint(0, len(numbers) - 1)) for i in range(n)]

def compList(a, b):
    return sum(1 for i in a if i in b)

def calc_prize(tall, tillegstall):
    return 'todo'

print(take_n(10))

print(compList([1,2,3],[1,5,6]))

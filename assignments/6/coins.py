import math

def count_coins(coins): return sum(coins)

def num_coins(numbers):
    res = [] # resultat-liste
    for num in numbers: # loop gjennom alle tall
        arr = [] # liste med mynter i dette tallet
        for curCoin in [20, 10, 5, 1]: # loop gjennom alle typer mynt
            coinCount = math.floor(num / curCoin) # antallet ganger denne mynten går opp i tallet
            num -= coinCount * curCoin # finn rest
            arr.append(coinCount) # legg til i liste med mynter i dette tallet
        res.append(arr) # legg til i rest-array
    return res # return resultat

def check_weight(lst):
    weights = { 20: 9.9, 10: 6.8, 5: 7.85, 1: 4.35 } # dict med mynt-vekter :D
    return sum(weights[num] for num in lst) # summer en liste som nå inneholder vekten til hver mynt

print(count_coins([1,1,5,10,20]))
print(num_coins([63,55]))
print(check_weight([20,10,5,1]))

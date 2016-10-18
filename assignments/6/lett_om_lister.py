# return true hvis det første eller siste tallet i lista er 6
def isSixAtEdge(lst):
    # kan også bruke lst[len(lst) - 1]
    return lst[0] == 6 or lst[-1] == 6

print(isSixAtEdge([0,5,3,6]))

# returner gjennomsnittet av en liste
def average(lst):
    return sum(lst) / len(lst)

print(average([1,2,3]))

# finn median til en liste
def median(lst):
    # sorter lista, finn verdien i midten. midten er floor(index / 2)
    return sorted(lst)[len(lst) // 2]

print(median([1,2,3,4,5]))

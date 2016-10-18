import numpy as np

def allUnique(lst): return len(set(lst)) == len(lst)
def removeDuplicates(lst): return list(set(lst))
def inAbutnotB(a, b): return list(set(a) - set(b))
def areOrthagonal(a, b): return np.dot(np.array(a), np.array(b)) == 0

print(allUnique([1,2,3]))
print(removeDuplicates([1,2,2]))
print(inAbutnotB([1,2],[1,1]))
print(areOrthagonal([1,-1,0],[2,2,3]))

# Forstår ikke B, men oppgaven er valgfri.

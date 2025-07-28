# create a list to store only the prime numbers from 1 to 100 using the comprehention
'''def prime(n):
      return [x for x in range(2, n + 1) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]

print(prime(100))
'''

# set comprehention create a list given in set comprehention {('A',1), ('A',2), ('A',3), ('B',1), ('B',2), ('B',3)} IN SIMPLE WAY
'''def set():
      return {(i, j) for i in ['A', 'B'] for j in range(1, 4)}
print(set())
'''

# DICTIONARY COMPREHENTION
# ZIP FUNCTION: ZIP() IT IS USED TO ITERATE BETWEEN MULTIPLE FUNCTIONS SYMLTANIOUSLY
# SYNTAX: {KEY: VALUE for KEY, VALUE in zip(KEYS, VALUES())}

'''l1 = [1,2,3,4,5]
l2 = ['a','b','c','d','e']

d = {i:j for i,j in zip(l1,l2)}
print(d)
'''

# store all the combination of 0 and 1 as three values (i,j,k) only if thire sum is != 3
def combi():
      return {(i, j, k) for i in range(2) for j in range(2) for k in range(2) if i + j + k != 3}
print(combi())

var = [(i,j,k) for i in range(0,2) for j in range(0,2) for k in range(0,2) if i + j + k != 3]
print(var)    
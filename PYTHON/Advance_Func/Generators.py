# Generators - A generator is a special type of iterator that is defined using a function and the 'yield' keyword.
# They allow you to iterate over a sequence of values without storing the entire sequence in memory.
# This makes them more memory-efficient for large datasets.
#counter make a list of numbers 1 to 10 using the generator function
'''def counter():
      for i in range(1, 11):
            yield i
for num in counter():
    print(num)
'''    
# Example of a generator function that yields countdown numbers
'''def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(10):
    print(i)
'''

l = [1,2,3,4,5,6,7,8,9,0,3,4,2,555,6,33,12,987]

def unique(l):
      for i in l:
            count = 0
            for j in l:
                  if i == j:
                        count += 1
            if count == 1:
                  yield i

print(list(unique(l)))

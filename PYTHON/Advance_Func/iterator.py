# Iterator - An iterator is an object that implement the iterator protocol, which consists of the methods __iter__() and __next__().
# Example of an iterator class that returns unique elements from a list
# This allows you to traverse through all the elements in a collection without needing to know the underlying structure.
# will able to trace back to the previous element - using a stack
# iter - it is used to fetch the address of the first node in the given collection or linked list.
# next - it is used to fetch the value where the control is pointing towards the address of the node and point towards the address of next node.

# NOTE - WE WILL KEEP ON FETCHING THE VALUES UNTIL WE GET AN ERROR MESSAGE AS "STOP ITERATION"

'''l = [1,2,3,4,5,6,7,8,9,0]

first = iter(l)
print(next(first))
print(next(first))
print(next(first))
print(next(first))
print(next(first))
print(next(first))
print(next(first))
print(next(first))
print(next(first))
print(next(first))
'''

# Example of the iteration protocol using a custom iteration class
'''l = [1,2,3,4,5,6]
it = iter(l)
while True:
    try:
        print(next(it))
    except StopIteration:
        break
'''


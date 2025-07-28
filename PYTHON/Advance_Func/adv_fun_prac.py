#write a program to chech the given number is palindrome or not if yess then print palindrom or else print is not palindrome using the lambda function 
'''var = lambda n: str(n) == str(n)[::-1]
print("palindrome" if var(121) else "not palindrome")'''

#write a program to chech the given string is palindrome or not if yess then print palindrom or else print is not palindrome using the lambda function 
'''var = lambda s: s == s[::-1]
print("palindrome" if var("racecar") else "not palindrome")

pal = lambda s:"palindrome" if s == s[::-1] else "not plalindrome"
print(pal("madam"))'''

# write a prongrame to check the given number is divsible by 5 is yes the add 15 else substract 10 using the lambda function
'''var = lambda n: n + 15 if n% 5 == 0 else n - 10
print(var(10))
print(var(12))'''

# writw a program to return the concatinate list if both has same lenth else return the first list using the lambda functions
'''def list(l1, l2):
      return (lambda l1, l2: l1 + l2 if len(l1) == len(l2) else l1)(l1,l2)
print(list([1,2,3,4,5], [6,7,8,9,0]))
print(list([5,4,3,2,1], [0,9,8,7,6,4])) '''

# write a program to print the cube if the numbers in given list using the map function take given list as a keys and values will be the cube of the keys
'''def cube(l):
      return (lambda l: dict(map(lambda i: (i, i**3), l)))(l)
print(cube(range(1,7)))'''

# print(dict(list(map(lambda i: (i, i**3), range(1,7)))))

# write the program to filter the prime numbers from the given range(1,500) using the filter function
'''def prime(n):
      return (lambda n: list(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)), range(2, n + 1))))(n)
print(prime(500))'''

'''def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

num = range(1, 501)
primeno = list(filter(prime, num))

print("Prime numbers from 1 to 500:")
print(primeno)'''

# write the program to ['hey', 'hello', 'python', 'programming'] to in the form of the dictionary like{'hey:'yeh', 'hello': 'olleh', 'python': 'nohtyp', 'programming': 'gnimmargorp'} using the map function
'''def reverse(l):
    return (lambda l: dict(map(lambda s: (s, s[::-1]), l)))(l)

print(reverse(['hey', 'hello', 'python', 'programming']))
'''

# write the program to ['hey', 'hello', 'python', 'programming'] to in the form of the dictionary like{'hey:'yeh', 'hello': 'olleh', 'python': 'nohtyp', 'programming': 'gnimmargorp'} using the map function
'''def reverse(l):
    return dict(map(lambda s: (s, s[::-1]), l))
print(reverse(['hey', 'hello', 'python', 'programming']))
'''
# wirte a program (1,1.2,'hi',4+5j,'hello',True,'False','Python') filter the strings and return the list of strings using the filter function
'''def string(l):
    return list(filter(lambda x: isinstance(x, str), l))
print(string((1,1.2,'hi',4+5j,'hello',True,'False','Python')))
'''

# wirte a program (1,1.2,'hi',4+5j,'hello',True,'False','Python') filter the strings and return the list of strings using the filter function
def string(l):
    return [r for r in l if type(r) == str]
print(string((1,1.2,'hi',4+5j,'hello',True,'False','Python')))


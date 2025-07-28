# lambada - anonymous function
'''even = lambda n : n%2 == 0
print(f'The given number is even {even(5)}')

odd = lambda n : n%2 != 0
print(f'The given number is odd {odd(4)}')

# write a program to find the square of the given number
sqr = lambda n : n*n
print(sqr(5))
'''

# write a following programs in lambada functions
# 1. check the number is integer or not 
'''integer = lambda x: type(x) == int

print(integer(5))
print(integer(5.5))
print(integer("I'm still in lecture "))
'''
# 2. age is valid or not to voting
'''a = lambda age: age >= 18
print(a(20))
print(a(16))
'''
# 3. convert the sentaence in upper case and lowercase
'''upper = lambda s: s.upper()
lower = lambda s: s.lower()

s = "Yee KYa Bolti TU"
print(upper(s))
print(lower(s))
'''


# even number 
l = [2, 3, 4, 5]
def even(n, i=2):
    return n % 2 == 0

even_num = filter(even, l)
print(list(even_num))

# create prime number function 
l = [2,3,4,5]
def prime(n, i=2):
      if i == n:
            return True
      if n % i == 0:
            return False
      return prime(n, i+1)

prime_num = filter(prime,l)
print(list(prime_num))

'''def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(prime(7))
print(prime(12))'''

# # create strong number function 
'''def strong(n):
    fact = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        fact += factorial(digit)
        temp //= 10
    return fact == n

print("Is 145 a strong number?", strong(145))
print("Is 123 a strong number?", strong(123))'''

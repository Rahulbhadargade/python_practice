# write a program to return only palindrom strings in a given string 
'''def palindromes(s):
    string = s.split()
    return [w for w in string if w == w[::-1] and len(w) > 1]

s = "My mom dad are soo cool"
print(palindromes(s))'''

'''s = "My mom dad are soo cool"
def palindrom(s):
    w = s.split()
    for word in w:
        if word == word[::-1] and len(word) > 1:
            print(word)
palindrom(s)'''

#write a program to validate password using functions 
'''password = input("Enter your password: ")
def validate(pw):
      upper, lower,number,symbol = 0,0,0,0
      if len(pw) >= 8:
            for i in pw:
                  if i in '0123456789':
                        number += 1
                  elif 'A'<= i <= 'Z':
                        upper += 1
                  elif 'a'<= i <= 'z':
                        lower += 1
                  else:
                        symbol += 1
      if upper >= 1 and lower >= 1 and number >= 1 and symbol >= 1:
            return "Password is valid"
      else:
            return "Password is invalid"

print(validate(password))'''

#write a program to find a prime numbers 
'''def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input("Enter a number: "))

if prime(n):
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")'''

'''def prime(n):
   
for i in range(2,n)
    	if n%i == 0:
        	return False
    return True'''
    
# CALCULATOR 
'''def Calculator():
    def add(a,b):
        return a+b
    
    def sub(a,b):
        return a-b
    
    def mul(a,b):
        return a*b
    
    def div(a,b):
        return a/b
    
    def mod(a,b):
        return a%b
    
    # for sqrt
    def vals():
        a = int(input('a: '))
        b = int(input('b: '))
        return a,b
    
    while True:
        print(''Welcome to Calculator
              for add press 1
              for sub press 2
              for mul press 3
              for div press 4
              for mod press 5
              for sqr press 6
              to exit press 0'')
        n =int(input("Enter your choice :"))
        
        if n == 1:
            a,b = vals()
            print(add(a,b))
        elif n == 2:
            a,b = vals()
            print(sub(a,b))
        elif n == 3:
            a,b = vals()
            print(mul(a,b))
        elif n == 4:
            a,b = vals()
            print(div(a,b))
        elif n == 5:
            a,b = vals()
            print(mod(a,b))
        elif n == 0:
            return
        else:
            print("Invalid Input")
Calculator()'''


# type's of the variables ["GLOBLE" AND "LOCAL"]
'''a = 10
b = 20
print(a,b)
def demo():
    # print(a,b)  --- globle variable's
    global a,b
    a = 100
    b = 200
    print(a,b)
print(a,b)
demo()
print(a,b)'''

#write a program to add upto 5 numbers [create a function to add upto 5 numbers]
#This numbers should be add as an example add(10,20,30), add(1,5,8,7,9), add(2,4,6,8)

# with return
'''def add(*args):
    if len(args) > 5:
        return "Error: You can add up to 5 numbers only."
    return sum(args)

print(add(10, 20, 30))       
print(add(1, 5, 8, 7, 9))    
print(add(2, 4, 6, 8))'''      

# without return
'''def add(a=0,b=0,c=0,d=0,e=0):
    print(a+b+c+d+e)
print(add(10, 20, 30))       
print(add(1, 5, 8, 7, 9))    
print(add(2, 4, 6, 8))'''

#write program to store all the marks of the students in the form of dictionary
# math = 10, copm = 80, eng = 94, sci = 75, marathi = 85, kannada = 50 using the dunctions 
'''def store_marks():
    marks = {
        'math': 10,
        'comp': 80,
        'eng': 94,
        'sci': 75,
        'marathi': 85,
        'kannada': 50
    }
    return marks

student_marks = store_marks()


print("Student Marks:")
for subject, mark in student_marks.items():
    print(f"{subject.capitalize()}: {mark}")'''

# write the program to resisteration of facebook using the function
# name, username,email, contact, gender(optional), date of birth (optional), password, confirm password.

'''import sys
sys.setrecursionlimit(5000)
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n *fact(n-1)
print(fact(4991))'''
    

#print the fabonachi series using the recursion
'''def demo(n):
    if n <= 1:
        return n
    return demo(n - 1) + demo(n - 2)

print("Fibonacci Series:")
for i in range(5):
    print(demo(i))'''
    
##print the fabonachi series using the recursion without using the looping
'''def demo(n, a=0, b=1):
    if n == 0:
        return
    print(a, end=' ')
    demo(n - 1, b, a + b)
n = 5
print("Fibonacci Series:")
demo(n)'''

# print the natural till 10 numbers using the recursion
'''def num(n):
    if n > 0:
        num(n - 1)
        print(n, end=' ')
n = 10
print("Natural Numbers:")
num(n)'''

#add two numbers using the recursion taking number in the function
'''def sumofN(n, res = 0):
    if n == 0:
        return n
    return n + sumofN(n-1, res)
print(sumofN(5))'''

# write a program to revers a given number using the recurtion
'''def RN(n, res=0):
    if n == 0:
        return res
    res = res * 10 + n % 10
    return RN(n // 10, res)
n = 1500
print("Reversed Number:", RN(n))'''

# write a program to add all trhe numbers in the given number using the recuresion
'''def sumofd(n):
    if n == 0:
        return 0
    return n % 10 + sumofd(n // 10)
n = 102030405
print("Sum of Digits:", sumofd(n))'''

# write a program to print the characters from given string using recursion...
'''def characters(s, i=0):
    if i == len(s):
        return
    print(s[i], end=' ')
    characters(s, i + 1)

string = "Hello"
print("Characters in the string:")
characters(string)'''

#write a program to reverse a string using the recursion...
'''def R_S(s, i=0):
    if i == len(s):
        return ""
    return R_S(s, i + 1) + s[i]

string = "Hello"
print("Reversed String:")
print(R_S(string))'''

# write a program to print the prime numbers in the given range using the recursion...
'''def p(n, i=2):
    if n <= 1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return p(n, i + 1)
def prime(start, end):
    if start > end:
        return
    if p(start):
        print(start, end=' ')
    prime(start + 1, end)
start = 1
end = 50
print("Prime numbers between", start, "and", end, ":")
prime(start, end)''' 

# wite a program to find the given number is prime or not using the recursion...
def p(n, i=2):
    if n <= 1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return p(n, i + 1)
n = 1
if p(n):
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")
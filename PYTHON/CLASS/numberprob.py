'''a=eval(input('Enter a Number: '))
if type(a)==int:
      print('The given Number is Integer')'''
      
# write a program to check whether the given age is eligible for voting or not
'''a=eval(input('Enter your Age: '))
if a>18:
      print('you are eligible for the voting')
else:
      print('you are not Eligible for the voting')'''

'''if False:
      print('hii')
else:
      print('hello')'''
      
# write a program to check whether the given input is list or not
'''a=eval(input('Enter the list: '))
if type(a)==list:
      print('The given input is list')
else:
      print ('The given input is not list')'''
      
# write a program to check the given input is str or list
'''a=eval(input('Enter the input:'))
if type(a)==str:
      print('the given input is string')
elif type(a)==list:
      print('The given input is a list')
else:
      print('invalid input')'''
      
# write a program to check whether the given number is integer or float or string
'''a=eval(input('Enter the number:'))
if type(a)==int:
      print('The given input is integer')
elif type(a)==float:
      print('The given number is float')
elif type(a)==str:
      print('The given number is string')
else:
      print('Invalid input')'''
      
# write a program to check whether the given number is integer or float or string using aski values
'''a=input('Enter the value:')
if 'A'<=a<='Z':
      print('the given value is uppercase string')
elif 'a'<=a<='z':
      print('the given value is lowercase string')
elif '0'<=a<='9':
      print('the given value is an integer')
else:
      print('the given value is invalid input')'''
      
# write a program to check the entered characters is vowel or not
'''a=input('Enter the character: ')
if a in 'aeiouAEIOU':
    print('The entered character is a vowel')
else:
    print('The entered character is not a vowel')'''
      
# write a program to print the second greatest of 4 numbers
'''a, b, c, d = eval(input('Enter the 4 numbers: '))
if a > b and a > c and a > d:
    greatest = a
elif b > a and b > c and b > d:
    greatest = b
elif c > a and c > b and c > d:
    greatest = c
else:
    greatest = d

if (a > b and a < greatest) or (a < b and a > greatest):
    second_greatest = a
elif (b > a and b < greatest) or (b < a and b > greatest):
    second_greatest = b
elif (c > a and c < greatest) or (c < a and c > greatest):
    second_greatest = c
else:
    second_greatest = d

print('The second greatest number is:', second_greatest)'''

# write a program to print the second greatest of 4 numbers using nested if statements
'''a, b, c, d = 5,2,7,9
if a>b and a>c and a>d:
      if b>c and b>d:
            print('The second greatest number is:', b)
      elif c>b and c>d:
            print('The second greatest number is:', c)
      else:
            print('The second greatest number is:', d)
elif b>a and b>c and b>d:
      if a>c and a>d:
            print('The second greatest number is:', a)
      elif c>a and c>d:
            print('The second greatest number is:', c)
      else:
            print('The second greatest number is:', d)
elif c>a and c>b and c>d:
      if a>b and a>d:
            print('The second greatest number is:', a)
      elif b>a and b>d:
            print('The second greatest number is:', b)
      else:
            print('The second greatest number is:', d)
else:
      if a>b and a>c:
            print('The second greatest number is:', a)
      elif b>a and b>c:
            print('The second greatest number is:', b)
      else:
            print('The second greatest number is:', c)'''

# write a program to print the "hello" for 5 times using while loop
'''i = 1
while i <= 5:
    print('hello')
    i += 1'''

# write the program to print the numbers from 1 to 10 using while loop
'''i = 1
while i <= 10:
    print(i)
    i += 1'''
    
# write the program to print only even numbers from 1 to 20 using while loop
'''i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1'''
    
# write a program to print the odd numbers from 1 to 20 using while loop
'''i = 1
while i <= 20:
    if i % 2 != 0:
        print(i)
    i += 1'''

# write a program to check whether the given number is prime or not using while loop
'''num = int(input('Enter a number: '))
if num > 1:
    i = 2
    while i < num:
        if num % i == 0:
            print('The number is not prime number')
            # break
        i += 1
    else:
        print('The number is prime number')
else:
    print('The number is not prime number')'''

# write a program to check whether the given number is fizz or buzz or fizzbuzz
'''num = int(input('Enter a number: '))
if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
elif num % 3 == 0:
    print('Fizz')
elif num % 5 == 0:
    print('Buzz')
else:
    print("The number is niether a fizz nor a buzz or a FizzBuzz number ")'''
    
# write a program to find the factorial of the given number using while loop
'''num = int(input('Enter a number: '))
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print('The factorial is:', factorial)'''

# print the fabonacci series using while loop till 5 numbers
'''n = int(input('Enter the number of terms: '))
a, b = 0, 1
count = 0
while count < n:
    print(a,end=', ') 
    a, b = b, a + b
    count += 1'''
    
# write program to reverse the given number using while loop
'''num = int(input('Enter a number: '))
rem = 0
while num > 0:
    digit = num % 10
    rem = rem * 10 + digit
    num //= 10
print('The reversed number is:', rem)'''

# to check the given nimber is palindrome or not using while loop
'''num = int(input('Enter a number: '))
rem = 0
while num > 0:
    digit = num % 10
    rem = rem * 10 + digit
    num //= 10
print('The reversed number is:', rem)
if rem == num:
    print('The number is a palindrome')
else:
    print('The number is not a palindrome')'''
    
# sum of all given integer numbers using while loop
'''num = int(input('Enter a number: '))
sum = 0
while num > 0:
    sum += num
    num -= 1
print('The sum of all numbers is:', sum)'''
    
# write a program to find the product of all given numbers using while loop
'''num = int(input('Enter a number: '))
product = 1
while num > 0:
    product *= num
    num -= 1
print('The product of all numbers is:', product)'''

# write a program to find the given number is strong number or not using the while loop
# if sum of the factorial of all the integers in a given number is equal to the number itself then the number is said to be a strong number
'''num = int(input('Enter a number: '))
i = num
sum = 0
while num > 0:
    digit = num % 10
    fact = 1
    while digit > 0:
        fact *= digit
        digit -= 1
    sum += fact
    num //= 10
if sum == i:
    print(sum, 'is a strong number')
else:
    print('The number is not a strong number')'''
    
# write a program to find the amstrong number uwsing while loop
'''num = int(input('Enter a Number: '))
i = num
sum = 0
while num > 0:
    digit = num % 10
    sum += digit ** len(str(i)) # or sum += digit ** 3 for 3 digit numbers
    num //= 10
if sum == i:
    print(i, 'is an Armstrong number')
else:
    print('The number is not an Armstrong number')'''
    
# write a program to find sum of 5 natural numbers using while loop 
'''num = int(input('Enter a number: '))
sum = 0
count = 1
while count <= 5:
    sum += count
    count += 1
print('The sum of first 5 natural numbers is:', sum)'''

# write a program to print the series : 10,20,30, ........ 300
'''i = 10
while i <= 300:
    print(i, end=', ')
    i += 10'''

# write a program to print the series : 105,98,91, ...... 0 
'''i = 105
while i >= 0:
    print(i, end=', ')
    i -= 7'''
    
# write a program to print the divisors of the given number using while loop
'''num = int(input('Enter a number: '))
i = 1
print('The divisors of', num, 'are:')
while i <= num:
   if num % i == 0:
       print(i, end=', ')
   i += 1'''
   
# print the perfect number
'''num = int(input('Enter a number: '))
sum = 0
i = 1
while i < num:
    if num % i == 0:
        sum += i
    i += 1
if sum == num:
    print(num, 'is a perfect number')
else:
    print(num, 'is not a perfect number')
'''
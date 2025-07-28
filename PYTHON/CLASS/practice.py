'''age = 16
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")'''

# swapping two numbers without using third variable
'''a = 5
b = 10
print("Before swapping: a =", a, ", b =", b) 
a = a + b
b = a - b 
a = a - b
print("After swapping: a =", a, ", b =", b)'''

#print 1 to 10 numbers using while loop
'''i = 1
while i <= 10:
    print(i)
    i += 1'''
    
# prints even numbers from 1 to 10 using while loop
'''i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1'''

# print even number from 1 to 10 without using while loop
'''for i in range(1, 11):
      if i % 2 == 0:
            print(i)'''

# print even numbers without using if statement
'''i = 2
print("even number from 1 to 10:")
while i <= 10:
    print(i)
    i += 2'''
    
# print fibonacci series using while loop
'''n = 7
a, b = 0, 1
print("Fibonacci series:")
while a <= n:
     print(a)
     a, b = b, a + b'''

# split and join 
#write a program to remove all wide spaces from the string s=  this is  cognizant    interview 
'''s = "  this is  cognizant   interview"
s = s.replace(" ", "")
print("String without white spaces:", s)'''

s = "  this is  cognizant   interview"
result = ""

for char in s:
    if char != " ":
        result += char

print("String without white spaces:", result)


#take a random list and remove duplicate from it without changing a order of the list dont use inbuilt function

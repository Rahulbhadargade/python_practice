# STRING PROBLEMS
'''s = input("Enter a string: ")
i= 0
while i < len(s):
      print(s[i], end=',')
      i += 1'''
      
# write a program to print only even indexed characters
'''s = input("Enter a string: ")
for i in range(len(s)):
    if i % 2 == 0:
        print(s[i], end=',')'''
        

# write a program to print reverse of the string without using slicing and negative indexing
'''s = input("Enter a string: ")
i = len(s)
while i >= 0:
      i -= 1
      print(s[i], end='')'''

# write a program to fetch only lowercase alphabets from a string
'''s = input("Enter a string: ")
for i in range(len(s)):
    if s[i].islower():
        print(s[i], end=' ')'''
        
'''s = input("Enter a string: ")
i = 0
lower = ''
while i < len(s):
      if ('a'<= s[i]) and (s[i]<='z'):
            lower += s[i]
      i += 1
print(lower)'''

# print a uppercase character without using any inbuilt function
'''s = input("Enter a string: ")
i = 0
while i < len(s):
      if 'A'<= s[i] and s[i] <= 'Z':
            print (s[i], end=' ')
      i += 1'''

# WRITE A PROGRAM TO EXTRACT LOWERCASE CHARACTERS, UPPERCASE CHARACTERS, NUMBERS AND SPECIAL SYMBOLS IN DIFFERENT VARIABLES USING WHILE LOOP
'''s = input("Enter a string: ")
lowercase = ''
uppercase = ''
numbers = ''
special_symbols = ''
i = 0
while i < len(s):
    if ('a'<= s[i]) and (s[i]<='z'):
        lowercase += s[i]
    elif ('A'<= s[i]) and (s[i]<='Z'):
        uppercase += s[i]
    elif ('0'<= s[i]) and (s[i]<='9'):
        numbers += s[i]
    else:
        special_symbols += s[i]
    i += 1
print("Lowercase characters:", lowercase)
print("Uppercase characters:", uppercase)
print("Numbers:", numbers)
print("Special symbols:", special_symbols)'''


# WRITE A SIMPLE PROGRAM TO EXTRACT LOWERCASE CHARACTERS, UPPERCASE CHARACTERS, NUMBERS AND SPECIAL SYMBOLS IN DIFFERENT LIST USING WHILE LOOP 
'''s = input("Enter a string: ")
lowercase = []
uppercase = []
numbers = []
special_symbols = []
i = 0
while i < len(s):
    if ('a'<= s[i]) and (s[i]<='z'):
        lowercase += s[i]
    elif ('A'<= s[i]) and (s[i]<='Z'):
        uppercase += s[i]
    elif ('0'<= s[i]) and (s[i]<='9'):
        numbers += s[i]
    else:
        special_symbols += s[i]

print("Lowercase characters:", lowercase)
print("Uppercase characters:", uppercase)
print("Numbers:", numbers)
print("Special symbols:", special_symbols)'''

# THE "CTRL + C" IS USED TO INTERRUPT THE INFINITE PROGRAM ITS ALSO CALLED AS "KEYBORDINTURPTION"
'''l = [1,2,3,4,5,6,7,8,9]
res = 0
i = 0
while i < len(l):
    res += l[i]
    i += 1
print("The sum of the list is:", res)'''

# write a program to add all the integers in given list using while loop
'''l = [1,4,6.7,2+3j,'hello',5,[10,20,30],4.3,True]
res = 0
i = 0
while i < len(l):
    if type(l[i]) == int:
        res += l[i]
    i += 1
print("The sum of the integers in the list is:", res)'''

# write a program to print the count of the input value in the given list using while loop
'''l = [1,2,3,4,5,6,7,8,9,5,4,2,6,1,4,2,5]
value = eval(input("Enter the value to count: "))
count = 0
i = 0
while i < len(l):
    if l[i] == value:
        count += 1
    i += 1
print("The count of", value, "in the list is:", count)'''

# write a program to store the number along with its count in a dictionary using while loop without using inbuilt functions
'''l = [1,2,3,4,5,6,7,8,9,5,4,2,6,1,4,2,5]
count = {}
i = 0
while i < len(l):
    if l[i] not in count:
        count[l[i]] = 1
    else:
        count[l[i]] += 1
    i += 1
print("The count of each number in the list is:", count)'''

'''l = [1,1,2,1,2]
i = 0
j= 0
res = {}
while i < len(l):
    count = 0
    j = 0
    while j < len(l):
        if l[i] == l[j]:
            count += 1
        j += 1
    res[l[i]] = count
    i += 1'''
    
# WRITE A PROGRAM TO STORE ALL THE STRING IN GIVEN LIST WITH THEIR LENGTH USING NESTED WHILE LOOP
l = ['hi', 'hello', 'hehehe', 'python']
res = {}
i = 0
while i < len(l):
    count = 0
    j = 0
    while j < len(l[i]):
        count += 1
        j += 1
    res[l[i]] = count
    i += 1
print("The length of each string in the list is:", res)
#check the string is palindrome or not
'''s = 'madam'
s1 = s[::-1]
if s == s1:
    print('Given string is palindrome')
else:
    print('Given string is not palindrome')'''
    
#to check the string is palindrome or not without using slicing
'''s = 'madam'
s1 = ''
for i in range(len(s)-1,-1,-1):
    s1 += s[i]
if s == s1:
    print('Given string is palindrome')
else:
    print('Given string is not palindrome')'''
    
#to check the given number is palindrome or not
'''n = 121
n1 = n
s = 0
while n > 0:
      r = n % 10
      s = s * 10 + r
      n = n // 10
if n1 == s:
      print('Given number is palindrome')
else:
      print('Given number is not palindrome')'''
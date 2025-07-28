import re

s1 = ''' Hi, my name is Bla Bla Bla 'rbhadargade@gmail.com', and I'm learning python in qspider 34567890212.
Today is my last day of the 'qspider2003@yahoo.com' Python batch. @9876543210 'jdh.sfjh@gamil.in' www.rb.com.
8/2/2003 Contact me at 'test.user@gmail.com', or call 9123456789. Visit www.example.com. The date is 15/08/2025.
Another email: admin123@yahoo.com and phone: 9876543210.
My website is www.mysite.org and my birthday is 01/01/2000.
Here is another number: 9988776655 and another email: hello.world@domain.co.in.
Some uppercase: ABCDEFG, lowercase: abcdefg, digits: 1234567890, whitespace:    .
Special chars: !@#$%^&*()_+-=[]{}|;:',.<>/?~ '''

# \w - word characters
print(re.findall('\\w', s1))

# \W - non-word characters
print(re.findall('\\W', s1))

# \d - digits
print(re.findall('\\d', s1))

# \D - non-digits
print(re.findall('\\D', s1))

# \s - whitespace
print(re.findall('\\s', s1))

# [a-z] - lowercase letters
print(re.findall('[a-z]', s1))

# [A-Z] - uppercase letters
print(re.findall('[A-Z]', s1))

# [a-zA-Z] - all letters
print(re.findall('[a-zA-Z]', s1))

# [0-9] - digits
print(re.findall('[0-9]', s1))

# Mobile numbers
print(re.findall('[6-9]{1}\\d{9}', s1))

# Emails
print(re.findall('\\w+\\.*\\w+@\\w+\\.\\w{2,3}', s1))

# Websites
print(re.findall('www\\.\\w+\\.\\w{2,}', s1))

# Dates
print(re.findall('\\d{2}/\\d{2}/\\d{4}', s1))

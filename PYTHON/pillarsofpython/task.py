# Task on functions from leetcode
# PLUS ONE PROBLEM -
# TEST CASES =
#     input is in list format 
#     add 1 into the last digit of list 
#     if i give my input as [1,2,3] then output should be [1,2,4] but whenever input is [1,2,9] then    output should be [1,3,0]
#     if input is [9,9,9] then output should be [1,0,0,0]

'''def plus_one(digits):
      n = len(digits)
      for i in range(n -1, -1, -1):
            if digits[i] < 19:
                  digits[i] +=1
                  return digits
            digits[i] = 0
      return [1] + digits

# Test case 
input = [1,2,3]
print(plus_one(input))

input = [1,2,3,4]
print(plus_one(input))

input = [1,3,9]
print(plus_one(input))

input = [1,9,8]
print(plus_one(input))

input = [9,9,9]
print(plus_one(input))

input = [11,12,19]
print(plus_one(input))
'''

# DUNDER METHODS (Magic Methods)
class bank:
    b_name = "icici"
    
    def __init__(self, n):
        self.num = n
        
    @classmethod
    def display(cls):
        print(f"Bank Name: {cls.b_name}")

class company:
    name = "google"
    loc = "world"
    ceo = "sundar pichai"
    parent = "Alphabet Inc."
    
    def __init__(self, n):
        self.num = n
        
    @classmethod
    def display(cls):
        print(f"Company Name: {cls.name}")
        
    # Arithmetic
    def __add__(self, other):
        return self.num + other.num
    def __sub__(self, other):
        return self.num - other.num
    def __mul__(self, other):
        return self.num * other.num
    def __truediv__(self, other):
        return self.num / other.num
    def __floordiv__(self, other):
        return self.num // other.num
    def __mod__(self, other):
        return self.num % other.num
    def __pow__(self, other):
        return self.num ** other.num
    
    # Relational
    def __lt__(self, other):
        return self.num < other.num
    def __le__(self, other):
        return self.num <= other.num
    def __eq__(self, other):
        return self.num == other.num
    def __ne__(self, other):
        return self.num != other.num
    def __gt__(self, other):
        return self.num > other.num
    def __ge__(self, other):
        return self.num >= other.num
    
    # Bitwise
    def __and__(self, other):
        return self.num & other.num
    def __or__(self, other):
        return self.num | other.num
    def __xor__(self, other):
        return self.num ^ other.num
    def __lshift__(self, other):
        return self.num << other.num
    def __rshift__(self, other):
        return self.num >> other.num
    
    
    # logical & and bitwise and basically performs the same operation, same goes for or operator as well
    # in case of logical not operator it will check wether the value is default or not default value and return the opposite in boolean were as in bitwise not it has its own logicx to perform the operation (-(operand + 1))
    # this is the resone why we do not have the maGIC METHOD FOR BITWISE NOT as __not__ instead we use __invert__

# objects
obj1 = company(10)
obj2 = company(5)

# Arithmetic    
print(obj1 + obj2) 
print(obj1 - obj2) 
print(obj1 * obj2) 
print(obj1 / obj2) 
print(obj1 // obj2)
print(obj1 % obj2) 
print(obj1 ** obj2)

# Relational
print(obj1 < obj2) 
print(obj1 <= obj2)
print(obj1 == obj2)
print(obj1 != obj2) 
print(obj1 > obj2)  
print(obj1 >= obj2) 

# Bitwise
print(obj1 & obj2) 
print(obj1 | obj2) 
print(obj1 ^ obj2) 
print(obj1 << obj2)
print(obj1 >> obj2)


#So when overriding operators like +, <, etc., you need to decide how those multiple properties should behave when compared or combined.

#12.WAP to print STRONG Number
n=int(input('n:'))
i=n
res=0
while n>0:
    fact = 1
    rem = n % 10
    while rem > 0:
        fact *= rem
        rem -= 1
    res += fact
    n//=10

if i==res:
    print('its a strong number')
else:
    print('its a strong number')


#13.WAP to check ArmStrong Number or Not
n=int(input("enter an number :"))
i = n
res = 0
while n>0:
    rem = n % 10
    res = res + rem ** len(str(i))
    n //=10
if(res == i):
    print("Armstrong number")
else:
    print("Not an Armstrong Number")


#WAP to check whether the given number is prime number
flag=True
n=7
i=2
while i<n:
    if n%i==0:
        flag=False
    i+=1
if flag:
        print(f"{n} is prime")
else:
        print(f"{n} is not prime")
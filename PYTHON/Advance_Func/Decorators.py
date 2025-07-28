# DECORATORS IN PYTHON - It is a function that takes another function as an argument  add additional functionality or extends its behaviour without modifying it.
# PROVIDES ADDITIONAL FUNCTIONALITY 
# BEGINS WITH @, ITSELF IS A FUNCTION.

# TYPES - INBUILT, USER DEFINED

# syntax: def fname(func):
#          def inner(*args, **kwargs):
#               pretask
#                   func(*args, **kwargs)
#                posttask
#          return inner
# use above syntax to create the decorator function.

def timer(a):
      def tame(*k):
            import time
            start = time.time()
            
            print(a(*k))
            
            end = time.time()
            print(f"total time taken to execute the function is {end - start} seconds")
      return tame

@timer
def factorial(n):
      fact =1
      for i in range(1, n + 1):
            fact *= i
      return fact
factorial(5)

@timer
def prime(n):
      flag = True
      for i in range(2,n):
            if n & i == 0:
                  flag = False
      if flag:
            return 'Prime'
      else:
            return 'Not Prime'
      
prime(7)
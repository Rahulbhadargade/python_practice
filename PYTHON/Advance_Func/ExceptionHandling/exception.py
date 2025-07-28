# Exception handling - 
# 4 key words -
# 1. Try
# 2. exception
# 3. else
# 4. finally

# types - 
# specific
# generic
# default

# Specific - 

# SYNTAX -
# try:
#       sb 
# exception spe_exc:
#       solution

# try:
#       a = int(input('Enter the Numerator: '))
#       b = int(input('Enter teh Denominator: '))
#       print(a/b)
# except ZeroDivisionError:
#       print('Do not Enter the 0 for Denominator')
      
# except ValueError:
#       print('Enter only Integer Values....')
      
# # Generic exception handling -
# try:
#       a = int(input('Enter the Numerator: '))
#       b = int(input('Enter teh Denominator: '))
#       print(a/b)
#       print(list(a))
# except Exception:
#       print('Exception has been handled!!')
      
# # Default exception handing -
# try:
#       i = 0
#       while i < 11:
#             print(i)
#             i = int(input('i:  '))
# except:
#       print("Exception Handled!!!")
      
      
# 4 blocks
# try:
#       a = int(input('Enter the Numerator: '))
#       b = int(input('Enter teh Denominator: '))
#       print(a/b)
# except Exception:
#       print('Exception has been handled!!🥴')
# else:
#       print("Attend Lectures😁")
# finally:
#       print("Do whatever you want😤😟")
      
# class RBError(Exception):
#       pass

# a= int(input('Enter the number'))
# b= int(input('Enter the number'))

import keyword
keyword.softkwlist
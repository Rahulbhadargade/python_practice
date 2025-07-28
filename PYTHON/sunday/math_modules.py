# --- Examples and Notes ---

import math
import random
import calendar
from datetime import date, datetime

# 1. Power function
print("pow(2, 3):", math.pow(2, 3))

# 2. Value of pi
print("pi:", math.pi)

# 3. Logarithm functions
print("log(100, 10):", math.log(100, 10))

# 4. Trigonometric functions
print("sin(math.pi/2):", math.sin(math.pi/2))

# 5. Square root, floor, ceil
print("sqrt(16):", math.sqrt(16))
print("floor(4.7):", math.floor(4.7))
print("ceil(4.2):", math.ceil(4.2))

# 6. Random choice from a sequence
seq = ['apple', 'banana', 'cherry']
print("choice:", random.choice(seq))

# 7. Random multiple choices
print("choices:", random.choices(seq, k=2))

# 8. Random integer between a and b
print("randint:", random.randint(1, 10))

# 9. Shuffle a list
lst = [1, 2, 3, 4, 5]
random.shuffle(lst)
print("shuffle(lst):", lst)

# 10. Random float between 0 and 1
print("random():", random.random())

# 11. Current date
print("date_today():", date.today())

# 12. Current date and time
print("datetime_now():", datetime.now())

# 13. Leap days between years
print("leapdays(2000, 2025):", calendar.leapdays(2000, 2025))

# 14. Month calendar
print("month(2025, 7):\n", calendar.month(2025, 7))

# 15. Day of the week (0=Monday)
print("weekday(2025, 7, 28):", calendar.weekday(2025, 7, 28))

# --- Notes ---
# math.pow(x, y): Returns x raised to the power y.
# math.pi: Returns the value of pi.
# math.log(x, base): Returns the logarithm of x to the given base.
# math.sin(x): Returns the sine of x radians.
# math.sqrt(x): Returns the square root of x.
# math.floor(x): Returns the largest integer <= x.
# math.ceil(x): Returns the smallest integer >= x.
# random.choice(seq): Returns a random element from the sequence.
# random.choices(seq, k): Returns k random elements from the sequence.
# random.randint(a, b): Returns a random integer between a and b (inclusive).
# random.shuffle(x): Shuffles the sequence x in place.
# random.random(): Returns a random float between 0 and 1.
# date.today(): Returns the current local date.
# datetime.now(): Returns the current local date and time.
# calendar.leapdays(y1, y2): Returns the number of leap days between years y1 and y2 (exclusive).
# calendar.month(year, month): Returns a string representing a month's calendar.
# calendar.weekday(year, month, day): Returns the day of the week (0=
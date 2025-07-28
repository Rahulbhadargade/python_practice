# PRINT "RAHUL SANJAYKUMAR BHADARGADE" WITH PATTERN PROGRAMING

def print_Name():
    # RAHUL
    for row in range(7):
        # R
        for col in range(5):
            if col == 0 or (row == 0 or row == 3) and col < 4 or (col == 4 and row in [1, 2]) or (row - col == 2 and row > 3):
                print("*", end="")
            else:
                print(" ", end="")
        print("   ", end="")

        # A
        for col in range(5):
            if (col == 0 or col == 4) and row != 0 or (row == 0 or row == 3) and (col > 0 and col < 4):
                print("*", end="")
            else:
                print(" ", end="")
        print("   ", end="")

        # H
        for col in range(5):
            if col == 0 or col == 4 or row == 3:
                print("*", end="")
            else:
                print(" ", end="")
        print("   ", end="")

        # U
        for col in range(5):
            if (col == 0 or col == 4) and row != 6 or row == 6 and (col > 0 and col < 4):
                print("*", end="")
            else:
                print(" ", end="")
        print("   ", end="")

        # L
        for col in range(5):
            if col == 0 or row == 6:
                print("*", end="")
            else:
                print(" ", end="")
        print("   ", end="")
        print()

    print("\n")

    # SANJAYKUMAR
    for row in range(7):
        # S
        for col in range(5):
            if (row == 0 or row == 3 or row == 6) and (col > 0 and col < 4) or \
               (col == 0 and (row > 0 and row < 3)) or \
               (col == 4 and (row > 3 and row < 6)):
                print("*", end="")
            else:
                print(" ", end="")
        print("   ", end="")

        #A
        for col in range(5):
            if (col == 0 or col == 4) and row != 0 or (row == 0 or row == 3) and (col > 0 and col < 4):
                print("*", end="")
            else:
                print(" ", end="")
        print("   ", end="")

        # N
        for col in range(5):
            if col == 0 or col == 4 or row == col:
                print("*", end="")
            else:
                print(" ", end="")
        print("   ", end="")

        # J
        for col in range(5):
            if (col == 3 and row != 6) or (row == 6 and col < 4 and col > 0) or (col == 0 and row > 3 and row < 6):
                print("*", end="")
            else:
                print(" ", end="")
        print("   ", end="")

        # A
        for col in range(5):
            if (col == 0 or col == 4) and row != 0 or (row == 0 or row == 3) and (col > 0 and col < 4):
                print("*", end="")
            else:
                print(" ", end="")
        print("   ", end="")

        # Y
        for col in range(5):
            if (row == col and row < 3) or (row + col == 4 and row < 3) or col == 2 and row >= 3:
                print("*", end="")
            else:
                print(" ", end="")
        print("   ", end="")

        # K
        for col in range(5):
            if col == 0 or \
               (row + col == 4) or \
               (row - col == 2):
                print("*", end="")
            else:
                print(" ", end="")
        print("   ", end="")

        # U
        for col in range(5):
            if (col == 0 or col == 4) and row != 6 or row == 6 and (col > 0 and col < 4):
                print("*", end="")
            else:
                print(" ", end="")
        print("   ", end="")

        # M
        for col in range(5):
            if col == 0 or col == 4 or (row == col and row < 3) or (row + col == 4 and row < 3):
                print("*", end="")
            else:
                print(" ", end="")
        print("   ", end="")

        # A 
        for col in range(5):
            if (col == 0 or col == 4) and row != 0 or (row == 0 or row == 3) and (col > 0 and col < 4):
                print("*", end="")
            else:
                print(" ", end="")
        print("   ", end="")

        # R 
        for col in range(5):
            if col == 0 or (row == 0 or row == 3) and col < 4 or (col == 4 and row in [1, 2]) or (row - col == 2 and row > 3):
                print("*", end="")
            else:
                print(" ", end="")
        print("   ", end="")
        print()

    print("\n")

    # BHADARGADE
    for row in range(7):
        # B
        for col in range(5):
            if col == 0 or (col == 4 and row not in [0, 3, 6]) or (row in [0, 3, 6] and col < 4):
                print("*", end="")
            else:
                print(" ", end="")
        print("   ", end="")

        # H
        for col in range(5):
            if col == 0 or col == 4 or row == 3:
                print("*", end="")
            else:
                print(" ", end="")
        print("   ", end="")

        # A 
        for col in range(5):
            if (col == 0 or col == 4) and row != 0 or (row == 0 or row == 3) and (col > 0 and col < 4):
                print("*", end="")
            else:
                print(" ", end="")
        print("   ", end="")

        # D
        for col in range(5):
            if col == 0 or (col == 4 and row not in [0, 6]) or (row in [0, 6] and col < 4):
                print("*", end="")
            else:
                print(" ", end="")
        print("   ", end="")

        # A 
        for col in range(5):
            if (col == 0 or col == 4) and row != 0 or (row == 0 or row == 3) and (col > 0 and col < 4):
                print("*", end="")
            else:
                print(" ", end="")
        print("   ", end="")

        for col in range(5):
            if col == 0 or (row == 0 or row == 3) and col < 4 or (col == 4 and row in [1, 2]) or (row - col == 2 and row > 3):
                print("*", end="")
            else:
                print(" ", end="")
        print("   ", end="")

        # G
        for col in range(5):
            if (col == 0 and row != 0 and row != 6) or \
               (row == 0 and col > 0 and col < 4) or \
               (row == 6 and col > 0 and col < 4) or \
               (col == 4 and row > 2 and row < 6) or \
               (row == 3 and col > 2):
                print("*", end="")
            else:
                print(" ", end="")
        print("   ", end="")

        # A 
        for col in range(5):
            if (col == 0 or col == 4) and row != 0 or (row == 0 or row == 3) and (col > 0 and col < 4):
                print("*", end="")
            else:
                print(" ", end="")
        print("   ", end="")

        # D 
        for col in range(5):
            if col == 0 or (col == 4 and row not in [0, 6]) or (row in [0, 6] and col < 4):
                print("*", end="")
            else:
                print(" ", end="")
        print("   ", end="")

        # E
        for col in range(5):
            if col == 0 or row == 0 or row == 3 or row == 6:
                print("*", end="")
            else:
                print(" ", end="")
        print("   ", end="")
        print()
print_Name()


# PRATIKSHA S BHADARAGADE
'''n = 5
# P
for i in range(n):
    for j in range(n):
        if j == 0 or (i == 0 or i == 2) and j < n - 1 or (j == n - 1 and i == 1):
            print('*', end='')
        else:
            print(' ', end='')
    print(end=" ")
# R
    for j in range(1, n+1):
        if j == 1 or i == 1 or ((i+j==n+1) and i < n//2+1) or (j == n and i != 2) or i == n//2+1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print(end=" ")
# A
    for j in range(n):
        if j == 0 or j == n-1 or i == 0 or i == n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print(end=" ")
# T
    for j in range(n):
        if i == 0 or j == n // 2:
            print('*', end='')
        else:
            print(' ', end='')
    print(end=" ")
# I
    for j in range(n):
        if i == 0 or j == n // 2 or i == n-1:
            print('*', end='')
        else:
            print(' ', end='')
    print(end=" ")
# K
    for j in range(n):
        if j == 0 or i + j == n - 1 and i < n // 2 or i - j == 0 and i >= n // 2:
            print('*', end='')
        else:
            print(' ', end='')
    print(end=" ")
# S
    for j in range(n):
        if i == 0 or i == 2 or i == n-1:
            print('*', end='')
        elif i == 1 and j == 0:
            print('*', end='')
        elif i == 3 and j == n - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print(end=" ")
# H
    for j in range(n):
        if j == 0 or j == n-1 or i == n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print(end=" ")
# A
    for j in range(n):
        if j == 0 or j == n-1 or i == 0 or i == n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''
    
def print_pratiksha(n=5):
    for i in range(n):
        # P
        for j in range(n):
            if j == 0 or (i == 0 or i == n // 2) and j < n - 1 or (j == n - 1 and i == 1):
                print('*', end='')
            else:
                print(' ', end='')
        print("  ", end="")

        # R 
        for j in range(n):
            if j == 0 or \
               (i == 0 or i == n // 2) and j < n - 1 or \
               (j == n - 1 and i > 0 and i < n // 2) or \
               (i > n // 2 and i == j):
                print("*", end="")
            else:
                print(" ", end="")
        print("  ", end="")

        # A
        for j in range(n):
            if j == 0 or j == n - 1 or i == 0 or i == n // 2:
                print("*", end="")
            else:
                print(" ", end="")
        print("  ", end="")

        # T
        for j in range(n):
            if i == 0 or j == n // 2:
                print('*', end='')
            else:
                print(' ', end='')
        print("  ", end="")

        # I
        for j in range(n):
            if i == 0 or j == n // 2 or i == n - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print("  ", end="")

        # K
        for j in range(n):
            if j == 0 or i + j == n - 1 and i < n // 2 or i - j == 0 and i >= n // 2:
                print('*', end='')
            else:
                print(' ', end='')
        print(end=" ")

        # S
        for j in range(n):
            if (i == 0 or i == n // 2 or i == n - 1) and (j > 0 and j < n - 1) or \
               (i == 1 and j == 0) or \
               (i == n - 2 and j == n - 1):
                print('*', end='')
            else:
                print(' ', end='')
        print("  ", end="")

        # H
        for j in range(n):
            if j == 0 or j == n - 1 or i == n // 2:
                print("*", end="")
            else:
                print(" ", end="")
        print("  ", end="")

        # A
        for j in range(n):
            if j == 0 or j == n - 1 or i == 0 or i == n // 2:
                print("*", end="")
            else:
                print(" ", end="")
        print()
print_pratiksha(n=5)
file = open("file.txt", "w")
data = "This line is written using the file handling in python. \n"
file.write(data)
file.close()

file = open("file2.txt", "w")
data = "This file is created and written using the file handling in python. \n"
file.write(data)
file.close()

file = open("Advance_Func/FILEHANDLING/file3.txt", "w")
file.writelines(["first line \n", "second line \n", "third line \n"])
file.close()

file = open("Advance_Func/FILEHANDLING/file4.txt", "w+")
data = " This file is overwritten data. after this we will read the data we stored in this file \n"
file.write(data)
file.seek(6)
read_data = file.read()
print(read_data)
file.close()

file = open("Advance_Func/FILEHANDLING/file4.txt", "r")
read_data = file.read()
print(read_data)
file.close()

with open("Advance_Func/FILEHANDLING/file5.txt", "w+") as file:
    data = "hello Machaa, this is a test file for read and write operations.\n"
    file.write(data)
    file.seek(0)
    read_data = file.read()
    print(read_data)

with open("Advance_Func/FILEHANDLING/file5.txt", "r") as file:
    data = file.readlines()
    print(data)

with open('tiger.jpeg', 'rb') as file:
    bin_data = file.read()

with open('tiger2.jpeg', 'wb') as file:
    file.write(bin_data)

with open('Video-570.mp4', 'rb') as file:
    data = file.read()

with open('Video-5702.mp4', 'wb') as file:
    file.write(data)

with open('file5.txt', 'a') as file:
    file.write("This is an appended line.\n")
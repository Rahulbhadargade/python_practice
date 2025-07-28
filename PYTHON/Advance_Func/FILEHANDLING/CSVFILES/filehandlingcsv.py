import csv

# Example 1: Write and read a simple table
data = [
    ['Name', 'Age', 'City'],
    ['Rahul', 25, 'Belagavi'],
    ['Anil', 30, 'Bangalore'],
    ['Suresh', 28, 'Mysore'],
    ['Ramesh', 35, 'Hubli']
]
with open('people.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
with open('people.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    print([row for row in reader])

# Example 2: Custom delimiter
data2 = [
    ['Product', 'Price', 'Quantity'],
    ['Pen', 10, 100],
    ['Book', 50, 200],
    ['Pencil', 5, 500]
]
with open('products.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(data2)
with open('products.csv', 'r', newline='') as file:
    reader = csv.reader(file, delimiter=';')
    print([row for row in reader])

# Example 3: DictWriter and DictReader
data3 = [
    {'Name': 'Amit', 'Age': 22, 'City': 'Delhi'},
    {'Name': 'Priya', 'Age': 24, 'City': 'Pune'},
    {'Name': 'Suresh', 'Age': 29, 'City': 'Chennai'}
]
with open('dict_people.csv', 'w', newline='') as file:
    fieldnames = ['Name', 'Age', 'City']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data3)
with open('dict_people.csv', 'r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(dict(row))

# Example 4: Append rows to an existing CSV
new_rows = [
    ['Ravi', 27, 'Goa'],
    ['Sneha', 31, 'Hyderabad']
]
with open('people.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(new_rows)
with open('people.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    print([row for row in reader])

# Example 5: Write and read numbers
numbers = [
    ['ID', 'Value'],
    [1, 100],
    [2, 200],
    [3, 300]
]
with open('numbers.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(numbers)
with open('numbers.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    print([row for row in reader])

# Example 6: Write and read boolean values
bools = [
    ['Item', 'Available'],
    ['Pen', True],
    ['Book', False]
]
with open('bools.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(bools)
with open('bools.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    print([row for row in reader])

# Example 7: Write and read with quoting
quotes = [
    ['Name', 'Comment'],
    ['Rahul', 'He said, "Hello!"'],
    ['Priya', 'Nice, clean, and simple.']
]
with open('quotes.csv', 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerows(quotes)
with open('quotes.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    print([row for row in reader])

# Example 8: Write and read empty rows
empty_rows = [
    ['A', 'B', 'C'],
    [],
    ['X', 'Y', 'Z']
]
with open('empty.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(empty_rows)
with open('empty.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    print([row for row in reader if row != []])

# Example 9: Write and read header only
header = [['Header1', 'Header2', 'Header3']]
with open('header.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(header)
with open('header.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    print([row for row in reader])

# Example 10: Write and read single column
single_col = [
    ['Names'],
    ['Rahul'],
    ['Divya'],
    ['Sahil']
]
with open('singlecol.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(single_col)
with open('singlecol.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    print([row for row in reader])
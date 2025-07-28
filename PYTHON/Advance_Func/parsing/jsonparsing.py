import json
data = [10,20,30,40,50]
print("Original Data:", data)
encrypt = json.dumps(data)
print("Encrypted Data:", encrypt)
decrypt = json.loads(encrypt)
print("Decrypted Data:", decrypt)

# Example 2: Dictionary
person = {"name": "Rahul", "age": 25, "city": "Mumbai"}
print("Original Dictionary:", person)
person_json = json.dumps(person)
print("Encrypted Dictionary:", person_json)
person_dict = json.loads(person_json)
print("Decrypted Dictionary:", person_dict)

# Example 3: List of dictionaries
students = [
    {"name": "Sahil", "marks": 85},
    {"name": "Satish", "marks": 92}
]
print("Original List of Dictionaries:", students)
students_json = json.dumps(students)
print("Encrypted List of Dictionaries:", students_json)
students_list = json.loads(students_json)
print("Decrypted List of Dictionaries:", students_list)
# List
friends = ["Sunny", "Naveen", "Alex", "Ram", "Prabhas"]
print(type(friends))

# Indexing and Slicing
print(friends[2:])
print(friends[1])
print(friends[-1])
print(len(friends))

# List Manipulation
friends.append("Karthik")
print(friends)

friends.insert(1, "Warner")
print(friends)

friends.remove("Warner")
print(friends)

friends.pop(1)
# If we did not specify any value then automatically removes the last value from the list
print(friends)

# Tuples
# Mutable = Can be changed i;e List
# Immutable = Cannot be Changed i;e Tuples

friends = ("Anee", "Sunny", "Sriram", "Manas")
print(type(friends))
print(f"My Tuple is: {friends}")

numbers = [10, 20, 100, 7, 90, 12]
print(max(numbers))

# Dictionary
student = {'name': 'Sunil', 'age': '28', 'marks': [100, 75, 90, 99, 89, 99]}
print(f"Student Dict ", student['name'])
print(student.get('subject', 'EEE'))
student['name'] = "Sam"
print(student)
student.pop('name')
print(student)
student.popitem()
print(student)
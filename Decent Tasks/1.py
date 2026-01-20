'''
Task:
You receive a list of users:

users = [
    {"id": 1, "name": "Alice", "age": 22},
    {"id": 2, "name": "Bob", "age": 17},
    {"id": 3, "name": "Charlie", "age": 30},
]

Requirements:

Filter users 18+

Return a dict {id: name}

Sort by name

Expected output:

{1: "Alice", 3: "Charlie"}
'''
users = [
    {"id": 1, "name": "Alice", "age": 22},
    {"id": 2, "name": "Bob", "age": 17},
    {"id": 3, "name": "Charlie", "age": 30},
    {"id": 4, "name": "Bobbie", "age": 30},
]
temp_dict = {}
for user in users: 
    if user["age"] >=18:
          temp_dict[user["id"]] = user["name"]
print(f"Filtered users {temp_dict}")   
temp_dict= dict(sorted(temp_dict.items(), key=lambda item:item[1]))
print(f"Sorted Users {temp_dict}")

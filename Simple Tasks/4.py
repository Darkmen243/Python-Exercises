'''
Пусть дано множество, которое представляет студентов:
students = {"Tom", "Bob", "Sam"}
И пусть дано множество, которое представляет рабочих:
employees = {"Tom", "Bob", "Alex", "Mike"}
Как видно, некоторые одновременно могут учиться и работать.
Напишите программу, которая находит
Всех людей в обоих группах
Всех людей, которые одновременно и учатся, и работают
Всех людей, которые только учатся, но не работают
Всех людей, которые либо только учатся, либо только работают, но не одновременно
'''
students = {"Tom", "Bob", "Sam"}
employees = {"Tom", "Bob", "Alex", "Mike"}
print(students.union(employees))
print(students.intersection(employees))
print(students.difference(employees))
print(print(students|employees))
'''
Создайте словарь, который хранит информацию о человеке.
Допустим, человека зовут "Том", ему 39 лет, он работает в компание SuperCorp и в работе использует языки программирования Python и JavaScript.
Сохраните всю эту информацию в словаре. 
Затем выведите эту информацию из словаря на консоль
'''
temp = {'name':"Tom", 'age':"39", 'company':"SuperCorp", 'languages':["Python", "JavaScript"]}
print("Name: ", temp.get("name"))
print("Age: ", temp["age"])
print("Company: ", temp["company"])
print("Languages: ", temp["languages"])

'''
Пусть дан следующий список, которые хранит несколько словарей:
people = [
    {"name": "Tom", "age": 39, "company": "SuperCorp", "languages": ["Python", "JavaScript"]},
    {"name": "Bob", "age": 43, "company": "BigCorp", "languages": ["Python", "C++", "C#"]},
    {"name": "Sam", "age": 28, "company": "LittleCorp", "languages": ["Python", "Java"]}
]
Каждый словарь в списке представляет программиста, где поле "name" представляет имя, а поле "languages" - список используемых языков программирования.
Выведите на консоль из каждого словаря имя и последний язык программирования, чтобы получился следуюший консольный вывод:
Name:  Tom
Last language:  JavaScript
Name:  Bob
Last language:  C#
Name:  Sam
Last language:  Java
'''
people = [
    {"name": "Tom", "age": 39, "company": "SuperCorp", "languages": ["Python", "JavaScript"]},
    {"name": "Bob", "age": 43, "company": "BigCorp", "languages": ["Python", "C++", "C#"]},
    {"name": "Sam", "age": 28, "company": "LittleCorp", "languages": ["Python", "Java"]}
]
for p in people:
    print("Name:", p["name"])
    print("Last language:", p["languages"][-1])
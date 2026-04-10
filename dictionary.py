import time

student = [
    {'name': 'John', 'age': 20, 'grade': 'A', 'major': ['Computer Science', 'PolySciences']},
    {'name': 'Jack', 'age': 25, 'grade': 'B', 'major': ['Computer Science', 'Biology', 'Chemistry']},
    {'name': 'Jerri', 'age': 23, 'grade': 'A', 'major': ['Computer Science', 'Math', 'Physics']}
]

def hello(name):
    print(f'Hello {name}!')

def determine_name():
    name = input('Enter your name: ')
    return name

stud_name = determine_name()

for s in student:
    if s['name'] == stud_name:
        hello(s['name'])
        print(s['age'])
        print(s['grade'])
        print(s['major'])
        break
else:
    print("Student not found.")
#______________________________________________________________________________________


# md = student
# print(md[1])
# for s in md:
#     for value in s.values():
#         print(value)
#         if value == 'Jack':
#             hello(s['name'])
#             print(s['major'])
#             break
#         time.sleep(1)
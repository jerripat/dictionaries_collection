import time

student = [
    {'name': 'John', 'age': 20, 'grade': 'A', 'major': ['Computer Science', 'PolySciences']},
    {'name': 'Jack', 'age': 25, 'grade': 'B', 'major': ['Computer Science', 'Biology', 'Chemistry']},
    {'name':'jerri', 'age': 23, 'grade': 'A', 'major': ['Computer Science', 'Math', 'Physics']}
    ]
# keys = student.keys()
# for each in student.keys():
#     print(each)
#
#
# for each in student:
#     print(each)
def hello(name):
    print(f'Hello {name}!')

def determine_name():
    name = input('Enter your name: ')
    return name

for s in student:
    for value in s.values():
        stud_name = determine_name()
        if value == str(stud_name):
            hello(s['name'])
            print('Major: Computer Science')
            break
        time.sleep(1)
        print(value)
#______________________________________________________________________________________


my_dictionary = {
    'name': 'John',
    'age': 20,
    'grade': 'A',
    'name': 'Jack',
    'major': ['Computer Science', 'Math', 'Physics'],
}
md = my_dictionary
print(md[0])

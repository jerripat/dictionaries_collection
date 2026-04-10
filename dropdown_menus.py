from tkinter import *

root = Tk()
root.title("Dropdown Menus")
root.geometry("300x200")

student = [
    {'name': 'John', 'age': 20, 'grade': 'A', 'major': ['Computer Science', 'PolySciences']},
    {'name': 'Jack', 'age': 25, 'grade': 'B', 'major': ['Computer Science', 'Biology', 'Chemistry']},
    {'name': 'Jerri', 'age': 23, 'grade': 'A', 'major': ['Computer Science', 'Math', 'Physics']}
]

main_menu = Menu(root)
root.config(menu=main_menu)

# File dropdown
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_command(label="Exit", command=root.quit)
main_menu.add_cascade(label="File", menu=file_menu)

# Students dropdown
students_menu = Menu(main_menu, tearoff=0)
for s in student:
    students_menu.add_command(label=s["name"])

main_menu.add_cascade(label="Students", menu=students_menu)

root.mainloop()
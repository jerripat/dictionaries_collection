# Filter(function,collection)=return all elements that pass a condition

grades = [91, 89, 88, 78, 100, 95, 93, 85, 82, 90]
passing_grades = list(filter(lambda g: g > 90, grades))
for each_grade in passing_grades:
    print(each_grade)

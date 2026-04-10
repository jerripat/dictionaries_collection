#Map Function

li =[1,2,3,4,5,6,7,8,9,10]

def func(x):
    return x**x

# newList = []
# for x in li:
#     newList.append(func(x))
#
# print(newList)

print(list(map(func,li)))

# Bro Code example
# def c_to_f(c):
#     return (c * 9/5) + 32

Celsius_temps=[0.0, 10.0, 20.0, 30.0, 40.0, 50.0]
Fahrenheit_temps=[50.0, 60.0, 70.0, 80.0, 90.0, 100.0]
#print(list(map(c_to_f,Celsius_temps)))
print(f"Fahrenheit_temps: {Fahrenheit_temps}")

#using lambda
fahrenheit_temps=list(map(lambda c: (c * 9/5) + 32, Celsius_temps))
print(f"Fahrenheit_temps: {fahrenheit_temps}")
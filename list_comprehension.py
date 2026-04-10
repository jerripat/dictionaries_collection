x = [i for i in range(10)]
print(x)


nums_squared = [n**2 for n in range(1,101)]
print(nums_squared)

remanders=[x**2 % 5 for x in range(1,101) if x > 2]
print(remanders)

# __________________________________________________
doubles = []
for i in range(1,10):
    doubles.append(i*2)
print(doubles)
triples = [i*3 for i in range(1,10)]
print(triples)


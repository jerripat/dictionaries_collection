def func(x):
    func2 = lambda x: x + 5
    return func2(x) + 85

func3 = lambda x: x + 5 if x > 3 else x

print(func3(2))
print(func(2))
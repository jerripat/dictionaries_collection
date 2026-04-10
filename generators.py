

def count_to(n):
    count = 1
    while count <= n:
       yield count  # yield the current count value
       count += 1


numbers = int(input("Enter a number to count to: "))

for n in count_to(numbers):
    print(n)
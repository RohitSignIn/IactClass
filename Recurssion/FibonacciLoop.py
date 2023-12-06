# Fibonacci Using loop 

n = 5
first = 0
second = 1

print(first, second, "", end="", sep=" => ")

for i in range(n-2):
    next = first+second
    print(next, "", end="", sep=" => ")
    first = second
    second = next 

print("End")
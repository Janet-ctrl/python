#range
for value in range(1, 5):
    print(value)

for value in range(6):
    print(value)

#numbers
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

odd_numbers = list(range(1,20,3))
print(odd_numbers)

#squares
squares = []
for value in range(1,11):
    square = value **2
    squares.append(square)
print(squares)

#short hand
squares =[]
for value in range(1,11):
    squares.append(value**2)
print(squares)

#list comprehensions shorter hand
squares = [value**2 for value in range(1,11)]
print(squares)

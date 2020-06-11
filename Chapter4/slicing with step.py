numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

#Slice every second item
print(numbers[0:5:2])

#everything excluding the last 2
print(numbers[:-2])

#reverse the entire list 10 - 1
print(numbers[::-1])

#the 1st 2 items reversed
print(numbers[1::-1])

#the last 2 items reversed
print(numbers[:-3:-1])

#everything excluding the last 2 items reversed
print(numbers[-3::-1])


####  alternative

print(numbers[slice(1,8,2)])



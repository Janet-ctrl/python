# replacing on the list
motorcycles = ['honda', 'yamaha', 'suziki']
motorcycles[0] = 'ducati'
print(motorcycles)

# adding to the list
motorcycles.append('honda')
print(motorcycles)

# insert into list
motorcycles.insert(-1, 'bmw')
print(motorcycles)

# removing from list
del motorcycles[-1]
print(motorcycles)

# popped method
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# popped method in action
last_owned = motorcycles.pop()
print(f'The last motorcycle I owned was a {last_owned.title()}.')

# pop from any position
first_owned = motorcycles.pop(0)
print(f'The first motorcycle I owned was a {first_owned.title()}.')

# one motorcycle left in the list.. hahaha
print(motorcycles)

#add motorcycles
motorcycles.append('bmw')
motorcycles.append('harley')
motorcycles.append('mercedes')
motorcycles.append('ducati')
print(motorcycles)

#removing by value
motorcycles.remove('yamaha')
print(motorcycles)

#remove by value providing reason
too_expensive = 'mercedes'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f'\nA {too_expensive.title()} is too expensive for me.')

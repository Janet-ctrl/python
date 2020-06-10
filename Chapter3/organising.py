#Organising lists

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
print(f'\n')

cars.sort(reverse=True)
print(cars)
print(f'\n')
cars.sort(reverse=False)

cars.clear()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f'Here is the original list: {cars}\n')

print(f'Here is the sorted list: {sorted(cars)}\n')

print(f'Here is the original list again: {cars}\n')

#Length
len(cars)

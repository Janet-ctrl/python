guest = ['Elvis', 'Pietie', 'Tante Koba']
invite = f'Come Party!'


print(f'\nHaloo {guest[2]}! {invite}')
print(f'\nHi!! {guest[0]}! {invite}')
print(f'\nHey {guest[1]}!! {invite}')

print(f'\nAwww, {guest[0]} can\'t make it.. Too bad.\n')

#guest list
print(f'This is out guest list {guest}\n')
#replacing guest
del guest[0]
guest.insert(0, 'Ouma Hettie')
print(f'And this is the updated list!! {guest}')
print(f'\nHi!! {guest[0]}! {invite}')
print(f'\nHi!! {guest[0]}! {invite}')
print(f'\nHey {guest[1]}!! {invite}')



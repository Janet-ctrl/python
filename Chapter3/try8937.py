guest = ['Elvis', 'Pietie', 'Tante Koba']
invite = f'Come Party!'


print(f'\nHaloo {guest[2]}! {invite}')
print(f'\nHi!! {guest[0]}! {invite}')
print(f'\nHey {guest[1]}!! {invite}')

not_guest = guest.pop(0)
print(f'\nAwww, {not_guest} can\'t make it.. Too bad.\n')

#replacing guest
guest.insert(0, 'Ouma Hettie')
print(f'We have a new guest!! {guest}')
print(f'\nHi!! {guest[0]}! {invite}')
print(f'\nHi!! {guest[2]}! {invite}')
print(f'\nHey {guest[1]}!! {invite}\n')

print(f'We have room for more!!\n')
# new guests added
guest.insert(0, 'Susan')
guest.insert(2, 'Karools')
guest.append('Mad Hatter')
# invites for new guests
print(f'\nHi!! {guest[0]}! {invite}')
print(f'\nHi!! {guest[1]}! {invite}')
print(f'\nHi!! {guest[2]}! {invite}')
print(f'\nHi!! {guest[3]}! {invite}')
print(f'\nHi!! {guest[4]}! {invite}')
print(f'\nHi {guest[5]}!! {invite}\n')

#Sad news
print(f'Hey guys.. So I have some sad news. The table is delayed. I only have room for 2 at the moment.')

#remove using pop
guest.pop(0)
guest.pop(2)
guest.pop(3)
guest.pop(1)

#new invites
print(f'\nI would like it if you could still come {guest[0]}!!')
print(f'\nIt would be nice if you could still join me {guest[1]}.\n')

#delete guests
del guest[0]
del guest[0]

#Current guest list
print(f'Current guests {guest}')
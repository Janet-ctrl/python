#copies

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print('My favorite foods are:')
print(my_foods)

print('\nMy friend\'s favorite foods are:')
print(friend_foods)

#adding to both lists to prove they are seperate
my_foods.append('pasta')
friend_foods.append('cheese crackers')

print(f'\nMy fav food: {my_foods}')
print(f'\nMy friends favs: {friend_foods}')



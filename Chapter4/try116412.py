pizzas =['pikkant', 'meaty treat', 'three cheese', 'chicken', 'sweet chilli']
friend_pizzas = pizzas[:]

pizzas.append('vegi')
friend_pizzas.append('hawain')

print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza.title())

print('\nMy Friend\'s favorite pizzas are:')
for pizza in friend_pizzas:
    print(pizza.title())
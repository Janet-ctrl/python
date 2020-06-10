#List of sporting hobbies
hobbies = ['Water ski', 'Jet Ski', 'Game hunting', 'Competition Shooting', 'Quadbike Riding']
print(hobbies)

#sort hobbies alphabetically permenantly
hobbies.sort()
print(hobbies)

#reverse sort
hobbies.reverse()
print(hobbies)

#temporary sort
print(sorted(hobbies))

#remove and reassign quadbikung to offroad hobby
offroad_hobby = hobbies.pop(-1)
print(f'\n{offroad_hobby} can be enjoyed by all ages.\n')

#insert a hobby at the front
hobbies.insert(0, 'Mountain biking')
print(hobbies)

#add hobby at the end of the list
hobbies.append('bi-athalon')
print(hobbies)

#delete bi-athalon
del hobbies[-1]
print(hobbies)

#reverse alphabetize the list
hobbies.sort()
hobbies.sort(reverse=True)
print(hobbies)

#count the lenth of the list
total = len(hobbies)
print(f'I have a total of {len(hobbies)} hobbies.')

#check the index number of 'Jet Ski'
print(hobbies.index('Jet Ski'))

#make a copy of the list
print(hobbies.copy())

#remove the element with the index value of 3
print(f'This is all the hobbies: {hobbies}.')
hobbies.remove('Jet Ski')
print(hobbies)

#cleat the list out
hobbies.clear()
print(f'Time for a new adventure, my current hobby list is: {hobbies} lets start fresh.')




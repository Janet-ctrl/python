players =['charles', 'martina', 'michael', 'florence', 'eli', 'eddie']

#Starting at the first name and ending @ 3
print(players[0:3])

#starts @ 2nd name ends @ 3
print(players[1:4])

#starts at the 1st and includes the 4th item in the list
print(players[:4])

#starts @ 3rd through to end
print(players[2:])

#prints the last 3 names on the list
print(players[-3:])

#skip between items in range ???
print(players[0:3:2])

#looping through a slice
print(f'Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())




print('Welcome to the Band Name Generator')
# use \n to create a new line to be readable
city = input('Where did you grow up in?\n')
pet = input('What is the name of the first pet you had before?\n')
print('Your band name could be: ' + city + ' ' + pet)
print(f'Your band name could be: {city} {pet} or {pet} {city}')
print('{0} {1}'.format(city, pet))
bandName0 = city + ' ' + pet
bandName1 = f'{city}{pet}1'
bandName2 = f'{pet}{city}2'
bandName3 = '{0}{1}3'.format(city, pet)

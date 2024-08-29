# len() can not be used to find the length of an integer.
len('12345')

#  type() can be used to find the type of variable.
print(type(69))
print(type('sixty nine'))
print(type(True))
print(type(69.31))

print(tuple('Hello' + f'{2 * "W"} + C3'))
print(type(tuple('Hello' + '{}{}'.format(2 * 'W', 'C3'))))


# ---Converting data types---

# int() can be used to convert a string or a float to an integer.
print(int(69.69)) # 69
print(int('69')) # 69

# float() can be used to convert a string or an integer to a float.
print(float(69)) # 69.0
print(float('69')) # 69.0

# str() can be used to convert an integer or a float to a string.
print(str(69)) # '69'
print(str(69.69)) # '69.69'

# bool() can be used to convert a string, an integer or a float to a boolean.
print(bool(69)) # True
print(bool(0)) # False
print(bool('')) # False
print(bool(' ')) # True
print(bool('69')) # True
print(bool('False')) # True

# TASK: Make this line of code run without errors.
# print("Number of letters in your name: " + len(input("Enter your name")))
print('Number of letters in your name: ' + str(len(input('Enter your name\n'))))

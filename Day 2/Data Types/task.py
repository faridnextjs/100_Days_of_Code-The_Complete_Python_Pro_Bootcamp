# Subscripting
print('Farid'[0])
print('Farid'[-1])

# String
print('031' + '069') # 031069

# Integer = Whole number
print(60 + 9) # 69

# Large Integer = Large number
# You can use underscore and comma to separate the numbers

print(123_456_789_098_765_432_1 + 1) # 1234567890987654322
# Each number does not have leading zeros and can add spaces among them
print(123, 456, 789, 98, 765, 432, 1 + 1) # 123 456 789 98 765 432 2

# Float, Floating Point Number = Decimal number
# You can use dot to show the decimal point
print(3.14) # 3.14
print(314_69.31) # 31469.31

# Boolean = True or False
print(True) # True
print(False) # False

# Bytes = Binary data
print(b'Hello') # b'Hello'
print(b'Hello'[0]) # 72

# Tuple = Immutable list (cannot be changed) like a constant
print((1, 2, 3)) # (1, 2, 3)
print((1, 2, 3)[0]) # 1
mixed_tuple = (1, "hello", 3.14)
tuple_without_parens = 1, 2, 3
single_element_tuple = (42,)  # Without the comma, it would just be an integer

# This will raise a TypeError cannot change the value of a tuple
# mixed_tuple[0] = 10

# List = Mutable list
print([1, 2, 3]) # [1, 2, 3]
print([1, 2, 3][0]) # 1

# Range = A sequence of numbers
print('range(5)') # range(5)
print(range(5)) # range(0, 5)

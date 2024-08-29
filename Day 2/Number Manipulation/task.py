bmi = round(63 / 1.74 ** 2) # 63 is weight in kg and 1.74 is height in meters
print(bmi) # 21


# round() function rounds the number to the nearest integer.
print(round(6.4555)) # 6
print(round(6.5000)) # 6
print(round(6.6510)) # 7

print(round(6.5511, 2)) # 6.55
print(round(6.5511, 1)) # 6.6
print(round(6.5511, 0)) # 7.0
print(round(6.5511, -1)) # 10.0
print(round(6.5511, 3)) # 6.551

# Assignment Operators +=, -=, *=, /=, **=, //=, %=
score = 11
print(score) # 11
score += 3 # score = score + 3
print(score) # 14
score -= 3 # score = score - 3
print(score) # 11
score *= 3 # score = score * 3
print(score) # 33
score /= 3 # score = score / 3
print(score) # 11.0
score **= 3 # score = score ** 3
print(score) # 1331.0
score //= 3 # score = score // 3
print(score) # 443.0
score %= 3 # score = score % 3
print(score) # 2.0

# f-string is used to format the string
score = 11
height = 1.74
isWinning = True
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}") # Your score is 11, your height is 1.74, you are winning

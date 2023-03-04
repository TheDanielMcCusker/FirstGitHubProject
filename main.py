# int, str, array, object, bool, NaN

daniel_age = 32 # int
john_age = 24 # int
name = "Daniel" # string
daniel_favorite_numbers = [1, 2, 4, 7] # arr of integers
daniel_is_male = True # bool
daniel_mixed_favorites = [111, name, daniel_is_male] # array of mixed data types

cutoff_age = 30

# print(daniel_age + john_age)
# print(daniel_favorite_numbers[0] + daniel_favorite_numbers[1]+ daniel_favorite_numbers[2])

# print(daniel_is_male)

# print(type(daniel_age))
# print(type(daniel_favorite_numbers))
# print(type(daniel_is_male))

# if(daniel_favorite_numbers[3] >= cutoff_age):
#   print("You are old as fuck.")
# else:
#   print("You're a spry, young chick.")
  

# function 
def add_sum(num1, num2):
    sum = num1 + num2
    sum2 = sum + num1
    return sum2

# Funtion call

funtion_sum = add_sum(daniel_age, john_age)
print(funtion_sum)
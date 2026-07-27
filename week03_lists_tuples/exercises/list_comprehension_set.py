squares_of_numbers = []
even_numbers = []
languages = ['python','java','c++','javascript']

for number in range(1,11):
    squares= number * number
    squares_of_numbers.append(squares)


for number in range(2,21,2):
    even_numbers.append(number)

upper = [language.upper() for language in languages]



print(squares_of_numbers)
print(even_numbers)

print(upper)
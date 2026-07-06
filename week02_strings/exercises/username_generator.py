first_name = input("Enter your first name: ").lower()
last_name = input("Enter your last name: ").lower()
birth_year =input("Enter your birth year: ").lower()

option1 = first_name + "_" + last_name
option2 = first_name[0] + last_name + birth_year[2:4]
option3 = last_name[::-1] + birth_year

print("Username Options")
print("1. ",option1)
print("2. ",option2)
print("3. ",option3)
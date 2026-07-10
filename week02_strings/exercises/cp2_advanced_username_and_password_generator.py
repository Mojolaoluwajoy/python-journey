print("=================================================")
print("USERNAME AND PASSWORD GENERATOR")
print("=================================================")

first_name =input("Enter your first name: ").lower()
last_name = input("Enter your last name: ").lower()
birth_date = input("Enter your birth date: ")
favourite_number = input("Enter your favourite number: ")

print("=================================================")



print("Username options: ")
print("1. ",first_name + "_" + last_name)
print("2. ",first_name[0] + last_name + birth_date[2:4])
print("3. ",last_name[::-1]+birth_date)
print("4. ",first_name[0:4]+"."+last_name)
print("5. ",first_name[0]+"."+last_name+"."+birth_date)

print("=================================================")
suggested_password =first_name[0:3] + last_name[-3:]+birth_date+favourite_number
strength =""
print("PASSWORD SUGGESTION: ",suggested_password)
if len(suggested_password) >=12:
    strength = "strong"
elif len(suggested_password) >=8:
    strength = "medium"
else:
    strength = "weak"

print("PASSWORD STRENGTH: ",strength)


print("=================================================")

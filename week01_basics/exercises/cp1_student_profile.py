full_name = input("Enter your full name: ")
age = int(input("Enter your age: "))
university =input("Which university do you study at: ")
course = input("Wha's your course of study?:")
gpa = float(input("Whats your current gpa(demimal): "))
favourite_language =input("What's your favourite programming language: ")

if gpa >= 3.5:
   gpa_class = "First Class"
elif gpa >=3.0:
   gpa_class = "Second class Upper"
elif gpa >=2.0 :
   gpa_class = "Second class Lower"
else:
   gpa_class ="Pass"

print("=====================================================")
print("STUDENT PROFILE CARD")
print("=====================================================")

print("Full Name: ",full_name)
print("Age: ",age)
print("University: ",university)
print("Course: ",course)
print("GPA: ",gpa)
print("Favourite Language: ",favourite_language)

print("-----------------------------------------------------")

print("Next Birthday: ",age + 1)
print("GPA Class: ",gpa_class)


print("=====================================================")
print("rofie generated successfully")
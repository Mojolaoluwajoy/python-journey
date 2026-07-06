full_name = input("Enter your full name: ")

words = full_name.split()
initials=""
if len(words) >= 1:
    initials = initials + words[0][0] + "."

if len(words) >= 2:
    initials = initials + words[1][0] + "."

if len(words) >= 3:
    initials = initials + words[2][0] + "."

print("initials: ",initials)
word = input("Enter a word: ")

reversed = word[::-1]
print(reversed)

if word.lower() == reversed.lower():
    print("Palindrome: True")
else:
    print("Palindrome: False")
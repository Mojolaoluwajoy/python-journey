sentence = input ("Enter a sentence: ")

print("Uppercase: ",sentence.upper())

word = sentence.split()
word_count =len(word)
print("Word count: ",word_count)

no_space= sentence.replace(" ","")
char_count= len(no_space)
print("Char count: ",char_count)

vowels ="aeiou"
count =sum(1 for char in sentence.lower() if char in vowels)
print("Vowel count: ",count)

words =sentence.split()
lengths =[len(words)]
longest_word =max(words,key =len)
print("Longest word: ",longest_word)


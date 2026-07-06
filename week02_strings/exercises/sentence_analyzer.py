
sentence = input("Enter a sentence: ")

word_count = len(sentence.split(" "))

no_space = sentence.replace(" ","")
char_count = len(no_space)

vowels ="aeiou"
vowel_count =sum(1 for char in sentence.lower() if char in vowels)

starts_with = sentence.startswith("The")
ends_with = sentence.endswith("dog")


words =sentence.split()
lengths =[len(words)]
longest_word =max(words,key =len)

shortest_word = min(words,key =len)
title_case = sentence.title()

words.reverse()
reversed_words = " ".join(words)

print("--- Sentence Analysis ---")
print("Word count: ",word_count)
print("Char count: ",char_count)
print("Vowel count: ",vowel_count)
print("Starts with: ",starts_with)
print("Ends with: ",ends_with)
print("Longest word: ",longest_word)
print("Shortest word: ",shortest_word)
print("Title case: ",title_case)
print("Reversed words: ",reversed_words)

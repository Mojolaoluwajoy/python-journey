events = [n for n in range (1,21) if n % 2 == 0]
print(events)

scores = [92, 78, 85, 67, 90, 55, 88]
high_scores = [a for a in scores if a >= 80]
print(high_scores)

language = ['python','java','c++']
upper =[lang.upper() for lang in language]
print(upper)
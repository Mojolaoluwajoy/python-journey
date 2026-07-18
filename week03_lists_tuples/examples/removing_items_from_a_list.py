languages = ['Python', 'Java','C++', 'JavaScript', 'Ruby']

languages.remove('C++')
print(languages)

removed = languages.pop()
print(removed)
print(languages)

removed = languages.pop(1)
print(removed)
print(languages)

del languages[0]
print(languages)


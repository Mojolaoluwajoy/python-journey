shopping_items = ["apple", "banana", "cherry","bread","butter"]

for item in range(len(shopping_items)):
    print(f'{item}: {shopping_items[item]}')
print()

shopping_items.append("orange")
shopping_items.append("mango")
shopping_items.insert(1, "sweets")
shopping_items.remove("banana")


for item in range(len(shopping_items)):
    print(f'{item}: {shopping_items[item]}')

print("Total items: ", len(shopping_items))



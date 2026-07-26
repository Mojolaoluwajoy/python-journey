numbers =[]

for index in range(1, 11):
    number =input(f"Enter number {index}:")

    numbers.append(number)


numbers= [int(number) for number in numbers]
print("...Statistics Report...")

print(f"Numbers: {numbers}")

print(f"Minimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"sum: {sum(numbers)}")
print(f"Average: {sum(numbers)/len(numbers)}")

print(f"Sorted(asc): {sorted(numbers)}")
print(f"Sorted(desc): {sorted(numbers, reverse=True)}")



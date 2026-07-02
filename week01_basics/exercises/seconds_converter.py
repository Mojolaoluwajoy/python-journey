seconds = int(input("Enter seconds: "))
hour=seconds//3600
remaining=seconds % 3600
minute =remaining // 60
remaining_seconds = remaining % 60
print(f"{seconds} seconds = {hour} hour(s), {minute} minute(s), and {remaining_seconds} second(s)")
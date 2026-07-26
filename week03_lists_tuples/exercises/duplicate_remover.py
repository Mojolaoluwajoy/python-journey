originals = [3,1,4,1,5,9,2,6,5,3,5]
cleaned = []
removed = []

for original in originals:
    if original not in cleaned:
        cleaned.append(original)
    elif original in cleaned:
            removed.append(original)


print(f"Originals: {originals}")
print(f"Cleaned: {cleaned}")
print(f"Removed: {removed}")
print(f"Removed Length: {len(originals) - len(cleaned)}")
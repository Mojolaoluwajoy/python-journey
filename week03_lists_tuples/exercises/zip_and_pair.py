names = ['Alice', 'Bob', 'Mojo', 'Diana', 'Eve']
scores = [88,72,95,81,63]

zipped = list(zip(names, scores))


sorted_pairs = sorted(zipped,key = lambda pair: pair[1],reverse=True)

print(f"names: {names}")
print(f"scores: {scores}")
print()
print("---- Leaderboard ----")
print()
rank = 1

for name,score in sorted_pairs:
    print(f"{rank}. {name} -- {score}")
    rank += 1


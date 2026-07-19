scores = [92, 78, 85, 90, 67]

for score in scores:
    print(f'Score: {score} --pass' if score >= 70 else f'Score: {score} --fail')

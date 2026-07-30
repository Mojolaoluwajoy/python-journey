students=[

    ['Mojolaoluwa Joy',[92,88,5,79,85]],
    ["Oluwapelumi Babatunde",[78,82,75,80,77]],
    ['Omobolanle Victoria',[65,70,68,72,60]]

    ]




for student in students:
    name = student[0]
    score = student[1]
    summation = sum(score)
    average = summation/5
    high_score = max(score)
    low_score = min(score)

    print(f"{name}: {score}")
    print(f'summation: {summation}')
    print(f'average: {average}')
    print(f'highest score: {high_score}')
    print(f'lowest score: {low_score}')


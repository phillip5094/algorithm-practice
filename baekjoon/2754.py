score = {
    'A' : {
        '+' : '4.3',
        '0' : '4.0',
        '-' : '3.7'
    },
    'B' : {
        '+' : '3.3',
        '0' : '3.0',
        '-' : '2.7'
    },
    'C' : {
        '+' : '2.3',
        '0' : '2.0',
        '-' : '1.7'
    },
    'D' : {
        '+' : '1.3',
        '0' : '1.0',
        '-' : '0.7'
    },
}

grade = input()

if len(grade) == 1:
    print('0.0')
else:
    print(score[grade[0]][grade[1]])

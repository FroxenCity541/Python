def add_score():
    k = input('plz enter subject:')
    while True:
        try:
            v = int(input('plz enter score:'))
        except:
            print("plz dooooooooo it again")
        else:
            grade[k] = v
            break


def remove_score():
    remove = input(' plz enter remove key:')
    if remove in grade:
        grade.pop(remove, '')
    else:
        print('cant find thing')


def submit_score():
    print(f'my grade average:{sum(grade.values())/len(grade)}')


grade = {}

while True:
    for key, value in grade.items():
        print(f'{key}:{value}')
    print('1. add grade')
    print('2. remove grade')
    print('3. summit grade')
    hello = input("plz enter 1 ,2 or 3:")
    if hello == '1':
        add_score()

    elif hello == '2':
        remove_score()

    elif hello == '3':
        submit_score()
        break

    else:
        print('plz do it again')

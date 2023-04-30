import random

answer = random.randrange(1, 101)
min = 1
max = 100
while True:
    i = int(input(f'plz give a number from {min} to {max}:'))
    if i < answer:
        print('bigger')
        if min < i:
            min = i
    if i > answer:
        print('SMaller')
        if max > i:
            max = i
    if i == answer:
        print('u got this')
        break

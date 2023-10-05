# for i in range(2,6)
#     print(i)
# else:
#     print("normal")
# i = 1
# while i<6:
#     if i== 3:
#         break
#     print(i)
#     i+=1

# for i in range(1,6):
#     if i == 3
#     break
# print(i)

# i = 1
# while i < 6:
#     if i == 3
#     i += 1
#     continue
# print(i)

# while True:
#    i= input('請輸入編號')
#     if  i=='1':
#      print('蘋果汁')
#     if  i=='2':
#      print('柳橙汁')
#     if  i=='3':
#      print('葡萄汁')
#     if  i=='4':
#      print('離開')

import random

# random.randrange(3)
# a = random.randrange(0, 8000, 2)
# print(a)
# random.randint(1, 3)
# random.randint(1, 10)
answer = random.randrange(1, 101)
while True:
    i = int(input('請輸入編號'))
    if i < answer:
        print('bigger')
    if i > answer:
        print('SMaller')
    if i == answer:
        print('u got this')
        break

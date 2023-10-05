# i = 0
# while i < 7:
#     print(i)
#     i += 1

# baka = input('plz answer this question: 1+1=?')
# while baka != '3':
#     print('u will go to school for 10hrs')
#     baka = input('plz answer this question')

# print("u can play brawl stars for 10hrs")

# x = int(input('plz eat prime'))
# if x == 1:
#     print('酩酊大醉酩酊大醉酩酊大醉酩酊大醉酩酊大醉酩酊大醉酩酊大醉酩酊大醉酩酊大醉酩酊大醉酩酊大醉酩酊大醉酩酊大醉酩酊大醉酩酊大醉')
# else:
#     i = 2
#     while x % i != 0 and i != x:
#         i += 1
#     if i == x:
#         print("yes")
#     else:
#         print("no")

n = 3
n1 = n
for i in range(n):
    n1 -= 1
    print(' ' * n1 + (i * 2 + 1) * '*')
for i in range(n):
    print(' ' * (n - 1) + '*')

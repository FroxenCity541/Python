# x = int(input('pls input a number'))
# if x % 2 == 0:
#     print('even')
# else:
#     print('odd')

import turtle

# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.done()
for i in range(5):
    print(i)
for i in range(2, 6):
    print(i)
for i in range(2, 10, 2):
    print(i)
turtle.speed(0)
turtle.color('blue')
turtle.shape('turtle')
turtle.stamp()
turtle.penup()
for i in range(0, 50000000, 3):
    turtle.forward(i)
    turtle.right(35)
    turtle.stamp()
turtle.done()

# turtle.pensize(5)
# turtle.pencolor("blue")
# turtle.fillcolor("blue")
# turtle.begin_fill()
# for i in range(5):
#     turtle.forward(200)
#     turtle.right(144)
# turtle.end_fill()
# turtle.done()
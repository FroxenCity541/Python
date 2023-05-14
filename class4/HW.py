import turtle as l

# l.penup()
# l.stamp()
# for i in range(8):
#     l.forward(200)
#     l.stamp()
#     l.backward(200)
#     l.right(45)

import time

l.speed(0)
for i in range(60):
    l.forward(200)
    l.stamp()
    l.backward(200)
    l.right(6)
    time.sleep(1)
    l.clear()

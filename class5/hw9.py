import turtle as t
import time


# t.shape("arrow")
# t.stamp()

t.pensize(2)
t.pencolor("black")

for i in range(1, 60):
    t.forward(100)
    time.sleep(1)
    t.home()
    t.right(6 * i)
    t.clear()

t.done()

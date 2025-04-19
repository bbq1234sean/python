import turtle as t
import time

t.speed(0)
t.pencolor("black")

for i in range(1, 60):
    t.right(6 * i)
    t.forward(80)
    time.sleep(1)
    t.home()
    t.clear()

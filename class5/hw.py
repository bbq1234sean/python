import turtle as t

t.penup()
t.color("black")
t.shape("arrow")
t.stamp()
for i in range(9):
    t.forward(100)
    t.stamp()
    t.home()
    t.right(45 * i)


t.done()

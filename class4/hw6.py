import turtle as t

t.penup()
t.color("dark red")
t.shape("circle")
for i in range(58):
    t.forward(i * 2)
    t.stamp()
    t.right(25)

t.done()

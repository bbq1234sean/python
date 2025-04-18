import turtle as t

t.pensize(5)
t.pencolor("yellow")
t.fillcolor("yellow")
t.begin_fill()
for i in range(5):
    t.forward(200)
    t.right(144)

t.end_fill()

t.done


x = int(input("請輸入數字:"))
sum = 0
for i in range(x + 1):
    sum = sum + i
print(sum)

for i in range(1, 10):
    for j in range(1, 10):
        print(str(i) + "x" + str(j) + "=" + str(i * j))

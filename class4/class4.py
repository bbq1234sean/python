n = int(input("請輸入數字:"))
if n % 2 == 0:
    print(f"{n}是偶數")
else:
    print(f"{n}是奇數")

# 匯入模組
# import turtle  #匯入模組turtle
import turtle as t  # 匯入模組turtle

# from turtle import * #匯入所有指令
# from turtle import done #匯入指令done

# done()
# turtle.done()

t.speed(0)
t.color("green")
t.shape("turtle")
t.stamp()
t.penup()
for i in range(4):
    t.forward(100)
    t.right(90)
t.done()

# for example
# for的組成有三個
# for 變數 in 範圍:
# 迴圈變數只能活在for內
for i in range(6):  # range(6)為0到5的數字
    print(i)

for i in range(1, 6):  # range(1,6)為1到5的數字
    print(i)

for i in range(1, 6, 2):  # range(1,6,2)為1到5的數字,每2個數字
    print(i)

import turtle

turtle.color("red")
turtle.shape("turtle")
turtle.stamp()
turtle.penup()

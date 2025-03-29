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
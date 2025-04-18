"""
請輸入正整數:20
3
6
7
9
12
14
15
18
"""

x = int(input("請輸入正整數:"))
for i in range(1, x):
    if i % 3 == 0:
        print(i)
    elif i % 7 == 0:
        print(i)

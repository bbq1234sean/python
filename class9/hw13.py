"""
回家作業1
修改上課的練習程式，當使用者輸入數值時，程式不僅提示再大再小還需要提示縮小過後的輸入範圍
EX:
請輸入0~100的整數:50
再小一點
請輸入0~50的整數:25
再小一點
請輸入0~25的整數:15
再大一點
請輸入15~25的整數:30
再小一點
請輸入15~25的整數:10
再大一點
請輸入15~25的整數 L:20
再大一點
請輸入20~25的整數:23
再大一點
請輸入23~25的整數:24
恭喜猜中!
"""

import random

u = 100
l = 0
a = random.randrange(1, 101)
x = int(input("請輸入1-100的整數 :"))
while True:

    if x < a:
        if x > l:
            l = x
        print("再大一點")
        x = int(input("請輸入" + str(l) + "~" + str(u) + "的整數:"))
        continue
    elif x > a:
        if x < u:
            u = x
        print("再小一點")
        x = int(input("請輸入" + str(l) + "~" + str(u) + "的整數:"))
        continue
    else:
        print("恭喜猜中")
        break


L = ["1.蘋果汁", "2.柳橙汁", "3.葡萄汁", "4.系統關閉"]
print(L)


while True:

    ans = input("請輸入編號:")
    if int(ans) == 4:
        print("系統關閉")
        break

    else:
        for i in range(len(L)):

            if int(ans) > len(L):
                print("輸入錯誤查無此果汁,請重新輸入輸入錯誤查無此果汁,請重新輸入")
                break
            elif int(ans) == i:
                print("您點的商品是:" + L[i - 1])
                break
            else:
                continue


juice = ["蘋果汁", "柳橙汁", "葡萄汁", "系統關閉"]

while True:
    for i in range(len(juice)):
        print(f"{i + 1}.{juice[i]}")
    try:
        n = int(input("請輸入編號編號:"))
    except:
        print("輸入錯誤,請重新輸入")
        continue
    if n == len(juice):
        print("系統關閉")
        break
    elif 1 <= n <= len(juice):
        print(f"您點的商品是{juice [n - 1]}")

    else:
        print("輸入錯誤,請重新輸入")

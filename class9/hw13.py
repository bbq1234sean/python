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

password = 24

Upper = 100
Lower = 0
num = int(input("請輸入0~100的整數:"))  # 取得輸入的數字

while True:

    if num < 0 or num > 100:
        num = int(input("請輸入0~100範圍內的整數:"))
        continue
    elif num > password:
        Upper = num
        print("再小一點")
        num = int(input("請輸入" + str(Lower) + "~" + str(Upper) + "的整數:"))
        continue
    elif num < password:
        Lower = num
        print("再大一點")
        num = int(input("請輸入" + str(Lower) + "~" + str(Upper) + "的整數:"))
        continue
    else:
        print("恭喜猜中!")
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

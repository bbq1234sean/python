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
        num=int(input("請輸入" + str(Lower) + "~" + str(Upper) + "的整數:"))
        continue
    elif num < password:
        Lower = num
        print("再大一點")
        num = int(input("請輸入" + str(Lower) + "~" + str(Upper) + "的整數:"))
        continue
    else:
        print("恭喜猜中!")
        break
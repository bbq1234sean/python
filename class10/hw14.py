L = ["晴天", "多雲", "雨天", "晴天", "多雲", "雷陣雨", "晴天"]
print(L)

while True:

    try:
        ans = int(input("請輸入要修改得星期數字(1-7):"))
    except:
        print("請輸入數字編號")
    else:
        if ans > len(L) or ans < 1:
            print("輸入錯誤,請重新輸入")

        else:
            print("你要修改的星期是" + str(ans))
            print("原本的天氣是" + L[ans])
            r = input("請輸入新的天氣:")
            print("修改後的天氣是" + r)
            L[ans] = r
            print(L)
            break

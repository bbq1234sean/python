print("1.蘋果汁")
print("2.柳橙汁")
print("3.葡萄汁")
print("4.系統關閉")
while True:
    print("1.蘋果汁")
    print("2.柳橙汁")
    print("3.葡萄汁")
    print("4.系統關閉")
    ans = input("請輸入編號編號:")
    x = int(input("請輸入數字:"))
    if ans == 1:
        print("您點的商品是蘋果汁")
    elif ans == 2:
        print("您點的商品是柳橙汁")
    elif ans == 3:
        print("您點的商品是葡萄汁")
    elif ans == 4:
        print("系統關閉")
        break
    else:
        print("輸入錯誤查無此果汁,請重新輸入輸入錯誤查無此果汁,請重新輸入")
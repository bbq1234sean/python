juice_list = ["蘋果汁", "柳橙汁", "葡萄汁", "系統關閉"]
L = [1, 2, 3, 4]
while True:

    ans = input("請輸入編號:")

    for i in L[1:4]:
        if ans == i:
            print(juice_list[i - 1])
            break
        print(L)

    else:
        print("輸入錯誤查無此果汁,請重新輸入輸入錯誤查無此果汁,請重新輸入")
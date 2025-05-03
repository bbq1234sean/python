# 迴圈的 break 可以用來跳出所屬的迴圈,所以判break屬於哪個迴圈時必須注意縮排
# 例如:

for i in range(5):
    for j in range(5):
        if i == 2 and j == 2:
            break
        print(f"i: {i}, j: {j}")
# 這裡的 break 只會跳出內層的 for 迴圈,外層的 for 回圈還是會繼續執行


print("1.蘋果汁")
print("2.柳橙汁")
print("3.葡萄汁")
print("4.系統關閉")
while True:
    print("1.蘋果汁")
    print("2.柳橙汁")
    print("3.葡萄汁")
    print("4.系統關閉")
    ans = input("請輸入編號編號:"))
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

# continue
# 當 for 迴圈正常結束時, 執行 continue 區塊的程式
# EX:
for i in range(5):
    if i == 2:
        continue
    print(i)
# 這裡的 continue 會跳過 i = 2 的那次迴圈接執行 i = 3 的那次迴圈
# 所以輸出的結果是 0, 1, 2, 3, 4
# continue 也可以用在 while 迴圈中
# ex:
i = 0
while i < 5:
    if i == 2:
        continue
    print(i)
    i = i + 1
# continue 也要判斷所屬的迴圈所以要注意縮排

a = int(input("請輸入跳繩次數:"))
for i in range(1, a + 1):
    if i % 10 == 0:
        print("休息一下")
        continue
    print(f"第 {i} 次跳繩")
    
    



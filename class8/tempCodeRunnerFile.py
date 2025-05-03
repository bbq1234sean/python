a = int(input("請輸入跳繩次數:"))
for i in range(1, a + 1):
    if i % 10 == 0:
        print("休息一下")
        continue
    print(f"第 {i} 次跳繩")
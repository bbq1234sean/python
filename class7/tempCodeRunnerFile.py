start = int(input("請輸入開始的整數:"))
end = int(input("請輸入結束的整數:"))
for n in range(start,end + 1):
    if n > 1:
        ans ="是質數"
        for i in range(2,n):
            if n % i == 0:
                ans = "不是質數"
            if ans == "是質數":
                print(n)
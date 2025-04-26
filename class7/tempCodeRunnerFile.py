import time

f = int(input("請輸入秒數 :"))
for i in range(f, -1, -1):
    print(i)
    time.sleep(1)
else:
    print("time up")
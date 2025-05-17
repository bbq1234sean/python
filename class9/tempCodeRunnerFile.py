import random
u = 100
l = 0
a = random.randrange(1, 101)
x = int(input("請輸入1-100的整數 :"))
while True:
    
    if x < a:
        l = x
        print("再大一點")
        x =  int(input("請輸入" + str(l) + "~" + str(u) + "的整數:"))
        continue
    elif x > a:
        u = x
        print("再小一點")
        x =  int(input("請輸入" + str(l) + "~" + str(u) + "的整數:"))
        continue
    else:
        print("恭喜猜中")
        break
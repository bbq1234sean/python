import random  # 這是隨機模組

# random.randrange  設定範圍方式跟 range 一樣,特性也一樣不包含最後一個數字
# random.randrange  的功能是隨機取得一個數字, range 式產生一組數字
print(random.randrange(10))  # 從0-9取得一個數字
print(random.randrange(1, 10))  # 從1-9取得一個數字
print(random.randrange(1, 10, 2))  # 從{1,3,5,7,9}取得一個數字

# random.randint 取得整數
# 不能跳字抽籤
print(random.randint(1, 10))  # 從1-10取得一個數字

import random as r

a = r.randrange(1, 101)
while True:
    x = int(input("請輸入1-100的整數 :"))
    if x == a:
        print(f"{x} 恭喜猜中")
        break
    elif x < a:
        print(f"{x} 再大一點")
    elif x > a:
        print(f"{x} 再小一點")

# list 清單
# list 可以存入很多資料, 每個資料都要使用`,`分隔
# list 可以存入不同型態的資料
# list 最外層用`[]`包起來
L = [1, 2, 3, 4, 5]  # 數字
print(L)
# 不同型態混和
L = [1, 2, "3", 4, 5, "hello", ["world", 6]]  # 數字,字串,清單
print(L)

# list 取值
# list 取值方式跟字串一樣用`[]`取值
# list 取值方式跟字串一樣用`[:]`取值
# list 當資料的編號(index)都從零開始
l = [1, 2, 3, 4, 5]
print(l[0])  # 取得第1個值
print(l[1])  # 取得第2個值
print(l[2])  # 取得第3個值

# list 取值的方式跟字串一樣,也可以用［:]取值
# 設定範圍的方式跟range很像還最後一個數字
print(l[1:4:2])  # 取得第2到第4個值,每2個值
print(l[0:3])  # 取得第1到第3個值
print(l[:3])  # 取得第1到第3個值
print(l[3:])  # 取得第4到最後的值
print(l[:])  # 取得所有值

# list len 列表長度
L = [1, 2, 3, 4, 5]
print(len(L))  # 取得list長度,也就是list當中有幾筆資料

# 務必不要跟list混淆,  index式資料的編號,len是資料數量

# len 可以搭配 for 迴圈使用來取得list當中的資料
for i in range(len(L)):  # 這邊的i是index
    print(L[i])

for i in L:  # 這邊的i是資料
    print(i)

# 要使用哪一種方式讀取list當中的資料,要看使用的情境當中會不會需要index

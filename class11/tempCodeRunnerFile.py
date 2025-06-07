print("購物清單:")
print("目前清單是空的!")
L = []
while True:
    print(L)
    print("1. 新增東西2. 修改東西3. 刪除東西4. 離開程式")
    t = input("請輸入你的選擇(1-4):")
    if t == "1":
        print("新增選單： a. 加到尾 b. 插入指定位置")
        a = input("請選擇方法(a,b):")
        s = input("請輸入新增的商品名稱:")
        if a == "a":
            L.append(s)
            print(s + "已加入清單")
        elif a == "b":
            i = input("請輸入新增的商品位置:")
            L.insert(i)
            print(s + "已加入清單")
    elif t == "2":
        a = int(input("請輸入要修改的物品編號(0是第一個):"))
        s = input("請輸入新的商品名稱:")
        L[a] = s
        print(s + "已修改清單")
    elif t == "3":
        a = input("刪除選單：a. 依名稱刪除 b. 依位置刪除")
        if a == "a":
            s = input("請輸入要刪除的商品名稱:")
            L.remove(s)
            print(s + "已刪除清單")
        elif a == "b":
            i = input("請輸入要刪除的商品位置:")
            L.pop(i)
            print(s + "已刪除清單")
    elif t == "4":
        break
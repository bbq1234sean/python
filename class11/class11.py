# 複製 List,避免原本List被更動
L = ["hello", "world"]  # 使用copy()複製List
L2 = L.copy()  # 使用copy()複製List
print(L2)  # ['hello', 'world']
L2[0] = "python"  # 修改複製的List
print(L)  # ['hello', 'world']# 原本的List不會被更動
print(L2)  # ['python', 'world']# 只有複製List被改變
# 這個變數的=負職不同,一般情況下會開2記憶體空間
# 在List情況下使用=會讓兩個變數名稱指向同一個記憶體
# 這導致修改一個List 會引想到另一個List
# 所以需要複製List時,應該使用 copy()方法所以需要複製List時,應該使用 copy()方法


# remove 移除 lIST中的元素
L = ["hello", "world", "python"]
L.remove("world")  # 移除"world"
print(L)  # ['hello', 'python']


# POP移除並回傳 lIST中的元素移除並回傳 lIST中的元素
L = ["hello", "world", "python"]
# 不給索引時,pop()會移除最後一個
L.pop()  # 移除最後一個元素
print(L)  # ['hello', 'world']
s = L.pop(1)  # 移除索引1的元素,並回傳該職
print(s)  # World
print(L)  # ['hello']


"""
你是一位「購物小幫手」！幫媽媽記下要買的東西，還能修改、刪除，或是看看清單裡有什麼。
📋 你可以做這些事：
程式會在每一步自動顯示目前的購物清單。
1️⃣ 新增東西
    ➕ 加到清單最後（append）
    📌 新增到清單中的某個位置（insert）
2️⃣ 修改東西
    ✏️ 輸入編號，換掉舊項目
3️⃣ 刪除東西
    ❌ 用名稱刪除（remove）
    🗑️ 用位置刪除（pop）
4️⃣ 離開程式
    👋 不想逛了就回家！
    """

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

# index :尋找指定元素 List 中第一次出現位置
# 如果元素不存在會產生錯誤,所以使用前建議先檢查元素是否存在
L = [1, 2, 3, 4, 5]
print(L.index(3))  # 找到數字3 再索引位置1

# count：統計某個元素在List中總共出現了幾次
# 這個方法很適合用來檢查重複資料的數量
L = ["Hello", "World", "Python", "Hello"]
print(L.count("Hello"))  # "Hello"這個字串總共出現了2次

# sort：將List中的元素進行排序，預設是由小到大 (昇序排列)
# 注意：這個方法會直接修改原本的List，不會產生新的List
L = [1, 2, 3, 4, 5]
L.sort()
print(L)

# sort(reverse=Ture)：將List中的元素由大到小排序 (降序排序)
# reverse=True 參數可以讓排序結果相反
L = [1, 2, 3, 4, 5]
L.sort(reverse=True)
print(L)

# reverse：將List中的元素順序完全顛倒
# 這不是排序! 只是把第一變到最後一個,最後變到第一個
L = [1, 2, 3, 4, 5]
L.reverse()
print(L)

# List和字串有很多相似的操作方式
# 我們可以像操作字串依樣來處理List

# 合併兩個List: 使用 + 運算子將兩個List連結再一起
# 這會產生一個全新的List,原本的List不會被改變
L1 = [1, 2, 3]
L2 = [4, 5, 6]
L3 = L1 + L2  # 把L1和L2合併成一個新的List
print(L3)

# 重複List中的內容: 使用 * 運算子讓List內容重複多次
# 這在需要建立重複資料時很有用
L = [1, 2, 3]
L = L * 3  # 讓List內容重複3次
print(L)

# 不同資料型態之間的轉換技巧
print(range(10))  # range物件本身看不到具體內容,只是一個範圍描述
print(list(range(10)))  # 使用List()將range轉換成可以看到內容的List
print(list("Hello"))  # 將字串轉換成List, 每個字元都會變成獨立的元素

# split：將一個完整的字串按照指定的分隔符號切割成多個部分
# 這是處理文字資料時非常常用的方法
S = "Hello World"
L = S.split(" ")  # 以空白字元作為分隔點來切割字串
print(L)
calendar = "2020/12/25"
L = calendar.split("/")  # 以斜線做為分割點來切割日期字串
print(L)

# join：將List中的多個字串元素合併成一個完整的字串
# 可以指定要用什麼符號來連接這些元素
L = ["Hello", "World"]
S = " ".join(L)  # 用空白字元將List中的元素連接成一個字串
print(S)

birthday = "2020/10/20"
birthday = birthday.split("/")
birthday = "-".join(birthday)  # 將字串元素連接成一個字串
print(birthday)

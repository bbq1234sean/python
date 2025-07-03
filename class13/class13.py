# 字典(Dictionary): 用來儲存[key-value]配對的資料結構
# 字典很適合用來表示有對應關係的資料,像是商品和價格的對應

# 建立字典:使用大括號 {} , key和value之間用冒號 : 分隔
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print(d)

# 從字典中取得特定key相應的value
# 如果key不存在會產生KeyError錯誤
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print(d["蘋果"])
# print(d["梨子"]) # 這行會產生KeyError:'梨子'錯誤

for food in d:
    print(food)
    print(d[food])

# 遍歷字典: 有多種方式可以有走訪字典中的資料
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}

# 方式一: 直接遍歷字典, 會取得所有的key
for k in d:
    print(k)  # 印出key名稱
    print(d[k])  # 用key來取得對應的value

# 方式二: 明確使用keys()方法來取得所有key
for k in d.keys():
    print(k)  # 印出key名稱
    print(d[k])  # 用key來取得對應的value

# 方式三: 使用values()方法來取得所有value
for v in d.values():
    print(v)  # 直接印出value,但不知道對應的key是什麼

# 方式四: 使用items()方法同時取得key和value
# 這是最常用的方式,因為可以同時存取key和value
for k, v in d.items():
    print(f"{k}:{v}")  # 同時印出key和value的配對關係

# 新增/修改字典的內容
# 直接指定key對應一個value, 如果key已存在就是修改, 如果key不存在就是新增
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
d["蘋果"] = 10  # 修改[蘋果]對應的value
print(d)
d["蓮霧"] = 15  # 新增一個key-value配對
print(d)

# 刪除字典的內容
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
d.pop("蘋果")  # 刪除[蘋果]
# 如果要刪掉的key不存在, 會出現keyError, 所以可以加上第二個參數, 當key不存在時, 不會有任何變化
popitem = d.pop("蓮霧", "不存在這筆資料")  # 不會有任何變化
print(d)  # {'香蕉':30, '橘子':25}
print(popitem)  # 不存在這筆資料

# len: 取得字典中有多少組key-value配對
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print(len(d))

# 檢查某個key是否存在於字典中
# 使用前先檢查可以避免keyError錯誤
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print("蘋果" in d)  # True, 蘋果這個key存在
print("蓮霧" in d)  # False, 蓮霧這個key不存在

# 檢查某個元素有沒有在list中
# 使用in可以快速檢查某格元素是否在於list中
L = [1, 2, 3, 4, 5]
print(3 in L)  # True, 3在list中

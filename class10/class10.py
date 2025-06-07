# append 在執行的過程當中可以將資料加入道列表的最後面
L = ["hello", "world"]
L.append("python")  # 加入資料
print(L)  # ['hello', 'world', 'python']

# insert 在執行的過程當中可以將資料加入道列表的指定位置
L = ["hello", "world"]
L.insert(1, "python")  # 在索引1的地方加入道列表的指定位置
print(L)  # ['hello', 'python', 'world']

# 修改特定位置定位置的資料
L = ["hello", "world"]
L[1] = "python"  # 修改特定位置定位置的資料
print(L)  # ['hello', 'python', 'world']

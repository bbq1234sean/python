# def
# 新增一個函數要用def開頭, 後面接著函數名稱, 再加上小括號,最後加上冒號
# 小括號面可以放入傳入函數的參數也可以不放
def hello():
    print("Hello World")


for i in range(10):
    hello()


# 有傳入參數的函數
# 這個函數有一個參數 name, 當呼叫這個函數十,可傳入一筆資料給name
def hello(name):
    print(f"Hello, {name}")


hello("Alice")
hello("Bob")
hello("Charlie")
for i in range(10):
    hello(i)  # 這裡的i 會被當作name的值


# 有回傳值的函數
# 這個函數回傳一個值，當呼叫這個函數時，可以把回傳的值存起來
# 在指令當中只要執行return, 就會回傳值,並結束函數
def add(a, b):  # 可以允許多個傳入參數
    return a + b


print(add(1, 2))
print(add("Hello", "World"))
sum = add(3, 4)  # 可將回傳值存到變數中
print(sum)


# 有多個回傳值的函數
# 這個函數會回傳兩個值,當呼叫這個函數時, 可以把回傳的值存起來
def add_sub(a, b):
    return a + b, a - b


sum, sub = add_sub(5, 6)  # 可以將回傳值存到多個變數中
print(f"sum:{sum}, sub:{sub}")


# 多個return
def add_sub(a, b):
    if a > b:
        return a + b
    else:
        return a - b


print(add_sub(5, 6))
print(add_sub(6, 5))


# 預設參數
# 可以在函數的參數中設定參數,當呼叫這個函數時,如果沒有傳入參數, 就會使用預設值
# 多個參數時,有預設值的參數要放在沒有預設值的參數後面
def hello(name, message="Hello World"):
    print(f"{message}:{name}")


# 如果是def hello(message="Hello", name) 會出錯, 因為有預設值的參數要放在沒有預設值的參數後面
hello("Alice")
hello("Bob", "Good morning")


# 限制傳入參數型態
# 可以在函數的參數中設定型態, 當呼叫這個函數時, 可以提示使用者要傳入的參數型態
# 變數: 型態=預設值
# -> 型態,代表回傳值的型態
def add(a: int, b: int) -> int:
    return a + b


print(add(1, 2))
print(add("Hello", "World"))


# def 區域變數和全域變數
length = 5  # 全域變數


def calculate_square_area():
    area = length**2  # length 是全域變數, area 是區域變數
    # length = length +1 # 這行會出錯
    # 因為在函數內部length 是區域變數, 所以不能直接修改全域變數
    print("面積是", area)


calculate_square_area()
# print("長度是", area) # 這行會出錯, 因為area是區域變數, 只能在函數內使用

length = 5  # 全域變數


def calculate_square_area():
    area = length**2  # length 是全域變數, area 是區域變數
    print("面積是", area)

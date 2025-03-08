# 字串運算
a = "hello"
b = "world"
c = a + "" + b  # 字串相加
print(c)

a = a * 3  # 字串乘法
print(a)

# 認識基本指令
# 指令會有名稱跟括號組成，()裡面放題給給指令的參數
# 每個參數都要用逗號隔開
m = max(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # 最大值

le = len("hello")  # 字串長度
print(le)

# type()取得參數的型態
print(type(1))  # 取型態
print(type("hello"))  # 取型態
print(type(True))  # 取型態
print(type(1.1))  # 取型態

# 型態轉換
# int() 轉換成整數
# float() 轉換成浮點數
# str() 轉換成字串
# bool() 轉換成布林值

print(int("123"))  # 123
print(int(123.99999))  # 123
print(int(True))  # 1
print(int(False))  # 0
print(
    "----------------------------------------------------------------------------------------------------"
)

print(float("123.456"))  # 123.456
print(float(123))  # 123.0
print(float(True))  # 1.0
print(float(False))  # 0.0
print(
    "----------------------------------------------------------------------------------------------------"
)

print(str(123))  # 123
print(str(123.456))  # 123.456
print(str(True))  # True
print(str(False))  # False
print(
    "----------------------------------------------------------------------------------------------------"
)

print(bool(123))  # True
print(bool(0))  # False
print(bool(-1))  # True
print(bool(""))  # False
print(bool("0"))  # True

# input() 讓使用者在中端端機輸入資料
# input() 的括弧括弧內可以放入"提示字串"
a = input("請輸入數字:")
# 透過 input() 取得的資料型態是 str
print(a + "123")  # 字串相加
print(int(a) + 1)  # 整數相加

# 運算子
print(1 + 1)  # 相加
print(1 - 1)  # 相減
print(1 * 1)  # 相乘
print(1 / 1)  # 相除
print(1 // 1)  # 取整除數
print(1 % 1)  # 取餘數
print(1**1)  # 次方

# 計算優先順序
# 1. ()
# 2. **次方
# 3. * / // %
# 4. + -

# 正方形面積計算
r = input("請輸入正方形邊長:")
print(r**2)
area = r * 2
print(f"正方形的面積為{area}")

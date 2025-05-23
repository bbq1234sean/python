# while 迴圈
# 這是條件式迴圈,當條件成立時,才會執行
i = 1
while i < 10:
    # 當i小於10時,才會執行
    print(i)
    i = i + 1

# 算術指定運算子
# +=, -=, *=, /=, %=, **=, //=
# x = x + 1 等於x += 1
# x = x - 1 等於x -= 1
# x = x * 1 等於x *= 1
# x = x / 1 等於x /= 1
# x = x % 1 等於x %= 1
# x = x ** 1 等於x **= 1
# x = x // 1 等於x //= 1

# 符號優先順序
# 1. () 先執行括號內的運算式
# 2. ** 次方
# 3. + - 加減
# 4. * / // % 多餘運算
# 5. + - 正負號
# 6. == != > < >= <= 小於大於等於
# 7. and or not 邏輯運算子
# 8. = += -= *= /= //= %= **=

i = 1
while i < 10:
    print(i)
    i = i + 1  # 等於i += 1


user_input = ""
while user_input != "1qaz":
    user_input = input("請輸入密碼:")
print("密碼正確")

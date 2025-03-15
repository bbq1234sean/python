# try except
# 錯誤處理
try:
    # 嘗試執行可能會出錯的程式碼
    n = int(input("input a number:"))

except:
    # 如果有錯誤發生,執行這段程式碼
    print("you should input a number")

else:
    # 如果沒有錯誤發生,執行這段程式碼
    print(n + 1)


try:
    h = float(input("請輸入你的身高:"))
    w = float(input("請輸入你的體重:"))
    bmi = w / h**2
    print(f"你的BMI為: {bmi}")
except:
    print("請輸入有效的數字")


# 比較運算子
print(1 == 1)  # True, 1 等於 1
print(1 != 1)  # False, 1 不等於 1
print(1 > 1)  # False, 1 大於 1
print(1 < 1)  # False, 1 小於 1
print(1 >= 1)  # True, 1 大於等於 1
print(1 <= 1)  # True, 1 小於等於 1

# 邏輯運算子
# and 代表全部條件成立才會回傳True
# or 代表其中一個條件成立才會回傳True
# not 代表將原布林值值反轉

print(True and True)  # True, True和True
print(True and False)  # False, True和False
print(False and False)  # False, False和False
print(True or True)  # True, True和True
print(True or False)  # True, True和False
print(False or False)  # False, False和False
print(not True)  # False, not True
print(not False)  # True, not False

# if
pwd = input("請輸入密碼:")

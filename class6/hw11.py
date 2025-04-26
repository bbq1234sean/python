total = 0
user_input = input("請輸入金額 :")
while user_input != "0":
    total = total + int(user_input)
    print("目前總金額 :", total)
    user_input = input("請輸入金額 :")

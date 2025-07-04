fruits = {"蘋果": 25, "香ㄅ蕉": 20, "橘子": 30}

print("=== 水果店價格查詢系統 ===")

while True:
    print("目前水果價格:")
    for fruit, price in fruits.items():
        print(f"{fruit}:{price}元")

    print("1. 新增水果價格")
    print("2. 修改水果價格")
    print("3. 刪除水果價格")
    print("4. 離開系統")

    choice = input("請選擇功能 (1~4):")
    print("=" * 26)

    if choice == "1":
        fruit_name = input("請輸入要新增的水果名稱:")
        if fruit_name in fruits:
            print("水果名稱已存在!")
        else:
            new_price = int(input(f"請輸入{fruit_name}的價格:"))
            fruits[fruit_name] = new_price
            print(f"{fruit_name}已新增,價格{price}元")

    elif choice == "2":
        fruit_name = input("請輸入要修改的水果名稱:")
        if fruit_name in fruits:
            new_price = int(input(f"請輸入{fruit_name}的新價格:"))
            fruits[fruit_name] = new_price
            print(f"{fruit_name}已修改,價格{new_price}元")
        else:
            print("查無此水果!")

    elif choice == "3":
        fruit_name = input("請輸入要刪除的水果名稱:")
        if fruit_name in fruits:
            fruits.pop(fruit_name)
            print(f"{fruit_name}已刪除")
        else:
            print("查無此水果!")
    elif choice == "4":
        print("感謝使用水果店價格查詢系統!")
        break

    else:
        print("輸入錯誤,請選擇1~4!")

    print("=" * 26)

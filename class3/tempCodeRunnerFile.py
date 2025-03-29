try:
    grade = int(input("請輸入你的考試成績:"))
except:
    print("you should input a number")
    exit()

if grade >= 90:
    print("A")
elif grade >= 80 and grade < 90:
    print("B")
elif grade >= 70 and grade < 80:
    print("C")
elif grade >= 60 and grade < 70:
    print("D")
else:
    print("E")
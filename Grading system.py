a = int(input("Enter marks: "))

if a >= 90:
    print("grade: A+")
elif a >= 80 and a < 90:
    print("grade = A")
elif a >= 75 and a < 80:
    print("grade = B+")
elif a >= 70 and a < 75:
    print("grade = B")
elif a >= 50 and a < 70:
    print("grade = C")
elif a >= 34 and a < 50:
    print("grade = D")
else:
    print("fail")

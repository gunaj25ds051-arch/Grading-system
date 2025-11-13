# Grading-system
📝 Program Explanation
a = int(input("Enter marks: "))


Takes marks as input from the user (must be a number between 0–100).

🧮 Grading Logic
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


The program checks the entered marks and prints a grade:

Marks Range	Grade
90 and above	A+
80–89	A
75–79	B+
70–74	B
50–69	C
34–49	D
Below 34	Fail
✅ Example Output
Enter marks: 82
grade = A

marks = [85, 90, 78, 88, 92]

percentage = sum(marks) / len(marks)

print("Percentage:", percentage)

if percentage >= 90:
    print("Grade: A")
elif percentage >= 75:
    print("Grade: B")
else:
    print("Grade: C")

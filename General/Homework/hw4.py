#Jlouzada .. This script asks user for grade from 0-100 and displays proper letter grade

score = int(input("What is your score?: "))
#Verify that user input meets criteria
while score < 0 or score > 100:
    print("Please input score 0 - 100")
    score = int(input("What is your score?: "))
if score >= 95:
    grade = "A"
elif score < 95 and score >= 90:
    grade = "A-"
elif score >= 85 and score < 90:
    grade = "B"
elif score >=80 and score <85:
    grade = "B-"
elif score >= 75 and score <80:
    grade = "C"
elif score >= 70 and score < 75:
    grade = "C-"
elif score >= 65 and score < 70:
    grade = "D"
elif score >= 60 and score < 65:
    grade = "D-"
print("Your grade is", grade)                

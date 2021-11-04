BBcyber = float(input("Enter BBcyber's scores here: "))
Total_mark = int(input(" Enter the total scores of the course here: "))
class_score = []

student_num = int(input("enter number of other students in class excluding BBcyber here: "))


for i in range(1,student_num+1):
    student = float(input("Student_score {}: ".format(i)))
    class_score.append(round((student/Total_mark)*100,0))

class_score.append(BBcyber)
avg_score = round((sum(class_score)/len(class_score)),0)

print(class_score)
print("The average score of the class is :",avg_score,"%")
if BBcyber >= (avg_score-5):
    print("passed")

else:
    print("E b for you BBcyber")
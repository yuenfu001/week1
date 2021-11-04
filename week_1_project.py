# The student to be evaluated
BBcyber = float(input("Enter BBcyber's scores here: "))

# The total mark of the Course
Total_mark = int(input("Enter the total scores of the course here: "))

# a python list to take all the student scores taking the course
class_score_list = []

# This will take the number of students taking the course excluding the evaluated student
student_num = int(input("enter number of other students in class excluding BBcyber here: "))

# a loop to check the student_num starting from index number 1 then add 1 to the student_num
for i in range(1,student_num+1):
    #This is take in the scores of the rest of the students taking the course
    student = float(input("Student_score {}: ".format(i)))
    # this takes in the students score excluding the Evaluated student, convert it into percentage and insert them in the class_score_list
    class_score_list.append(round((student/Total_mark)*100,0))

#this appends the evaluated student to the list
class_score_list.append(BBcyber)
# the avg_score will take the average of all the students in the updated class_score_list
avg_score = round((sum(class_score_list)/len(class_score_list)),0)

print(class_score_list)
print("The average score of the class is :",avg_score,"%")

#This is a condition that if the evaluated student is 5 points less than the average score and if he has 60 points
#meaning if both conditions are true then it is a pass else fail
if BBcyber >= (avg_score-5) and BBcyber >= 60:
    print("passed")

else:
    print("Olodo")
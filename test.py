n = int(input("Enter Total Class here: "))
total_mark = int(input("Enter Total mark of course here: "))
# d=dict(input("Enter name and score with space between them").split(" ") for x in range(n))
dict1 ={}
for a in range(1,n+1):
    keys = input("Enter  Student {}'s name here: ".format(a))
    values = float(input("Enter Student {}'s scores here: ".format(a)))
    dict1[keys] = values
percent = [(x/total_mark)*100 for x in dict1.values()]
print(percent)
avg_scores = sum(percent)/len(percent)

print("Average score is : ", round(avg_scores,1))
print ("{:<25} {:<10} {:<10}(%) {:<10}".format("Name","Score", "Percentage","Comments"))
for i in range(0, len(dict1.items())):
    p = percent[i]
    name, score = list(dict1.items())[i]
    comments = "Passed" if p >=60 and p >= (avg_scores-5) else "Failed like an olodo"
    print ("{:<25} {:<10} {:<13} {:<10}".format(name, score, round(p,0), comments))
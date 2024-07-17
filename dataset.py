from tabulate import tabulate
column=['stdid','stdname','standard','Age','Hindi','English','Maths','Science','Computer','Total']
students=[['std101','Ashish kumar','10th',15,67,89,87,89,90,422],
          ['std102','Abhishek Kumar','10th',14,85,45,48,90,45,313],
          ['std103','Aman','10th',15,23,56,78,78,67,302],
          ['std104','Rahul','10th',14,45,67,45,45,56,258],
          ['std105','Ruby','10th',13,89,67,89,93,65,403],
          ['std106','Suman','10th',13,90,46,67,67,67,337],
          ['std107','saurabh','10th',15,45,23,34,45,34,181],
          ['sts108','Sumit','10th',14,23,45,67,78,90,303],
          ['std109','Kamlesh','10th',15,45,56,78,99,67,345],
          ['std110','Rohan','10th',15,34,12,24,45,56,171]]
table=tabulate(students[0:],headers=column,tablefmt='grid')
print("Data is",table)
print("Those Students whose Marks in english is greater than 50")
for row in students:
    if(row[5]>50):
        print(row[1])
print("\n")
print("Name and age those student Who are the top 4 score of Maths")
score=sorted(students, key=lambda row: row[6], reverse=True)
for i in range(0,4):
    print(score[i][1]," ",score[i][3])
print("\n")
print("Name , age and id those student Who are the top 4 scorer of English")
score=sorted(students, key=lambda row: row[8], reverse=False)
for i in range(0,4):
    print(score[i][0]," ",score[i][1]," ",score[i][5])


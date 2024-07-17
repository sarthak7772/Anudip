from tabulate import tabulate
data={
    1:{'stdid': 'sid101', 'sidname': 'ashish kumar', 'standard': '10th', 'age': 15, 'hindi': 67, 'english': 89, 'math': 87, 'science': 89, 'computer': 90,'total': 422},
    2:{'stdid': 'sid102', 'sidname': 'abhishek kumar', 'standard': '10th', 'age': 14, 'hindi': 85, 'english': 45, 'math': 48, 'science': 90, 'computer': 45,'total': 313},
    3:{'stdid': 'sid103', 'sidname': 'aman', 'standard': '10th', 'age': 15, 'hindi': 23, 'english': 56, 'math': 78, 'science': 78, 'computer': 67, 'total': 302},
   4:{'stdid': 'sid104', 'sidname': 'rahul', 'standard': '10th', 'age': 14, 'hindi': 45, 'english': 67, 'math': 45, 'science': 45, 'computer': 56, 'total': 258},
    5:{'stdid': 'sid105', 'sidname': 'ruby', 'standard': '10th', 'age': 13, 'hindi': 89, 'english': 67, 'math': 89, 'science': 93, 'computer': 65, 'total': 403},
    6:{'stdid': 'sid106', 'sidname': 'suman', 'standard': '10th', 'age': 13, 'hindi': 90, 'english': 46, 'math': 67, 'science': 67, 'computer': 67, 'total': 337},
    7:{'stdid': 'sid107', 'sidname': 'saurabh', 'standard': '10th', 'age': 15, 'hindi': 45, 'english': 23, 'math': 34, 'science': 45, 'computer': 34, 'total': 181},
    8:{'stdid': 'sid108', 'sidname': 'sumit', 'standard': '10th', 'age': 14, 'hindi': 23, 'english': 45, 'math': 67, 'science': 78, 'computer': 90, 'total': 303},
    9:{'stdid': 'sid109', 'sidname': 'kamlesh', 'standard': '10th', 'age': 15, 'hindi': 45, 'english': 56, 'math': 78, 'science': 99, 'computer': 67, 'total': 345},
    10:{'stdid': 'sid110', 'sidname': 'rohan', 'standard': '10th', 'age': 15, 'hindi': 34, 'english': 12, 'math': 24, 'science': 45, 'computer': 56, 'total': 171}
}
# column=['stdid', 'sidname', 'standard', 'age', 'hindi', 'english', 'math', 'science', 'computer', 'total']
table=tabulate(data.values(),headers={'stdid': 'stdid', 'sidname': 'sidname', 'standard': 'standard', 'age': 'age', 'hindi': 'hindi', 'english': 'english', 'math': 'math', 'science': 'science', 'computer': 'computer', 'total':'total'},tablefmt='grid'
            )
print(table)

print('--------------------------------------------------------------------------\n')
print("name of those students who has english marks greater than 50")
for i,j in data.items():
    if (j["english"] > 50):
        print(j["sidname"])
        
print('----------------------------------------------------------\n')
score=sorted(data.values(), key=lambda row: row['math'], reverse=True)
top=score[:4]
for i in top:
    print(i['sidname']," ",i['age'])
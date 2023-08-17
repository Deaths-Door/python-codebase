students = []
n = int(input())
for _ in range (n) :
    roll = int(input())
    name = input()
    branch = input()
    students.append({
        "roll-no" : roll,
        "name" : name,
        "branch" : branch
    })
print(students)
employees = [
   {"name": "Rahul", "salary": 25000},
   {"name": "Amit", "salary": 35000},
   {"name": "Priya", "salary": 30000}
]

highest = None
second_highest = None

for emp in employees:
    salary = emp["salary"]

    if highest is None or salary > highest["salary"]:
        second_highest = highest
        highest = emp

    elif salary < highest["salary"]:
        if second_highest is None or salary < second_highest["salary"]:
            second_highest = emp

print("Highest Salary:", highest)
print("Second Highest Salary:", second_highest)


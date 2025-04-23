data = [
    {"dept_no": 101, "emp_roll_no": 1, "salary": 50000},
    {"dept_no": 102, "emp_roll_no": 2, "salary": 60000},
    {"dept_no": 101, "emp_roll_no": 3, "salary": 45000},
    {"dept_no": 102, "emp_roll_no": 4, "salary": 70000},
    {"dept_no": 101, "emp_roll_no": 5, "salary": 52000}
]

result = {}

for record in data:
    dept = record["dept_no"]
    salary = record["salary"]
    if dept not in result:
        result[dept] = {"min": salary, "max": salary}
    else:
        result[dept]["min"] = min(result[dept]["min"], salary)
        result[dept]["max"] = max(result[dept]["max"], salary)

print(result)
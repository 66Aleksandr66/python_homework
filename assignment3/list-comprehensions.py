#Task 3
import csv

with open("../csv/employees.csv", 'r', newline='') as employees_table:
    employees = list(csv.reader(employees_table))
    first_indx = employees[0].index("first_name")
    last_indx = employees[0].index("last_name")
full_name = [row[first_indx] + ' ' + row[last_indx] for row in employees[1:]]
filter_list = [x for x in full_name if 'e' in x]
print(full_name)
print(filter_list)

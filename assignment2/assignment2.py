import os
import csv
import traceback
import sys
import custom_module
from datetime import datetime
# Task 2
def read_employees():
    string = []
    my_dict = {}
    try:
        with open("../csv/employees.csv", 'r', newline='') as employees_table:
            reader = csv.reader(employees_table)
            header = next(reader)
            my_dict["fields"] = header
            for row in reader:
                string.append(row)
        my_dict["rows"] = string
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        sys.exit(1)
    return my_dict

employees = read_employees()
print(employees)

# Task 3
def column_index(search_str):
    return employees["fields"].index(search_str)
employee_id_column = column_index("employee_id")
# Task 4
def first_name(index_string):
    index_column = column_index("first_name") # результат index first name индекс колонки
    return employees["rows"][index_string][index_column]
# Task 5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return matches
# Task 6
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches
# Task 7
def sort_by_last_name():
     employees["rows"].sort(key = lambda row: row[column_index("last_name")])
     return employees["rows"]
sort_by_last_name()
# Task 8
def employee_dict(row_string):
    new_dict = dict(zip(employees["fields"], row_string))
    del new_dict["employee_id"]
    return new_dict
print(employee_dict(employees["rows"][0]))
# Task 9
def all_employees_dict():
    my_dict={}
    for row in employees["rows"]:
        my_dict[row[employee_id_column]] = employee_dict(row)
    return my_dict
print(all_employees_dict())
# Task 10
def get_this_value():
    return os.getenv("THISVALUE")
print(get_this_value())
# Task 11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
# Task 12
def dry(path):
    rows = []
    my_dict = {}
    try:
        with open(path, 'r', newline='') as minutes1_table:
            reader = csv.reader(minutes1_table)
            header = next(reader)
            my_dict['fields'] = header
            for row in reader:
                rows.append(tuple(row))
        my_dict["rows"] = rows
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        sys.exit(1)
    return my_dict
def read_minutes():
    minutes1 = dry("../csv/minutes1.csv")
    minutes2 = dry("../csv/minutes2.csv")
    return minutes1, minutes2
minutes1, minutes2 = read_minutes()

print(read_minutes())

# Task 13
def create_minutes_set():
    return set(minutes1["rows"]).union(set(minutes2["rows"]))
minutes_set = create_minutes_set()

# Task 14
def create_minutes_list():
    return list(map(lambda x:(x[0], datetime.strptime(x[1], "%B %d, %Y")),list(minutes_set)))
minutes_list = create_minutes_list()

# Task 15
def write_sorted_list():
    minutes_list.sort(key = lambda row : row[1])
    result = list(map(lambda x :(x[0],datetime.strftime(x[1], "%B %d, %Y")), minutes_list))
    try:
        with open("./minutes.csv", 'w', newline='') as result_minutes_table:
            writer = csv.writer(result_minutes_table)
            writer.writerow(minutes1["fields"])
            writer.writerows(result)
    except Exception as e:
            trace_back = traceback.extract_tb(e.__traceback__)
            stack_trace = list()
            for trace in trace_back:
                stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
            print(f"Exception type: {type(e).__name__}")
            message = str(e)
            if message:
                print(f"Exception message: {message}")
            print(f"Stack trace: {stack_trace}")
            sys.exit(1)
    return result
print(write_sorted_list())
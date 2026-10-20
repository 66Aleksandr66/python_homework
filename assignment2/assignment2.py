import csv
import traceback
import sys
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
# print(employees)

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
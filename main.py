import department
import employee

class Main(object):

    def __init__(self):
        self.employees = []
        self.departments = []

    def read_emp_from_db(self, filename):
        file = open(filename, "r")
        employee_row_data = file.readlines()
        for line in employee_row_data:
            words = line.split()
            print(words)




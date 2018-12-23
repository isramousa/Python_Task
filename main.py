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
            emp = employee.Employee()
            emp.empName = words[0]
            emp.empPhoneNumber = words[1]
            emp.empId = words[2]
            emp.empDOB = words[3]
            emp.empPosition = words[4]
            emp.empManagerId = words[5]
            emp.empDepartmentId = words[6]
            self.employees.append(emp)

    def read_department_from_db(self, filename):

        defile = open(filename, "r")
        department_row_data = defile.readlines()
        for line in department_row_data:
            words = line.split()
            dep = department.Department()
            dep.managerId = words[0]
            dep.departmentId = words[1]
            dep.departmentName = words[2]


    if __name__ == '__main__':
        main = Main()
        main.read_emp_from_db()
        main.read_department_from_db()

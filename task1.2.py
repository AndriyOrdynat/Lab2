class Employee:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def __str__(self):
        return f"{self.name} {self.surname}"
    
class Office(Employee):
    def __init__(self):
        self.employees = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def sort_employees(self):
        empl_num = len(self.employees)
        for i in range(empl_num):
            for j in range(0, empl_num - i - 1):
                if self.employees[j].surname > self.employees[j + 1].surname:
                    temp = self.employees[j]
                    self.employees[j] = self.employees[j + 1]
                    self.employees[j + 1] = temp
        for employee in self.employees:
            print(employee)

    def edit_employee(self, index, name=None, surname=None, position=None):
        if index >= 0 and index < len(self.employees):
            if name:
                self.employees[index].name = name
            if surname:
                self.employees[index].surname = surname
            if position:
                setattr(self.employees[index], 'position', position)
        else:
            print("Немає такого індекса")


of = Office()
a = Employee("Bob", "Robin")
b = Employee("Mark", "Person")
c = Employee("Kevin", "Clark")

of.add_employee(a)
of.add_employee(b)
of.add_employee(c)
of.sort_employees()

of.edit_employee(2, surname="Robinson", position="Boss")

of.sort_employees()
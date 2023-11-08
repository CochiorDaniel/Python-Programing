class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def manage(self):
        return f"{self.name} manages the {self.department} department."


class Engineer(Employee):
    def __init__(self, name, salary, specialty):
        super().__init__(name, salary)
        self.specialty = specialty

    def domain(self):
        return f"{self.name} is engineer in the field of {self.specialty}."


class Salesperson(Employee):
    def __init__(self, name, salary, region):
        super().__init__(name, salary)
        self.region = region

    def sell(self):
        return f"{self.name} sells in the {self.region}."


manager = Manager('Daniel', 10000, 'IT')
print(manager.manage())

engineer = Engineer('Andrei', 8000, 'Software')
print(engineer.domain())

salesperson = Salesperson('Serban Trambitasu', 2000, 'Bucuresti')
print(salesperson.sell())

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __str__(self):
        return f"{self.name}: {self.salary:2f}"
    
employee = [
    Employee("Riddhi", 40000),
    Employee("Dishu", 50000),
    Employee("Heni", 60000),
    Employee("Putha", 70000)
]


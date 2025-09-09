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

employee = list(map(lambda e: Employee(e.name, e.salary * 1.10), employee))

high_salary = list(filter(lambda e: e.salary > 50000, employee))

print("All employees after raise:")
for e in employee:
    print(e)

print("\nEmployees with salary greater than 50000:")
for e in high_salary:
    print(e)
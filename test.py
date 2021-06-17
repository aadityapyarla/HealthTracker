class Employee:

    counter = 0
    no_of_leaves = 8

    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position
        Employee.counter = Employee.counter + 1
        self.id = Employee.counter

    @classmethod
    def instance_count(cls):
        return cls.counter

    @classmethod
    def modify_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves


class Programmer(Employee):
    def print_details(self):
        print("You are a Porgrammer")


aaditya = Programmer("Aaditya  Pyarla", 145000, "Assistant Vice President")
print(aaditya.no_of_leaves)
aaditya.modify_leaves(100)
print(aaditya.no_of_leaves)


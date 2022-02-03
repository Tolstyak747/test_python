import random

class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age


class Employee(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def payment(self):
        pass

    def __str__(self):
        print(f"{self.get_name()} {self.get_surname()} в возрасте {self.get_age()} получает зарплату {self.payment()}")


class Manager(Employee):
    salary = 13000

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)


    def payment(self):
        return self.salary



class Agent(Employee):
    salary = 5000

    def __init__(self, name, surname, age, sales=random.randint(1000, 100000)):
        super().__init__(name, surname, age)
        self.sales = sales


    def payment(self):
        return self.sales * 0.05 + self.salary


class Worker(Employee):
    def __init__(self, name, surname, age, hours=random.randint(1, 150)):
        super().__init__(name, surname, age)
        self.hours = hours

    def payment(self):
        return 100 * self.hours


a = Manager(name="Denis", surname="Poplavok", age=random.randint(20, 50))
b = Manager(name="Artem", surname="Kiss", age=random.randint(20, 50))
c = Manager(name="Ivan", surname="Egov", age=random.randint(20, 50))
d = Agent(name="Larisa", surname="Ivanova", age=random.randint(20, 50))
e = Agent(name="Dima", surname="Terak", age=random.randint(20, 50))
f = Agent(name="Valya", surname="Proslova", age=random.randint(20, 50))
g = Worker(name="Serg", surname="Vasilev", age=random.randint(20, 50))
h = Worker(name="Wayne", surname="Kotov", age=random.randint(20, 50))
i = Worker(name="Bruce", surname="Lof", age=random.randint(20, 50))

ls = [a, b, c, d, e, f, g, h, i]


for i in ls:
    i.__str__()





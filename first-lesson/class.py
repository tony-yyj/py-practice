class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]
    
    def give_raise(self, percent):
        self.pay *= (1.0 + percent)


bob = Worker('Bob Smith', 5000)

print(bob)

print(bob.last_name())
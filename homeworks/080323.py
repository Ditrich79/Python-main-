
class Student:
    def __init__(self, name):
        self.name = name
        self.lt = self.Laptop()

    def show_info(self):
        print(f'{self.name} =>', end=' ')
        self.lt.show_lap()

    class Laptop:
        def __init__(self):
            self.model = 'HP'
            self.cpu = 'i7'
            self.memory = '16'

        def show_lap(self):
            print(f'{self.model}, {self.cpu}, {self.memory}')


stud = Student("Roman")
stud.show_info()
stud2 = Student('Vladimir')
stud2.show_info()







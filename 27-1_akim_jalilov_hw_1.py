class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
    def introduce_myself(self):
        print(f"Полное имя:{self.fullname} \nВозраст:{self.age} \nЖенат/Замужем:{self.is_married}")
class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = dict(marks)
    def average_marks(self):
        print(f"средняя оценка по предметам: {(sum(self.marks.values()) / len(self.marks)).__round__(1)}")

class Teacher(Person):
    salary = 1000
    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience
    def all_salary(self):
        all_salary = self.salary * self.experience
        if self.experience > 3:
            all_salary += all_salary / 100 * 5
        print(all_salary)
teacher = Teacher("Александр", 43, True, 5)
teacher.introduce_myself()
teacher.all_salary()

def create_students():
    student1 = Student("Байистан", 17, False, {"Алгебра": 4, "Русский": 3, "Кыргызский": 4})
    student2 = Student("Камила", 17, False, {"Алгебра": 5, "Русский": 5, "Кыргызский": 5})
    student3 = Student("Айдана", 17, False, {"Алгебра": 4, "Русский": 5, "Кыргызский": 5})
    students = [student1, student2, student3]
    return students

for i in create_students():
    i.introduce_myself()
    i.average_marks()
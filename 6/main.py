# 6).

class Human:
    def __init__(self, gender, first_name, last_name, age):
        self.gender = gender
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nAge: {self.age} years old\nGender:{self.gender}"


class Student(Human):
    def __init__(self, gender, first_name, last_name, age, record_book):
        super().__init__(gender, first_name, last_name, age)
        self.record_book = record_book

    def __str__(self):
        return f"Record Book: {self.record_book}"


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise Exception("Group is full")
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += str(student) + '\n'
        if all_students:
            return f"Group {self.number}:\n{all_students}"
        else:
            return f"Group {self.number} is empty."


st1 = Student("Male", "Steve", "Jobs", 30, "AN142")
st2 = Student("Female", "Liza", "Taylor", 25, "AN145")
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
gr.find_student("Jobs")
gr.find_student("Jobs2")  # None

gr.delete_student('Taylor')
print(gr)  # Only one student

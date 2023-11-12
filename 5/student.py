from human import Human


class Student(Human):
    def __init__(self, gender, first_name, last_name, age, record_book):
        super().__init__(gender, first_name, last_name, age)
        self.record_book = record_book

    def __str__(self):
        return f"Record Book: {self.record_book}"

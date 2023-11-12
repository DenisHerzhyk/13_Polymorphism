class Human:
    def __init__(self, gender, first_name, last_name, age):
        self.gender = gender
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nAge: {self.age} years old\nGender: {self.gender}"

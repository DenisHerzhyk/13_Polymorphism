from student import Student
from group import Group

st1 = Student("Male", "Steve", "Jobs", 30, "AN142")
st2 = Student("Female", "Liza", "Taylor", 25, "AN145")
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
gr.find_student("Jobs")
gr.find_student("Jobs2")  # None

gr.delete_student('Taylor')
gr.delete_student('Jobs')
print(gr)  # Only one student

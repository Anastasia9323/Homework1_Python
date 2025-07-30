from lesson3_student import Student
from lesson3_courseGroup import CourseGroup

student = Student("Анна", "Иванова", 25, "Тестировщик")
classmate1 = Student("Иван", "Петров", 27, "Тестировщик")
classmate2 = Student("Мария", "Сидорова", 24, "Тестировщик")
classmate3 = Student("Дмитрий", "Кузнецов", 26, "Тестировщик")

course_group = CourseGroup(student, [classmate1, classmate2, classmate3])

print(course_group)

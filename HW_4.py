#Создайте по 2 экземпляра каждого класса, вызовите все созданные методы, а также реализуйте две функции:
#для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
#(в качестве аргументов принимаем список студентов и название курса);
#для подсчета средней оценки за лекции всех лекторов в рамках курса
#(в качестве аргумента принимаем список лекторов и название курса).

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}  # Оценки студентов за ДЗ

    def rate_lecturer(self, lecturer, course, grade):
        #Метод для выставления оценки лектору студентом
        if (
            isinstance(lecturer, Lecturer) and
            course in self.courses_in_progress and
            course in lecturer.courses_attached
        ):
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def get_average_grade(self):
        #Вычисляет среднюю оценку за домашние задания
        if not self.grades:
            return 0
        total_grades = sum(sum(grades) for grades in self.grades.values())
        count_grades = sum(len(grades) for grades in self.grades.values())
        return round(total_grades / count_grades, 1)

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.get_average_grade()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses) if self.finished_courses else 'Нет'}")

    def __lt__(self, other):
        #Сравнение студентов по средней оценке
        if isinstance(other, Student):
            return self.get_average_grade() < other.get_average_grade()
        return NotImplemented

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # Оценки за лекции от студентов

    def get_average_grade(self):
        #Вычисляет среднюю оценку за лекции
        if not self.grades:
            return 0
        total_grades = sum(sum(grades) for grades in self.grades.values())
        count_grades = sum(len(grades) for grades in self.grades.values())
        return round(total_grades / count_grades, 1)

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.get_average_grade()}")

    def __lt__(self, other):
        #Сравнение лекторов по средней оценке
        if isinstance(other, Lecturer):
            return self.get_average_grade() < other.get_average_grade()
        return NotImplemented

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        #Метод для проверки ДЗ студентам (доступен только у Reviewer)
        if (
            isinstance(student, Student) and
            course in self.courses_attached and
            course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

# Функция для подсчета средней оценки за ДЗ по курсу
def average_student_grade(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    return round(sum(total_grades) / len(total_grades), 1) if total_grades else 0

# Функция для подсчета средней оценки за лекции по курсу
def average_lecturer_grade(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    return round(sum(total_grades) / len(total_grades), 1) if total_grades else 0

# Создаем объекты студентов
student1 = Student('Анна', 'Иванова', 'женский')
student1.courses_in_progress.append('Python')
student1.finished_courses.append('Git')

student2 = Student('Олег', 'Смирнов', 'мужской')
student2.courses_in_progress.append('Python')

# Создаем объекты лекторов
lecturer1 = Lecturer('Игорь', 'Петров')
lecturer1.courses_attached.append('Python')

lecturer2 = Lecturer('Мария', 'Васильева')
lecturer2.courses_attached.append('Python')

# Создаем объекты проверяющих
reviewer1 = Reviewer('Мария', 'Сидорова')
reviewer1.courses_attached.append('Python')

reviewer2 = Reviewer('Алексей', 'Кузнецов')
reviewer2.courses_attached.append('Python')

# Проверяющие оценивают ДЗ студентов
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)

reviewer2.rate_hw(student2, 'Python', 8)
reviewer2.rate_hw(student2, 'Python', 7)

# Студенты оценивают лекторов
student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Python', 8)

student2.rate_lecturer(lecturer2, 'Python', 9)
student2.rate_lecturer(lecturer2, 'Python', 7)

# Вывод объектов
print(reviewer1, "\n")
print(reviewer2, "\n")
print(lecturer1, "\n")
print(lecturer2, "\n")
print(student1, "\n")
print(student2, "\n")

# Сравнение студентов и лекторов
print("Сравнение студентов:")
print(f"{student1.name} лучше {student2.name}? {'Да' if student1 > student2 else 'Нет'}\n")

print("Сравнение лекторов:")
print(f"{lecturer1.name} лучше {lecturer2.name}? {'Да' if lecturer1 > lecturer2 else 'Нет'}\n")

# Вычисление средней оценки за курс
students = [student1, student2]
lecturers = [lecturer1, lecturer2]

print(f"Средняя оценка за ДЗ по курсу 'Python': {average_student_grade(students, 'Python')}")
print(f"Средняя оценка за лекции по курсу 'Python': {average_lecturer_grade(lecturers, 'Python')}")
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)  # Инициализация родительского класса
        self.lecturer_courses = []  # Можно добавить атрибуты, специфичные для лекторов


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)  # Инициализация родительского класса
        self.reviewer_courses = []

# Создаем студента
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

# Создаем ментора (лектора)
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

# Лектор ставит оценки
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 9)

# Выводим оценки студента
print(best_student.grades)

# Создаем эксперта
expert = Reviewer('Expert', 'One')
expert.courses_attached += ['Python']

# Эксперт может поставить оценку (если необходим метод для этого)
expert.rate_hw(best_student, 'Python', 8)

# Выводим оценки студента
print(best_student.grades)

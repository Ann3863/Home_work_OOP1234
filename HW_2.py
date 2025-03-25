#Задание № 2. Атрибуты и взаимодействие классов.
#В квизе к предыдущей лекции мы реализовали возможность выставлять студентам оценки за домашние задания.
#Теперь это могут делать только Reviewer (реализуйте такой метод)! А что могут делать лекторы?
# Получать оценки за лекции от студентов :)
# Реализуйте метод выставления оценок лекторам у класса Student
# (оценки по 10-балльной шкале, хранятся в атрибуте-словаре у Lecturer,
# в котором ключи – названия курсов, а значения – списки оценок).
# Лектор при этом должен быть закреплен за тем курсом, на который записан студент.

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}  # Оценки студентов за ДЗ

    def rate_lecturer(self, lecturer, course, grade):
        #Метод для выставления оценки лектору студентом.
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

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # Оценки за лекции от студентов

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

# Создаем объекты
student1 = Student('Анна', 'Иванова', 'женский')
student1.courses_in_progress.append('Python')

lecturer1 = Lecturer('Игорь', 'Петров')
lecturer1.courses_attached.append('Python')

reviewer1 = Reviewer('Мария', 'Сидорова')
reviewer1.courses_attached.append('Python')

# Эксперт оценивает ДЗ студента
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)

# Студент оценивает лектора
student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Python', 8)

# Вывод результатов
print(f'Студент {student1.name} {student1.surname}, обучаясь на курсе "Python", получил оценки {student1.grades["Python"]}')
print(f'Лектор {lecturer1.name} {lecturer1.surname}, преподавая курс "Python", получил оценки {lecturer1.grades["Python"]}')
import json

# Класс DataService для работы с данными о студентах
class DataService:
    def __init__(self, data_file):
        self.data_file = data_file
        self.students = self.load_data()

    # Метод для загрузки данных из файла
    def load_data(self):
        try:
            with open(self.data_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    # Метод для сохранения данных в файл
    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.students, file, indent=4)

    # Метод для добавления данных о студенте
    def add_student(self, student_data):
        self.students.append(student_data)
        self.save_data()

    # Метод для получения списка студентов
    def get_students(self):
        return self.students

# Создаем экземпляр класса DataService и передаем ему имя файла с данными о студентах
if __name__ == "__main__":
    data_service = DataService('students_data.json')
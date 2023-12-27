import sys
from data import DataService

# Создаем экземпляр класса DataService и передаем ему имя файла с данными о студентах
data_service = DataService('students_data.json')


# Функция для вывода информации о студентах
def print_students():
    # Получаем список студентов с помощью метода get_students() из класса DataService
    students = data_service.get_students()

    # Выводим заголовок таблицы
    print("ФИО\t\t\tДата Рождения")

    # Перебираем каждого студента и выводим его ФИО и дату рождения
    for student in students:
        print(f"{student['name']}\t{student['dob']}")


# Основная функция программы
def main():
    # Проверяем, передан ли флаг '--auto' в аргументах командной строки
    if '--auto' in sys.argv:
        # Если да, просто выводим список студентов и выходим
        print_students()
        return

    while True:
        # Запрашиваем у пользователя команду
        action = input("Введите 'fd' для вывода списка ФИО и даты рождения студентов, или 'exit' для выхода: ")

        # Если пользователь ввел 'exit', выходим из программы
        if action.lower() == 'exit':
            break
        # Если пользователь ввел 'fd', вызываем функцию print_students() для вывода списка студентов
        elif action.lower() == 'fd':
            print_students()


# Проверяем, является ли данный файл главным исполняемым модулем
if __name__ == "__main__":
    main()
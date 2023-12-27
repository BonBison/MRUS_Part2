import unittest
from data import DataService

class TestDataService(unittest.TestCase):
    def setUp(self):
        self.data_service = DataService('students_data.json')
        self.data_service.students = [
            {"name": "Освальд Кобблпот", "dob": "2000-01-02"},
            {"name": "Селина Кайл", "dob": "1999-12-31"},
            {"name": "Хантер Соломон", "dob": "2001-06-15"}
        ]

if __name__ == '__main__':
    unittest.main()
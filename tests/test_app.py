import unittest
from unittest.mock import patch
import io
from app import print_students

class TestApp(unittest.TestCase):

    @patch('app.data_service.get_students')
    def test_print_students(self, mock_get_students):
        mock_get_students.return_value = [
            {"name": "Освальд Кобблпот", "dob": "2000-01-02"},
            {"name": "Селина Кайл", "dob": "1999-12-31"}
        ]
        with patch('sys.stdout', new_callable=io.StringIO) as fake_out:
            print_students()
            self.assertIn("Освальд Кобблпот\t2000-01-02", fake_out.getvalue())
            self.assertIn("Селина Кайл\t1999-12-31", fake_out.getvalue())

if __name__ == '__main__':
    unittest.main()
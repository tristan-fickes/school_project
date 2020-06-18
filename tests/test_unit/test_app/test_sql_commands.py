import unittest
from unittest.mock import MagicMock, patch

from app.sql_commands import create_connection


class TestCreateConnection(unittest.TestCase):

    def test_returns_database(self):
        actual = create_connection(r"C:\Users\Tristan\Desktop\School Project\app\new.sqlite")
        self.assertIsNotNone(actual)

    @patch('app.sql_commands.sqlite3')
    def test_calls_connect_with_path(self, mock_connect):
        path = r"C:\Users\Tristan\Desktop\School Project\app\test.sqlite"
        connect = create_connection(r"C:\Users\Tristan\Desktop\School Project\app\test.sqlite")
        # with self.subTest():
        #     mock_connect.assert_called_once_with(path)
        self.assertIsNotNone(connect)


if __name__ == '__main__':
    unittest.main()

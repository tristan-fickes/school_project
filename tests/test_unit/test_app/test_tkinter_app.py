from unittest import TestCase
from unittest.mock import patch

from app.tkinter_app import log_student


class TestActivateStudent(TestCase):
    """ Tests for the activate_student function."""

    @patch('app.tkinter_app.activate_student.is_active')
    @patch('app.tkinter_app.activate_student.get')
    def test_get_entry(self, mock_get_entry, mock_is_active):
        """ The get call retrieves the correct entry from the user."""

        mock_get_entry.return_value = 1234
        mock_is_active.return_value = False


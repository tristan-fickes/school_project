from unittest import TestCase
from unittest.mock import patch

from school_project.app.tkinter_app import StudentLogging, MainApplication


class TestMainApplication(TestCase):
    """ Tests for the activate_student function."""

    @patch('app.tkinter_app.MainApplication.create_list_widgets')
    @patch('app.tkinter_app.MainApplication.create_label_widgets')
    @patch('app.tkinter_app.MainApplication.create_button_widgets')
    @patch('app.tkinter_app.MainApplication.create_entry_widgets')
    @patch('app.tkinter_app.MainApplication.set_window_config')
    def setUp(
            self,
            mock_set_window_config,
            mock_create_entry_widgets,
            mock_create_button_widgets,
            mock_create_label_widgets,
            mock_create_list_widgets
    ):
        mock_set_window_config = "config"
        self.mock_set_window_config = mock_set_window_config
        mock_create_entry_widgets = "entry"
        self.mock_create_entry_widgets = mock_create_entry_widgets
        mock_create_button_widgets = "button"
        self.mock_create_button_widgets = mock_create_button_widgets
        mock_create_label_widgets = "label"
        self.mock_create_label_widgets = mock_create_label_widgets
        mock_create_list_widgets = "list"
        self.mock_create_list_widgets = mock_create_list_widgets
        app = MainApplication()

    def test_init_calls_methods(self):

        with self.subTest():
            self.mock_set_window_config.assert_called_once_with()



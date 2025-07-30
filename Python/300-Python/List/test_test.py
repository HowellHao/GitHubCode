import unittest
from unittest.mock import patch
from Python.List.test import main # type: ignore

class TestMainFunction(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '5', '2'])
    @patch('builtins.print')
    def test_insert_number_and_exit(self, mock_print, mock_input):
        main()
        print(mock_print.mock_calls)  # Debug print to see what is being printed
        mock_print.assert_any_call([1, 2, 3, 4, 5, 5, 6, 7, 8, 9])
        mock_print.assert_any_call("Exit Program")

    @patch('builtins.input', side_effect=['2'])
    @patch('builtins.print')
    def test_exit_program(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("Exit Program")

    @patch('builtins.input', side_effect=['3', '2'])
    @patch('builtins.print')
    def test_invalid_choice(self, mock_print, mock_input):
        main()
        mock_print.assert_any_call("Invalid choice. Please choose a valid option.")
        mock_print.assert_called_with("Exit Program")

if __name__ == '__main__':
    unittest.main()
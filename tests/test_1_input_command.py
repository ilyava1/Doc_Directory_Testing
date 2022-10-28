import unittest
from unittest.mock import patch
from doc_operations import input_command


class TestClass_1_Functions(unittest.TestCase):
    @patch('builtins.input', return_value='x')
    def test_input_command(self, mock_input):
        result = input_command()
        self.assertEqual('x', result)

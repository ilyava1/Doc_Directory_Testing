import unittest
from unittest.mock import patch
from doc_operations import input_doc_num, input_doc_owner, input_doc_type
from doc_operations import input_doc_shelf


class TestClass_21_Functions(unittest.TestCase):
    @patch('builtins.input', return_value='11-2')
    def test_input_doc_num(self, mock_input):
        result = input_doc_num()
        self.assertEqual('11-2', result)


class TestClass_22_Functions(unittest.TestCase):
    @patch('builtins.input', return_value='passport')
    def test_input_doc_type(self, mock_input):
        result = input_doc_type()
        self.assertEqual('passport', result)


class TestClass_23_Functions(unittest.TestCase):
    @patch('builtins.input', return_value='Harry Potter')
    def test_input_doc_owner(self, mock_input):
        result = input_doc_owner()
        self.assertEqual('Harry Potter', result)


class TestClass_24_Functions(unittest.TestCase):
    @patch('builtins.input', return_value='4')
    def test_input_doc_shelf(self, mock_input):
        result = input_doc_shelf()
        self.assertEqual('4', result)

import unittest
from parameterized import parameterized
from doc_operations import add_doc_shelf
from doc_directory_db import directories

FIXTURES = [
    ('4', 'Полка 4 добавлена'),
    ('3', 'Полка с таким номером уже существует')
]


class TestClass_10_Functions(unittest.TestCase):
    @parameterized.expand(FIXTURES)
    def test_move_doc(self, shelf_number, expected_result):
        result = add_doc_shelf(shelf_number, directories)
        self.assertEqual(result, expected_result)

import unittest
from parameterized import parameterized
from doc_operations import move_doc
from doc_directory_db import directories

FIXTURES = [
    ('2207 876234', '3', 'Документ номер 2207 876234 перемещен на полку 3'),
    ('10006', '4', 'Полки номер 4 нет в каталоге')
]


class TestClass_9_Functions(unittest.TestCase):
    @parameterized.expand(FIXTURES)
    def test_move_doc(self, doc_number, shelf_number, expected_result):
        result = move_doc(doc_number, shelf_number, directories)
        self.assertEqual(result, expected_result)

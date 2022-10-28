import unittest
from parameterized import parameterized
from doc_operations import add_new_doc
from doc_directory_db import documents, directories

FIXTURES = [
    ('333', 'passport', 'Harry Potter', '3',
     'Документ passport номер 333 добавлен на полку 3'),
    ('444', 'passport', 'Ron Weasley', '4',
     'Полки номер 4 не существует')
]


class TestClass_7_Functions(unittest.TestCase):
    @parameterized.expand(FIXTURES)
    def test_add_new_doc(self, new_doc_number, new_doc_type, new_doc_owner,
                         new_doc_shelf, expected_result):
        result = add_new_doc(new_doc_number, new_doc_type, new_doc_owner,
                             new_doc_shelf, documents, directories)
        self.assertEqual(result, expected_result)

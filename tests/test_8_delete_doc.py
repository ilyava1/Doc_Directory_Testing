import unittest
from parameterized import parameterized
from doc_operations import delete_doc
from doc_directory_db import documents, directories

FIXTURES = [
    ('11-2', 'Документ номер 11-2 удален из каталога и с полки 1'),
    ('44-4', 'Документ с таким номером в каталоге отсутствует')
]


class TestClass_8_Functions(unittest.TestCase):
    @parameterized.expand(FIXTURES)
    def test_add_new_doc(self, doc_number, expected_result):
        result = delete_doc(doc_number, documents, directories)
        self.assertEqual(result, expected_result)

import unittest
from parameterized import parameterized
from doc_operations import doc_owner_name
from doc_directory_db import documents

FIXTURES = [
    ('2207 876234', 'Василий Гупкин'),
    ('11-2', 'Геннадий Покемонов'),
    ('10006', 'Аристарх Павлов')
]


class TestClass_3_Functions(unittest.TestCase):
    @parameterized.expand(FIXTURES)
    def test_doc_owner_name(self, doc_num, exp_result):
        result = doc_owner_name(doc_num, documents)
        self.assertEqual(exp_result, result)

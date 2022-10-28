import unittest
from parameterized import parameterized
from doc_operations import doc_shelf
from doc_directory_db import directories

FIXTURES = [
    ('2207 876234', '1'),
    ('11-2', '1'),
    ('5455 028765', '1'),
    ('10006', '2')
]


class TestClass_4_Functions(unittest.TestCase):
    @parameterized.expand(FIXTURES)
    def test_doc_shelf(self, doc_num, exp_result):
        result = doc_shelf(doc_num, directories)
        self.assertEqual(exp_result, result)

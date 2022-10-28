import unittest
from doc_operations import doc_list
from doc_directory_db import documents


class TestClass_5_Functions(unittest.TestCase):

    def test_doc_list(self):
        result = doc_list(documents)
        self.assertEqual(documents, result)

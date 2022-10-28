import unittest
from doc_operations import doc_shelf_list
from doc_directory_db import documents, directories


class TestClass_6_Functions(unittest.TestCase):

    def test_doc_list(self):
        result_doc, result_dir = doc_shelf_list(documents, directories)
        self.assertEqual(result_doc, documents)
        self.assertEqual(result_dir, directories)

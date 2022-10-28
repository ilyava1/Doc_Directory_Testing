from test_1_input_command import TestClass_1_Functions
from test_2_input_doc_num import TestClass_21_Functions
from test_2_input_doc_num import TestClass_22_Functions
from test_2_input_doc_num import TestClass_23_Functions
from test_2_input_doc_num import TestClass_24_Functions
from test_3_doc_owner_name import TestClass_3_Functions
from test_4_doc_shelf import TestClass_4_Functions
from test_5_doc_list import TestClass_5_Functions
from test_6_doc_shelf_list import TestClass_6_Functions
from test_7_add_new_doc import TestClass_7_Functions
from test_8_delete_doc import TestClass_8_Functions
from test_9_move_doc import TestClass_9_Functions
from test_10_add_doc_shelf import TestClass_10_Functions
import unittest
from unittest import TestSuite


def load_tests(loader, tests, pattern):
    suite = TestSuite()
    for test_class in (TestClass_1_Functions, TestClass_21_Functions,
                       TestClass_22_Functions, TestClass_23_Functions,
                       TestClass_24_Functions, TestClass_3_Functions,
                       TestClass_4_Functions, TestClass_5_Functions,
                       TestClass_6_Functions, TestClass_7_Functions,
                       TestClass_8_Functions, TestClass_9_Functions,
                       TestClass_10_Functions):
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite


unittest.main(verbosity=2)

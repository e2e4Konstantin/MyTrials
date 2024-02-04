# https://docs.python.org/3/library/unittest.html#unittest.TestCase

import unittest
import sys
import time

# from Unittest_case.class_for_test import Student
# # set PYTHONPATH=%PYTHONPATH%;F:\Kazak\GoogleDrive\Python_projects\MyTrials\Unittest_case
# # export PYTHONPATH=$PYTHONPATH:F:\Kazak\GoogleDrive\Python_projects\MyTrials\Unittest_case
# # bash: export PYTHONPATH="F:\Kazak\GoogleDrive\Python_projects\MyTrials\Unittest_cas"




if "F:\Kazak\GoogleDrive\Python_projects\MyTrials" not in sys.path:
    sys.path.append(r"F:\Kazak\GoogleDrive\Python_projects\MyTrials")
# print(type(sys.path))
# for x in sys.path:
#     print(x)

from Unittest_case.class_for_test import Student

# class StudentTestCase(unittest.TestCase):

#     def test_default_name_is_none(self):
#         student = Student()
#         self.assertIsNone(student.name)

#     def test_set_invalid_age(self):
#         student = Student()
#         with self.assertRaises(ValueError):
#             student.set_age(-100)


class StudentTestCase(unittest.TestCase):
    def setUp(self):
        self.start = time.perf_counter()
        self.student = Student()

    def tearDown(self):
        self.end = time.perf_counter()
        print('\n---> ', self.id(), self.end - self.start)

    def test_million_appends(self):
        N = 1_000_000
        lst = [i for i in range(N)]
        self.assertListEqual(lst, list(range(N)))

    def test_default_name_is_none(self):
        self.assertIsNone(self.student.name)


    # def test_set_invalid_age(self):
    #     with self.assertRaises(ValueError):
    #         self.student.set_age(-100)


class PerformanceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.file = open("test_log.txt", "a")

    def setUp(self):
        self.start = time.perf_counter()

    def test_million_appends(self):
        N = 1_000_000
        lst = []
        for i in range(N):
            lst.append(i)
        self.assertListEqual(lst, list(range(N)))

    def test_sum_of_numbers(self):
        N = 1_000_000
        self.assertEqual(sum(range(N)), N * (N + 1) // 2)

    def tearDown(self):
        self.end = time.perf_counter()
        print(self.id(), self.end - self.start, file=self.file)

    @classmethod
    def tearDownClass(cls):
        cls.file.close()



if __name__ == '__main__':
    unittest.main()

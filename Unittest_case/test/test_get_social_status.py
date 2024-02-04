# python -m unittest  - запуск тестов из модуля test
# python -m unittest test.test_get_social_status.TestSocialAge.test_can_get_pensioner_age
# python -m unittest -v

# python -m unittest discover <test_directory>
# or
# python -m unittest discover -s <directory> -p '*_test.py'


import unittest
from social_age import get_social_status

class TestSocialAge(unittest.TestCase):

    def test_can_get_child_age(self):
        age = 8
        expected_res = 'ребенок'
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)

    def test_can_get_teenager_age(self):
        age = 15
        expected_res = "подросток"
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)

    def test_can_get_adult_age(self):
        age = 45
        expected_res = "взрослый"
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)

    def test_can_get_elderly_age(self):
        age = 64
        expected_res = "пожилой"
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)

    def test_can_get_pensioner_age(self):
        age = 70
        expected_res = "пенсионер"
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)


    def test_cannot_pass_str_as_age(self):
        age = 'old'
        with self.assertRaises(ValueError):
            get_social_status(age)

    def test_cannot_pass_negative_age(self):
        age = -20
        with self.assertRaises(ValueError):
            get_social_status(age)

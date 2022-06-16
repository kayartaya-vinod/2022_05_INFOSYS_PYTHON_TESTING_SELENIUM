import unittest
from mathutils import calculate_sum


class TestMathutilsCalculateSum(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('TestMathutilsCalculateSum.setUpClass() called')

    @classmethod
    def tearDownClass(cls) -> None:
        print('TestMathutilsCalculateSum.tearDownClass() called')

    def setUp(self):
        print('TestMathutilsCalculateSum.setUp() called')

    def tearDown(self):
        print('TestMathutilsCalculateSum.tearDown() called')
        print()

    def test_should_add_two_numbers(self):
        print('TestMathutilsCalculateSum.test_should_add_two_numbers() called')
        self.assertEqual(30, calculate_sum("10, 20"))

    def test_should_add_numbers_with_strings(self):
        print('TestMathutilsCalculateSum.test_should_add_numbers_with_strings called')
        self.assertEqual(30, calculate_sum("10, 20, vinod, kumar"))

    def test_should_add_negative_numbers(self):
        print('TestMathutilsCalculateSum.test_should_add_negative_numbers() called')
        self.assertEqual(30, calculate_sum("60, -10, -20"))


if __name__ == '__main__':
    unittest.main()

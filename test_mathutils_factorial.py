import unittest
from mathutils import factorial
import HtmlTestRunner


class TestMathutilsFactorial(unittest.TestCase):

    def test_should_get_factorial_of_positive_number(self):
        num = 5
        expected = 120
        actual = factorial(num)
        self.assertEqual(expected, actual)

    # @unittest.skip('not interested now')
    def test_should_get_factorial_of_zero(self):
        expected = 1
        actual = factorial(0)
        self.assertEqual(expected, actual)

    def test_should_raise_value_error_for_negative_input(self):
        # this is not the right way to handle error situations
        try:
            factorial(-5)
            self.fail('Was expecting a ValueError; but did not receive one!')
        except ValueError:
            pass  # this was expected; all is well

    def test_should_raise_type_error_for_str(self):
        def fn():
            factorial('Vinod')
        self.assertRaises(TypeError, fn)

    def test_should_raise_type_error_for_boolean_false(self):
        self.assertRaises(TypeError, lambda: factorial(False))

    def test_should_raise_type_error_for_boolean_true(self):
        self.assertRaises(TypeError, lambda: factorial(True))


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./report'))

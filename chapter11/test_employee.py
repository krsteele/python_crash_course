import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """
    Tests for the class Employee.
    """

    def setUp(self):
        """Create employee for use in all test methods."""
        self.employee_1 = Employee('Cat', 'Sandwich', 125000)

    def test_give_default_raise(self):
        """Test that the give_raise method works with the default raise."""
        self.employee_1.give_raise()
        self.assertEqual(self.employee_1.annual_salary, 130000)

    def test_give_custom_raise(self):
        """Test that the give_raise method works given an argument different than the default."""
        self.employee_1.give_raise(10000)
        self.assertEqual(self.employee_1.annual_salary, 135000)

if __name__ == '__main__':
    unittest.main()
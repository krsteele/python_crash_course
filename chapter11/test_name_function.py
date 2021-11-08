# A unit test verifies that one specific aspect of a function's behavior is correct. 
# A test case is a collection of unit tests that together prove that a function behaves as it's supposed to,
# within a full range of situations you expect it to handle. 

# import the unittest module and the function you want to test
import unittest
from name_function import get_formatted_name

# create a class which will contain a series of unit tests. this class must inherit from the class unittest.TestCase 
class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    # method to test one aspect of our function
    # any method that starts with test_ will be run automatically when we run this file
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        # call the function we want to test, pass in arguments, and assign the results to a variable
        formatted_name = get_formatted_name('janis', 'joplin')
        # use unittest's assert method to verify that the result we receive is the result we expect to receive
        # this says, "compare the value in formatted_name and 'Janis Joplin' to make sure they are equal. let me know if they are not."
        self.assertEqual(formatted_name, 'Janis Joplin')
    # name the method to make it clear which behavior we're testing
    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()
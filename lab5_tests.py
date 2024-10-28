import lab5
import unittest
from data import Time



# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_time_add1(self):
        time1 = Time(4,50,55)
        time2 = Time(7,25,23)
        result = lab5.time_add(time1, time2)
        expected = Time(11, 75, 78)
        self.assertEqual(expected, result)


    # Part 4


    # Part 5


    # Part 6





if __name__ == '__main__':
    unittest.main()

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
        expected = Time(12, 16, 18)
        self.assertEqual(expected, result)

    def test_time_add2(self):
        time1 = Time(1,30,30)
        time2 = Time(1,6,30)
        result = lab5.time_add(time1, time2)
        expected = Time(2,37,0)
        self.assertEqual(expected, result)

    # Part 4
    def test_is_descending1(self):
        list = [5,4,3,2,1]
        result = lab5.is_descending(list)
        expected = True
        self.assertEqual(expected, result)

    # Part 5


    # Part 6





if __name__ == '__main__':
    unittest.main()

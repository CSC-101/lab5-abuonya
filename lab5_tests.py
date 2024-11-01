import lab5
import unittest
from data import Time
from data import Point



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

    def test_is_descending2(self):
        list = []
        result = lab5.is_descending(list)
        expected = True
        self.assertEqual(expected, result)

    def test_is_descending3(self):
        list = [6,9,40,1,4]
        result = lab5.is_descending(list)
        expected = False
        self.assertEqual(expected, result)

    # Part 5
    def test_largest_between1(self):
        list = ([1,2,3,4,5,6,7,8,9,10])
        a = 2
        b = 7
        result = lab5.largest_between(list, a, b)
        expected = 8
        self.assertEqual(expected, result)

    def test_largest_between2(self):
        list = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        a = 7
        b = 2
        result = lab5.largest_between(list, a, b)
        expected = None
        self.assertEqual(expected, result)

    # Part 6
    def test_furthest_from_origin1(self):
        input = [Point(4,4),  Point(79, 87), Point(700, 700)]
        result = lab5.furthest_from_origin(input)
        expected = 2
        self.assertEqual(expected, result)

    def test_furthest_from_origin2(self):
        input = [Point(700, 700), Point(4,4),  Point(79, 87), Point(700, 700)]
        result = lab5.furthest_from_origin(input)
        expected = 0
        self.assertEqual(expected, result)

    def test_furthest_from_origin3(self):
        input = []
        result = lab5.furthest_from_origin(input)
        expected = None
        self.assertEqual(expected, result)






if __name__ == '__main__':
    unittest.main()

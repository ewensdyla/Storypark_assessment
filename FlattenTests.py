import unittest
import FlattenArray


class Tests(unittest.TestCase):
    def test_nested_array_01(self):
        array = [[1], [2], 3]
        flat_array = FlattenArray.flatten(array)
        expected = [1, 2, 3]
        self.assertTrue(flat_array == expected)

    def test_nested_array_02(self):
        array = [[1], [2], [3]]
        flat_array = FlattenArray.flatten(array)
        expected = [1, 2, 3]
        self.assertTrue(flat_array == expected)

    def test_nested_array_03(self):
        array = [1, [2, 3], [4]]
        flat_array = FlattenArray.flatten(array)
        expected = [1, 2, 3, 4]
        self.assertTrue(flat_array == expected)

    def test_nested_array_04(self):
        array = [[1], [2, 3], [4]]
        flat_array = FlattenArray.flatten(array)
        expected = [1, 2, 3, 4]
        self.assertTrue(flat_array == expected)

    def test_nested_array_05(self):
        array = [[], [1], [2, 3], [4]]
        flat_array = FlattenArray.flatten(array)
        expected = [1, 2, 3, 4]
        self.assertTrue(flat_array == expected)

    def test_nested_array_06(self):
        array = [[], [1, []], [2, 3], [4, [5], [[6]]]]
        flat_array = FlattenArray.flatten(array)
        expected = [1, 2, 3, 4, 5, 6]
        self.assertTrue(flat_array == expected)


if __name__ == '__main__':
    unittest.main()

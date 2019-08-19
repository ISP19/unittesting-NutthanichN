import unittest
from listutil import unique


class ListTest(unittest.TestCase):
    def test_unique_single_value(self):
        """Test single value including borderline cases"""
        self.assertEqual([], unique([]))
        self.assertEqual([5], unique([5]))
        self.assertEqual(["a"], unique(["a"]))

    def test_unique_many_values(self):
        """Test many values with a few duplicates and no duplicates"""
        self.assertEqual([1, 2, 3], unique([1, 2, 3]))
        self.assertEqual(["a", 56, 25.8], unique(["a", 56, 25.8]))
        self.assertEqual([1], unique([1, 1, 1, 1, 1]))
        self.assertEqual([1, 2], unique([1, 1, 2, 2, 5, 5, 1, 2]))
        self.assertEqual([{'car': 'Honda'}, {1, 2, 3}, [1], 1, 2, 'a', 'b'],
                         unique([{"car": "Honda"}, {"car": "Honda"}, {1, 2, 3}, [1],
                                 1, 1, 2, 2, "a", "a", "b", "a", 2]))

    def test_unique_extreme_value(self):
        """Test extreme case, a very large list"""
        self.assertEqual([1], unique([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        self.assertEqual(["a", "b"], unique(["a", "a", "a", "a", "a", "b", "b", "b", "b", "b", "b",
                                             "a", "b", "a", "b", "b", "b", "a", "a", "a", "a", "a"]))

    def test_unique_wrong_value(self):
        """Test impossible case, argument is not a list"""
        # TODO finish this
        with self.assertRaises(ValueError):
            unique(set())
            unique((2, 5))
            unique({"car": "Honda"})

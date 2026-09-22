"""Tests des exemples du checkpoint et de ses cas limites."""

import importlib.util
from pathlib import Path
import unittest


def load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).parent / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


problem1 = load_module("problem1", "probleme1-algo.py")
problem2 = load_module("problem2", "probleme2-algo.py")


class DistinctElementsTests(unittest.TestCase):
    def test_official_example(self):
        self.assertEqual(problem1.sum_of_distinct_elements([3, 1, 7, 9], [2, 4, 1, 9, 3]), 13)

    def test_identical_sets(self):
        self.assertEqual(problem1.sum_of_distinct_elements([1, 2, 3], [3, 1, 2]), 0)

    def test_disjoint_sets_with_negative_values(self):
        self.assertEqual(problem1.sum_of_distinct_elements([-3, 8], [2, 4]), 11)

    def test_empty_sets(self):
        for left, right, expected in (([], [], 0), ([], [2, 4], 6), ([2, 4], [], 6)):
            with self.subTest(left=left, right=right):
                self.assertEqual(problem1.sum_of_distinct_elements(left, right), expected)


class DotProductTests(unittest.TestCase):
    def test_procedure_writes_output_and_returns_none(self):
        v1, v2 = [1, 2, 3], [-2, 4, -1]
        ps = [999]
        self.assertIsNone(problem2.dot_product(v1, v2, ps))
        self.assertEqual(ps, [3])
        self.assertEqual(v1, [1, 2, 3])
        self.assertEqual(v2, [-2, 4, -1])

    def test_procedure_resets_output_for_each_pair(self):
        ps = [999]
        problem2.dot_product([1, 2, 3], [-2, 4, -1], ps)
        problem2.dot_product([1, 2, 3], [1, 1, -1], ps)
        self.assertEqual(ps, [0])

    def test_function_returns_scalar(self):
        self.assertEqual(problem2.dot_product_function([1, 2, 3], [-2, 4, -1]), 3)
        self.assertEqual(problem2.dot_product_function([1.5, 2], [2, -1.5]), 0)

    def test_multiple_pairs_in_both_versions(self):
        pairs = [([1, 2, 3], [1, 1, -1]), ([1, 2, 3], [-2, 4, -1]), ([0, 0], [5, 6])]
        expected = [(0, True), (3, False), (0, True)]
        self.assertEqual(problem2.check_orthogonality_with_procedure(pairs), expected)
        self.assertEqual(problem2.check_orthogonality_with_function(pairs), expected)

    def test_no_pairs(self):
        self.assertEqual(problem2.check_orthogonality_with_procedure([]), [])
        self.assertEqual(problem2.check_orthogonality_with_function([]), [])

    def test_decimal_rounding_in_orthogonality(self):
        pairs = [([0.1, 0.2, 0.3], [1, 1, -1])]
        self.assertTrue(problem2.check_orthogonality_with_procedure(pairs)[0][1])
        self.assertTrue(problem2.check_orthogonality_with_function(pairs)[0][1])

    def test_incompatible_dimensions(self):
        with self.assertRaises(ValueError):
            problem2.dot_product([1, 2], [3], [0])
        with self.assertRaises(ValueError):
            problem2.dot_product_function([1, 2], [3])

    def test_invalid_output_container(self):
        with self.assertRaises(ValueError):
            problem2.dot_product([1], [2], [])


if __name__ == "__main__":
    unittest.main()

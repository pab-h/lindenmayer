import unittest

from lindenmayer import Rule
from lindenmayer import Lindenmayer

class TestLindenmayer(unittest.TestCase):
    def setUp(self):
        self.axiom = "A"
        self.rules = [
            Rule("A", "AB"),
            Rule("B", "A")
        ]
        self.lindenmayer = Lindenmayer(self.axiom, self.rules)

    def test_initial_state(self):
        self.assertEqual(self.lindenmayer.axiom, "A")
        self.assertEqual(self.lindenmayer.last_interact, "A")

    def test_apply_single_iteration(self):
        result = next(self.lindenmayer)
        self.assertEqual(result, "AB")
        self.assertEqual(self.lindenmayer.last_interact, "AB")

    def test_apply_multiple_iterations(self):
        results = list(self.lindenmayer.applyn(3))
        self.assertEqual(results, ["AB", "ABA", "ABAAB"])
        self.assertEqual(self.lindenmayer.last_interact, "ABAAB")

    def test_reset(self):
        self.lindenmayer.apply()
        self.lindenmayer.reset()
        self.assertEqual(self.lindenmayer.last_interact, self.axiom)

if __name__ == '__main__':
    unittest.main()

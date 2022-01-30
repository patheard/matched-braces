import unittest

MODULE = __import__("matched_braces")


class MatchedBracesTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_valid_braces(self):
        self.assertTrue(MODULE.is_balanced("(())"))
        self.assertTrue(MODULE.is_balanced("([])"))
        self.assertTrue(MODULE.is_balanced("{(())[]}"))
        self.assertTrue(MODULE.is_balanced("()[]{}"))
        self.assertTrue(MODULE.is_balanced("[hello]"))
        self.assertTrue(MODULE.is_balanced("{general kenobi}"))

    def test_invalid_braces(self):
        self.assertFalse(MODULE.is_balanced("(d))"))
        self.assertFalse(MODULE.is_balanced("([a]"))
        self.assertFalse(MODULE.is_balanced("([{}]]"))
        self.assertFalse(MODULE.is_balanced("{(())[]}}"))
        self.assertFalse(MODULE.is_balanced("}"))
        self.assertFalse(MODULE.is_balanced("[]]]]]]]]](()()()()"))
        self.assertFalse(MODULE.is_balanced("{{}}}"))
        self.assertFalse(MODULE.is_balanced("[][][][][]}"))

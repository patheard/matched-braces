import unittest

MODULE = __import__("matched_braces")


class MatchedBracesTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_valid_braces(self):
        self.assertTrue(MODULE.match_braces("(())"))
        self.assertTrue(MODULE.match_braces("([])"))
        self.assertTrue(MODULE.match_braces("{(())[]}"))
        self.assertTrue(MODULE.match_braces("()[]{}"))
        self.assertTrue(MODULE.match_braces("[hello]"))
        self.assertTrue(MODULE.match_braces("{general kenobi}"))

    def test_invalid_braces(self):
        self.assertFalse(MODULE.match_braces("(d))"))
        self.assertFalse(MODULE.match_braces("([]"))
        self.assertFalse(MODULE.match_braces("{(())[]}}"))
        self.assertFalse(MODULE.match_braces("}"))
        self.assertFalse(MODULE.match_braces("[]]]]]]]]](()()()()"))
        self.assertFalse(MODULE.match_braces("{{}}}"))
        self.assertFalse(MODULE.match_braces("[][][][][]}"))

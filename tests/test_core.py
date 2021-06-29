import unittest


class ExconvcsvExecuteTest(unittest.TestCase):
    def test_firstchk_execute(self):
        from exconvcsv.core import exconvcsv_execute

        self.assertTrue(exconvcsv_execute())

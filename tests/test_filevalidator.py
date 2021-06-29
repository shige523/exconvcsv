import unittest
import pathlib


class FileValidator_chk_dir_Test(unittest.TestCase):
    def tearDown(self):
        outputdir = pathlib.Path("testdir")
        outputdir.rmdir()

    def test_chk_dir_no_exist(self):
        from exconvcsv.filevalidator import chk_dir

        outputdir = pathlib.Path("testdir")
        chk_dir("testdir")
        self.assertTrue(outputdir.exists())


class FileValidator_chk_target_file_Test(unittest.TestCase):
    def test_chk_target_extension_false(self):
        from exconvcsv.filevalidator import chk_target_extension

        dirname = "input"
        extensions = "*.txt"
        self.assertFalse(chk_target_extension(dirname, extensions))

    def test_chk_target_extension_true(self):
        from exconvcsv.filevalidator import chk_target_extension

        dirname = "input"
        self.assertTrue(chk_target_extension(dirname, "*.xls"))


class FileValidator_chk_prepare_Test(unittest.TestCase):
    def test_chk_target_extension_not_exist_inputdir(self):
        from exconvcsv.filevalidator import chk_prepare

        self.assertFalse(chk_prepare("output", "test_input", "*.xls"))

    def test_chk_target_extension_exist_targetfile(self):
        from exconvcsv.filevalidator import chk_prepare

        self.assertTrue(chk_prepare("output", "input", "*.xls"))

    def test_chk_target_extension_not_exist_targetfile(self):
        from exconvcsv.filevalidator import chk_prepare

        self.assertFalse(chk_prepare("output", "input", "*.txt"))

    def test_chk_target_extension_exist_multi_targetfile(self):
        from exconvcsv.filevalidator import chk_prepare

        self.assertTrue(chk_prepare("output", "input", "*.xls", "*.xlsx"))

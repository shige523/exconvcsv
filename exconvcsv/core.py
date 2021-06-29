from exconvcsv.filevalidator import chk_prepare


def exconvcsv_execute():

    if chk_prepare("output", "input", "*.xls", "*.xlsx") == False:
        return False

    return True


if __name__ == "__main__":
    exconvcsv_execute()

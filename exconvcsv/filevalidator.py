import pathlib

"""[directory and file check]"""


def chk_dir(dirname):
    """check directory exists

    Args:
        dirname ([string]): [dirname]
    """
    p = pathlib.Path(dirname)
    if p.exists() == False:
        p.mkdir()


def chk_target_extension(dirname, ext):
    """[check target file's extension in directory]

    Args:
        dirname ([string]): [tartet directory]
        ext ([string]): [target extension]

    Returns:
        [bool]: [True:target file is exists]
    """
    p = pathlib.Path(dirname)
    target_file_list = []

    [target_file_list.append(filepath) for filepath in p.glob(ext)]

    if len(target_file_list) > 0:
        return True

    return False


def chk_prepare(outputdirname, inputdirname, *extensions):

    chk_dir(outputdirname)

    p = pathlib.Path(inputdirname)

    if p.exists() == False:
        print("inputフォルダがない")
        return False

    for ext in extensions:
        print(ext)
        if chk_target_extension(inputdirname, ext) == True:
            return True

    print("処理対象のファイルがない")
    return False

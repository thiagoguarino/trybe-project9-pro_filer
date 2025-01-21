from pro_filer.actions.main_actions import show_details
from unittest.mock import patch

# made by Thiago Martins Guarino

# Arrange
# Act
# Assert


def exists_mock(x):
    return True


def getsize_mock(x):
    return 22438


def isdir_mock(x):
    return False


def splitext_mock(x):
    return (x, '.png')


def getmtime_mock(x):
    return 1675023065


def isdir_mockz(x):
    return True


def splitext_mockz(x):
    return (x, '')


def test_show_details(capsys):
    context = {"base_path": "/home/trybe/Downloads/Trybe_logo.png"}

    with patch('os.path.exists', exists_mock), \
         patch('os.path.getsize', getsize_mock), \
         patch('os.path.isdir', isdir_mock), \
         patch('os.path.splitext', splitext_mock), \
         patch('os.path.getmtime', getmtime_mock):

        show_details(context)

    captured = capsys.readouterr()

    expected_output = """File name: Trybe_logo.png
File size in bytes: 22438
File type: file
File extension: .png
Last modified date: 2023-01-29\n"""

    assert captured.out == expected_output


def test_show_details_directory(capsys):
    context = {"base_path": "/home/trybe/Downloads"}

    with patch('os.path.exists', exists_mock), \
         patch('os.path.getsize', getsize_mock), \
         patch('os.path.isdir', isdir_mockz), \
         patch('os.path.splitext', splitext_mockz), \
         patch('os.path.getmtime', getmtime_mock):

        show_details(context)

    captured = capsys.readouterr()

    expected_output = """File name: Downloads
File size in bytes: 22438
File type: directory
File extension: [no extension]
Last modified date: 2023-01-29\n"""

    assert captured.out == expected_output


def test_show_details_no_file(capsys):
    context = {"base_path": "/home/trybe/????.txt"}

    show_details(context)

    captured = capsys.readouterr()

    expected_output = "File '????.txt' does not exist\n"

    assert captured.out == expected_output

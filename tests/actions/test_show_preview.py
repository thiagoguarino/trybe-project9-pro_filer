from pro_filer.actions.main_actions import show_preview

# made by Thiago Martins Guarino

# Arrange
# Act
# Assert


def test_show_preview(capsys):
    context = {
        "all_files": [
            "one.py",
            "two.py",
            "three.py"
        ],
        "all_dirs": ["src", "src/utils"]
    }

    expected_output = (
        "Found 3 files and 2 directories\n"
        "First 5 files: ['one.py', 'two.py', 'three.py']\n"
        "First 5 directories: ['src', 'src/utils']\n"
    )

    show_preview(context)

    captured = capsys.readouterr()

    assert captured.out == expected_output


def test_show_preview_empty_context(capsys):
    context = {"all_files": [], "all_dirs": []}

    show_preview(context)

    captured = capsys.readouterr()

    assert captured.out.strip() == "Found 0 files and 0 directories"


def test_show_preview_more_items(capsys):
    context = {
        "all_files": [
            "one.py",
            "two.py",
            "thr.py",
            "four.py",
            "five.py",
            "six.py"
        ],
        "all_dirs": [
          "src",
          "util", "tests", "confs", "vws"
        ]
    }

    expected_output = (
        "Found 6 files and 5 directories\n"
        "First 5 files: ['one.py', 'two.py', 'thr.py', 'four.py', 'five.py']\n"
        "First 5 directories: ['src', 'util', 'tests', 'confs', 'vws']\n"
    )

    show_preview(context)

    captured = capsys.readouterr()

    assert captured.out == expected_output

from pro_filer.actions.main_actions import find_duplicate_files
import pytest

# made by Thiago Martins Guarino

# Arrange
# Act
# Assert


def test_find_duplicate(tmp_path):
    test_dir = tmp_path / "test"
    dup_dir = tmp_path / "dup"
    dup_dir.mkdir()
    test_dir.mkdir()

    file_one = test_dir / '1.txt'
    file_two = test_dir / '2.txt'
    dup_one = dup_dir / '1.txt'
    file_one.write_text("one")
    dup_one.write_text("one")
    file_two.write_text("two")

    context = {
        "all_files":
        [
            f"{test_dir}/1.txt",
            f"{test_dir}/2.txt",
            f"{dup_dir}/1.txt",
        ]
    }

    result = find_duplicate_files(context)

    files = [x.split('/')[-1] for x in result[0]]
    assert '1.txt' in files
    assert '2.txt' not in files


def test_non_existent_file(tmp_path):
    test_dir = tmp_path / "test"
    test_dir.mkdir()
    one = test_dir / "one.txt"
    one.write_text("one")

    context = {
        "all_files":
        [
            "not.txt",
            f"{test_dir}/one.txt"
        ]
    }

    with pytest.raises(ValueError):
        find_duplicate_files(context)

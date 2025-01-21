from pro_filer.actions.main_actions import show_disk_usage
import pytest

# made by Thiago Martins Guarino

# Arrange
# Act
# Assert


@pytest.fixture
def get_context(faker, tmp_path):
    seed = "Trybe"

    faker.seed_instance(seed)

    files = list()

    for _ in range(3):
        name_file = faker.file_name(category='text', extension='txt')

        tmp_path_file_name = tmp_path / name_file

        tmp_path_file_name.touch()

        files.append(tmp_path_file_name.__str__())

        with open(tmp_path_file_name.__str__(), 'w') as writer:
            writer.write(faker.text())

    return {"all_files": files}


def test_show_disk_usage(get_context, capsys):
    context = get_context

    show_disk_usage(context)

    out_list = capsys.readouterr().out.split("\n")

    assert "171 (42%)" in out_list[0]

    assert "123 (30%)" in out_list[1]

    assert "112 (27%)" in out_list[2]

    assert "Total size: 406" == out_list[3]


def test_show_disk_usage_no_files(capsys):

    show_disk_usage({"all_files": []})

    assert capsys.readouterr().out == "Total size: 0\n"

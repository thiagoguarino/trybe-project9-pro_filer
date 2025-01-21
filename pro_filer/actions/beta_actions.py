"""Arquivo que estudantes devem editar"""


# made by Thiago Martins Guarino

def show_deepest_file(context):
    if not context["all_files"]:
        print("No files found")
    else:
        maior = 0
        deepest_file = ""

        for elem in context["all_files"]:
            if elem.count('/') > maior:
                deepest_file = elem
                maior = elem.count('/')

        print(f"Deepest file: {deepest_file}")


# made by Thiago Martins Guarino

def find_file_by_name(context, search_term, case_sensitive=True):
    if not search_term:
        return []

    found_files = []

    for path in context["all_files"]:
        file_name = path.split("/")[-1]

        if not case_sensitive:
            file_name = file_name.lower()
            search_term = search_term.lower()

        if search_term in file_name:
            found_files.append(path)

    return found_files

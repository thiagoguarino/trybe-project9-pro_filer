# Project ProFiler

<details>
<summary><strong>🧑‍💻 O que deverá ser desenvolvido</strong></summary>

Você irá trabalhar com uma aplicação com uma interface de linha de comando (CLI) que recebe como entrada um caminho (diretório ou arquivo) e gera um relatório com informações sobre o caminho informado.

Para executar a aplicação:

1. Siga os passos do tópico [**🏕️ Ambiente Virtual**]
2. Configure o auto-complete da aplicação com o comando `pro-filer --install-completion` e reinicie o terminal;
3. Execute o comando `pro-filer` seguido de um caminho (diretório ou arquivo) e uma ação. Por exemplo:

```bash
pro-filer . preview
```

![pro-filer preview](./images/pro-filer-preview.gif)

A aplicação já está funcional, mas possui dois problemas:

1. alguns bugs precisam ser corrigidos;
2. mais testes precisam ser implementados.

Você deverá corrigir os bugs e implementar os testes para garantir que a aplicação funcione corretamente. Será o momento de aplicar tudo o que você aprendeu sobre debugging e testes automatizados em Python!

</details>
  
<details>
  <summary><strong>🏕️ Habilidades a serem trabalhadas </strong></summary>

- Encontrar bugs no código de uma aplicação escrita em Python;
- Corrigir bugs no código de uma aplicação escrita em Python;
- Criar testes para uma aplicação escrita em Python;
- Utilizar o `pytest` para criar testes automatizados em uma aplicação escrita em Python.

</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary>
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando `deactivate`. Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` instalará todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`. Se você desejar instalar uma nova dependência, basta adicioná-la no arquivo `dev-requirements.txt` e executar o comando `python3 -m pip install -r dev-requirements.txt` novamente.

  Se o VS Code não reconhecer as dependências instaladas no ambiente virtual criado, será necessário informar o caminho do interpretador Python. Para isso, abra o VS Code e pressione `Ctrl + Shift + P` (no Mac, `Cmd + Shift + P`) e digite `Python: Select Interpreter`. Selecione o interpretador que possui o caminho `./.venv/bin/python` no nome.
</details>

<details>
<summary><strong>🎛 Linter</strong></summary>

Para garantir a qualidade do código, vamos utilizar nesse projeto o linter `Flake8`. Assim o código estará alinhado com as boas práticas de desenvolvimento, sendo mais legível e de fácil manutenção! Para poder executar o `Flake8`, certifique-se de ter seguido os passos do tópico [**🏕️ Ambiente Virtual**] dentro do repositório.

Para rodá-lo localmente no repositório, execute o comando a seguir:

```bash
python3 -m flake8
```

Se a análise do `Flake8` encontrar problemas no seu código, tais problemas serão mostrados no seu terminal. Se não houver problema no seu código, nada será impresso no seu terminal.

Você pode também pode contar com a ajuda do `Flake8` no `VSCode`. Para isso, basta instalar a [extensão oficial do VS Code para a linguagem Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python).

</details>

<details>
  <summary><strong>🛠 Testes</strong></summary>

  Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  <strong>Executar os testes</strong>

  ```bash
  python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o `pytest`. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv --continue-on-collection-errors
  ```

  O `pytest` possui diversos parâmetros que podem ser utilizados para executar os testes de diferentes formas. Alguns exemplos são:

  ```bash
  python3 -m pytest tests/test_nome_do_arquivo.py  # Executa todos os testes do arquivo de testes especificado
  python3 -m pytest tests/test_nome_do_arquivo.py::test_nome_do_teste  # Executa apenas o teste especificado
  python3 -m pytest -k expressao  # Executa apenas os testes que contém a expressão informada como substring
  python3 -m pytest -x  # Executa os testes até encontrar o primeiro erro
  ```

  Você pode combinar os parâmetros para executar os testes da forma que desejar! Para mais informações, consulte a [documentação do pytest](https://docs.pytest.org/en/7.3.x/contents.html).
</details>

## Requisitos do projeto

<details>

<summary> 1. Elimine o(s) bug(s) da função `show_deepest_file`</summary>

### 1. Elimine o(s) bug(s) da função `show_deepest_file`

> Arquivo a ser alterado: `pro_filer/actions/beta_actions.py`

Você está colaborando com a comunidade open-source e recebeu uma tarefa de corrigir bugs em algumas funções!

Encontre e corrija o(s) bug(s) da função `show_deepest_file` para que ela informe corretamente o caminho arquivo mais profundo dentro do diretório informado.

Execute os testes do arquivo `tests/actions/test_deepest_file.py` para te ajudar a encontrar o(s) bug(s): **você saberá que o(s) bug(s) foi(ram) corrigido(s) quando todos os testes desse arquivo passarem.**

<details>

<summary> 🤖 Comportamento esperado da função <code>show_deepest_file</code> </summary>

A função `show_deepest_file` deve receber um dicionário `context` com a chave `all_files` e imprime na saída padrão (`stdout`) o caminho do arquivo mais profundo dentro do diretório informado. A chave `all_files` armazena uma lista de strings, que representam os caminhos de todos os arquivos dentro de um diretório.

**O caminho mais profundo** será o caminho que possui a maior quantidade de diretórios aninhados. Considere esse exemplo:

```python
context = {
    "all_files": [
        "/home/trybe/Downloads/trybe_logo.png",
        "/home/trybe/Documents/aula/python/tests.txt",
    ]
}

show_deepest_file(context)
# Saída:
# Deepest file: /home/trybe/Documents/aula/python/tests.txt

context = {
    "all_files": []
}

show_deepest_file(context)
# Saída:
# No files found
```

Na primeira chamada, o arquivo com caminho mais profundo é `/home/trybe/Documents/aula/python/tests.txt`, pois ele possui 5 diretórios aninhados: `home`, `trybe` e `Documents`, `aula` e `python`.

Na segunda chamada, não há arquivos dentro do diretório informado, então a função imprime `No files found`.

> **De olho na dica 👀:** Essa função pode ser acionada pelo comando `pro-filer <caminho> deepest-file`!

</details>
</details>

<details>

<summary>2. Elimine o(s) bug(s) da função `find_file_by_name`</summary>

> Arquivo a ser alterado: `pro_filer/actions/beta_actions.py`

Com a resolução do último bug, as pessoas responsáveis pela manutenção do projeto ficaram extremamente satisfeitas e agora estão solicitando uma nova tarefa para você!

Encontre e corrija o(s) bug(s) da função `find_file_by_name` para que ela faça corretamente a busca de arquivos baseada em um termo de busca.

Execute os testes do arquivo `tests/actions/test_find_file_by_name.py` para te ajudar a encontrar o(s) bug(s): **você saberá que o(s) bug(s) foi(ram) corrigido(s) quando todos os testes desse arquivo passarem.**
<details>

<summary> 🤖 Comportamento esperado da função <code>find_file_by_name</code> </summary>

A função `find_file_by_name` deve receber como parâmetro:

- um dicionário `context` com a chave `all_files`, que armazena uma lista de strings, representando os caminhos de todos os arquivos dentro de um diretório
- uma _string_ `search_term` com a string a ser buscada
- (opcional) um _booleano_ `case_sensitive` que indica se a busca deve ser sensível a maiúsculas e minúsculas ou não. O valor padrão é `True`.

O retorno será uma lista de strings com os caminhos dos arquivos que possuem o termo buscado em seu nome.

**A busca é realizada** considerando apenas o nome do arquivo (com sua extensão), ignorando o nome das pastas. Considere esse exemplo:

```python
context = {
    "all_files": [
        "/home/trybe/Downloads/Trybe_logo.png",
        "/home/trybe/Documents/aula/python/tests.py",
    ]
}


find_file_by_name(context, '.py')
# Retorno: ["/home/trybe/Documents/aula/python/tests.py"]

find_file_by_name(context, 'trybe', case_sensitive=False)
# Retorno: ["/home/trybe/Downloads/Trybe_logo.png"]

context = {
    "all_files": []
}

find_file_by_name(context, "trybe")
# Retorno: []
```

Na 1ª chamada, apenas o segundo arquivo é encontrado pois apenas ele possui o termo `.py` em seu nome.

Já na 2ª chamada, apenas o primeiro arquivo é encontrado, pois apenas ele possui o termo `Trybe` em seu nome. Como `case_sensitive` foi passado como `False`, a busca não diferencia maiúsculas de minúsculas.

E na 3ª chamada, não há arquivos dentro do dicionário `context`, então a função retorna uma lista vazia.

> **De olho na dica 👀:** Essa função pode ser acionada pelo comando `pro-filer <caminho> search-file <termo_de_busca>`!

</details>
</details>

<details>

<summary>3. Crie testes para a função `show_preview`</summary>

> Arquivo a ser alterado: `tests/actions/test_show_preview.py`

Agora que você já corrigiu bugs do projeto e mostrou que consegue trabalhar com o `Pytest`, as pessoas encarregadas do projeto solicitaram que você desenvolva testes para as funções que ainda não foram testadas!

Implemente testes para a função `show_preview` do arquivo `pro_filer/actions/main_actions.py` para garantir que ela está funcionando corretamente. **Os testes devem ser implementados no arquivo `tests/actions/test_show_preview.py`. Você pode criar quantas funções de teste desejar, desde que respeite o padrão do `Pytest`.**

<details>

<summary> 🤖 Comportamento esperado da função <code>show_preview</code> </summary>

A função `show_preview` deve receber como parâmetro um dicionário `context` com as chaves `all_files` e `all_dirs`:

- `all_files` armazena uma lista de strings, representando os caminhos de todos os arquivos dentro de um diretório;
- `all_dirs` armazena uma lista de strings, representando os caminhos de todos os diretórios dentro de um diretório.

A função imprime na saída padrão (`stdout`):

- A quantidade de arquivos e diretórios listados;
- Se houver algum dado nas chaves do dicionário `context`, os 5 primeiros arquivos listados;
- Se houver algum dado nas chaves do dicionário `context`, os 5 primeiros diretórios listados.

Considere esse exemplo:

```python
context = {
    "all_files": ["src/__init__.py", "src/app.py", "src/utils/__init__.py"],
    "all_dirs": ["src", "src/utils"]
}


show_preview(context)
# Saída:
# Found 3 files and 2 directories
# First 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py']
# First 5 directories: ['src', 'src/utils']


context = {
    "all_files": [],
    "all_dirs": []
}


show_preview(context)
# Saída:
# Found 0 files and 0 directories
```

Na 1 primeira chamada, a função imprime as informações como.

Na 2ª chamada, não há arquivos listados em `all_files`, então a função imprime apenas o espaço total ocupado: `0`.

> **De olho na dica 👀:** Essa função pode ser acionada pelo comando `pro-filer <caminho> preview`!

> **De olho na dica 👀:** Execute o teste da Trybe `tests/trybe/show_preview_test.py` para verificar se seus testes cobrem todos os casos de uso previstos!

</details>

<details>
  <summary> 📌 Como seu teste é avaliado </summary>

O **teste da Trybe** irá avaliar se os **seus testes** estão passando conforme seu objetivo, e se estão falhando em alguns casos que deveria falhar.

Executaremos as funções de teste que você escrever no arquivo indicado (`tests/actions/test_show_preview.py`) substituindo a função sendo testada (`show_preview`) por outras implementações "quebradas".

❌ Se seu teste **aprovar** alguma das implementações "quebradas", **o teste da Trybe FALHARÁ**, indicando que o requisito **não está** aprovado.

✅ Se seu teste **rejeitar** todas as implementações "quebradas", **o teste da Trybe PASSARÁ**, indicando que o requisito **está** aprovado.

</details>
</details>
</details>

<details>

<summary>4. Crie testes para a função `show_details`</summary>


> Arquivo a ser alterado: `tests/actions/test_show_details.py`

Parabéns por todas as contribuições feitas até aqui! O time responsável pelo projeto está gostando do seu trabalho e tem uma nova tarefa para você: criar testes para outra funcionalidade!

Implemente testes para a função `show_details` do arquivo `pro_filer/actions/main_actions.py` para garantir que ela está funcionando corretamente. **Os testes devem ser implementados no arquivo `tests/actions/test_show_details.py`. Você pode criar quantas funções de teste desejar, desde que respeite o padrão do `Pytest`.**

<details>

<summary> 🤖 Comportamento esperado da função <code>show_details</code> </summary>

A função `show_details` deve receber como parâmetro um dicionário `context` com as chave `base_path`, que armazena uma string representando o caminho do arquivo (ou diretório) que deve ser analisado. A função então imprime na saída padrão (`stdout`) as seguintes informações:

- O nome do arquivo informado;
- O tamanho ocupado pelo arquivo informado;
- O tipo do arquivo informado (`file` ou `directory`);
- A extensão do arquivo informado (ou `[no extension]` caso não possua extensão);
- A data da última modificação do arquivo informado, no formato `yyyy-mm-dd`.

```python
context = {
    "base_path": "/home/trybe/Downloads/Trybe_logo.png"
}


show_details(context)
# Saída:
# File name: Trybe_logo.png
# File size in bytes: 22438
# File type: file
# File extension: .png
# Last modified date: 2023-06-13


context = {
    "base_path": "/home/trybe/????"
}


show_details(context)
# Saída:
# File '????' does not exist
```

Na 1ª chamada, o arquivo é um arquivo comum, então a função imprime `file` como tipo do arquivo e `.png` como extensão.

Na 2ª chamada, o arquivo informado não existe, então a função imprime `File '????' does not exist`.

> **De olho na dica 👀:** Essa função pode ser acionada pelo comando `pro-filer <caminho> file-details`!

> **De olho na dica 👀:** Execute o teste da Trybe `tests/trybe/show_details_test.py` para verificar se seus testes cobrem todos os casos de uso previstos!

</details>

<details>
  <summary> 📌 Como seu teste é avaliado </summary>

O **teste da Trybe** irá avaliar se os **seus testes** estão passando conforme seu objetivo, e se estão falhando em alguns casos que deveria falhar.

Executaremos as funções de teste que você escrever no arquivo indicado (`tests/actions/test_show_details.py`) substituindo a função sendo testada (`show_details`) por outras implementações "quebradas".

❌ Se seu teste **aprovar** alguma das implementações "quebradas", **o teste da Trybe FALHARÁ**, indicando que o requisito **não está** aprovado.

✅ Se seu teste **rejeitar** todas as implementações "quebradas", **o teste da Trybe PASSARÁ**, indicando que o requisito **está** aprovado.

</details>
</details>



<details>
  <summary>5. Crie testes para a função `show_disk_usage`</summary>

> Arquivo a ser alterado: `tests/actions/test_show_disk_usage.py`

Continuando suas contribuições no projeto, precisamos que você crie testes para mais uma funcionalidade importante do projeto!

Implemente testes para a função `show_disk_usage` do arquivo `pro_filer/actions/main_actions.py` para garantir que ela está funcionando corretamente. **Os testes devem ser implementados no arquivo `tests/actions/test_show_disk_usage.py`. Você pode criar quantas funções de teste desejar, desde que respeite o padrão do `Pytest`.**

<details>

<summary> 🤖 Comportamento esperado da função <code>show_disk_usage</code> </summary>

A função `show_disk_usage` deve receber como parâmetro um dicionário `context` com a chave `all_files`, que armazena uma lista de strings representando os caminhos de todos os arquivos dentro de um diretório. A função então imprime na saída padrão (`stdout`) o espaço total ocupado por todos os arquivos dentro do diretório informado.

A função então imprime na saída padrão (`stdout`) as seguintes informações:

- Para cada arquivo listado em `all_files`:
  - O caminho do arquivo;
  - O espaço ocupado pelo arquivo, em bytes;
  - A porcentagem do tamanho ocupado pelo arquivo em relação ao espaço total ocupado (por todos os arquivos listados em `all_files`);
- O espaço total ocupado por todos os arquivos listados em `all_files`, em bytes.

**A listagem de arquivos** é realizada em ordem decrescente de espaço ocupado. Considere esse exemplo:

```python
context = {
    "all_files": [
        "src/app.py",
        "src/__init__.py",
    ]
}


show_disk_usage(context)
# Saída:
# 'src/app.py':                                                          2849 (100%)
# 'src/__init__.py':                                                     0 (0%)
# Total size: 2849

context = {
    "all_files": []
}


show_disk_usage(context)
# Saída:
# Total size: 0
```

Na 1 primeira chamada, a função imprime a listagem de arquivos e seu tamanho em _bytes_ com a porcentagem do total e, ao final, o espaço total ocupado pelos arquivos listados.

Na 2ª chamada, não há arquivos listados em `all_files`, então a função imprime apenas o espaço total ocupado: `0`.

**Atenção ⚠️:** Como pode ser observado na implementação de `show_disk_usage`, a formatação de cada linha da listagem de arquivos é feita com auxílio da função `_get_printable_file_path`. Não se preocupe em validar o comportamento dessa função, você pode criar um dublê de teste para ela.

> **De olho na dica 👀:** Essa função pode ser acionada pelo comando `pro-filer <caminho> disk-usage`!

> **De olho na dica 👀:** Execute o teste da Trybe `tests/trybe/show_disk_usage_test.py` para verificar se seus testes cobrem todos os casos de uso previstos!

<details>
  <summary> 📌 Como seu teste é avaliado </summary>

O **teste da Trybe** irá avaliar se os **seus testes** estão passando conforme seu objetivo, e se estão falhando em alguns casos que deveria falhar.

Executaremos as funções de teste que você escrever no arquivo indicado (`tests/actions/test_show_disk_usage.py`) substituindo a função sendo testada (`show_disk_usage`) por outras implementações "quebradas".

❌ Se seu teste **aprovar** alguma das implementações "quebradas", **o teste da Trybe FALHARÁ**, indicando que o requisito **não está** aprovado.

✅ Se seu teste **rejeitar** todas as implementações "quebradas", **o teste da Trybe PASSARÁ**, indicando que o requisito **está** aprovado.

</details>
</details>
</details>

<details>
  <summary>6. Crie testes para a função `find_duplicate_files`</summary>

> Arquivo a ser alterado: `tests/actions/test_find_duplicate_files.py`

Para concluir sua participação na temporada de melhorias, as pessoas responsáveis pelo projeto têm uma última tarefa para você: criar testes para uma funcionalidade final!

Implemente testes para a função `find_duplicate_files` do arquivo `pro_filer/actions/main_actions.py` para garantir que ela está funcionando corretamente. **Os testes devem ser implementados no arquivo `tests/actions/test_find_duplicate_files.py`. Você pode criar quantas funções de teste desejar, desde que respeite o padrão do `Pytest`.**

<details>
<summary> 🤖 Comportamento esperado da função <code>find_duplicate_files</code> </summary>

A função `find_duplicate_files` deve receber como parâmetro um dicionário `context` com a chave `all_files`, que armazena uma lista de strings representando os caminhos de todos os arquivos dentro de um diretório.

A função então retorna uma lista de tuplas com os pares de arquivos que possuem o mesmo conteúdo.

Considere esse exemplo:

```python
context = {
    "all_files": [
        ".gitignore",
        "src/app.py",
        "src/utils/__init__.py",
    ]
}


find_duplicate_files(context)
# Retorno:
# []

context = {
    "all_files": [
        "./tests/__init__.py",
        "./tests/actions/__init__.py",
        "./pro_filer/__init__.py",
    ]
}

find_duplicate_files(context)
# Retorno:
# [
#     ('./tests/__init__.py', './tests/actions/__init__.py'),
#     ('./tests/__init__.py', './pro_filer/__init__.py'),
#     ('./tests/actions/__init__.py', './pro_filer/__init__.py')
# ]
```

Na 1 primeira chamada, o resultado é uma lista vazia pois não há arquivos duplicados: todos os arquivos possuem conteúdos diferentes.

Na 2ª chamada, o resultado é uma lista de tuplas com todos os pares de arquivos duplicados. Como todos os arquivos possuem o mesmo conteúdo, todos os pares são retornados.

> **Atenção ⚠️:** Como pode ser observado na implementação de `find_duplicate_files`, a comparação de conteúdo de arquivos é feita com auxílio da função `filecmp.cmp(...)`. Essa função é nativa do Python, e compara o conteúdo dos arquivos (retornando `True` se forem iguais). Caso algum dos arquivos não exista, é levantada uma exceção `FileNotFoundError`.

Caso a exceção `FileNotFoundError` seja levantada na chamada de `filecmp.cmp(...)`, a função `find_duplicate_files` levantará uma exceção `ValueError`. Você deve testar se a exceção `ValueError` é levantada caso algum arquivo em `all_files` não exista.

> **De olho na dica 👀:** Essa função pode ser acionada pelo comando `pro-filer <caminho> find-duplicate`!

> **De olho na dica 👀:** Execute o teste da Trybe `tests/trybe/find_duplicate_test.py` para verificar se seus testes cobrem todos os casos de uso previstos!

</details>

<details>
  <summary> 📌 Como seu teste é avaliado </summary>
</details>

Executaremos as funções de teste que você escrever no arquivo indicado (`tests/actions/test_show_disk_usage.py`) substituindo a função sendo testada (`show_disk_usage`) por outras implementações "quebradas".

❌ Se seu teste **aprovar** alguma das implementações "quebradas", **o teste da Trybe FALHARÁ**, indicando que o requisito **não está** aprovado.

✅ Se seu teste **rejeitar** todas as implementações "quebradas", **o teste da Trybe PASSARÁ**, indicando que o requisito **está** aprovado.


</details>
</details>
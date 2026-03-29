def output_to_terminal(text):
    """
    Виводить текст у консоль.

    Args:
        text (str): текст для виводу.
    """
    print(text)


def output_to_file_builtin(file_path, text):
    """
    Записує текст у файл за допомогою вбудованих можливостей Python.

    Args:
        file_path (str): шлях до файлу.
        text (str): текст для запису.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)
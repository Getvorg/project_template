def input_from_terminal():
    """
    Зчитує текст, введений користувачем з консолі.

    Returns:
        str: текст, введений користувачем.
    """
    return input("Введіть текст: ")


def input_from_file_builtin(file_path):
    """
    Зчитує текст із файлу за допомогою вбудованих можливостей Python.

    Args:
        file_path (str): шлях до файлу.

    Returns:
        str: вміст файлу.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def input_from_file_pandas(file_path):
    """
    Зчитує текст із файлу за допомогою бібліотеки pandas.

    Args:
        file_path (str): шлях до файлу.

    Returns:
        str: текстовий вміст файлу.
    """
    import pandas as pd

    data = pd.read_csv(file_path)

    if data.empty:
        return ""

    return str(data["text"].iloc[0])
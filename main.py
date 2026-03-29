from app.io.input import (
    input_from_terminal,
    input_from_file_builtin,
    input_from_file_pandas,
)
from app.io.output import output_to_terminal, output_to_file_builtin


def main():
    terminal_text = input_from_terminal()
    file_text_builtin = input_from_file_builtin("data/input.txt")
    file_text_pandas = input_from_file_pandas("data/input.csv")

    output_to_terminal("Текст із консолі:")
    output_to_terminal(terminal_text)

    output_to_terminal("Текст із файлу (builtin):")
    output_to_terminal(file_text_builtin)

    output_to_terminal("Текст із файлу (pandas):")
    output_to_terminal(file_text_pandas)

    result_text = (
        f"Текст із консолі:\n{terminal_text}\n\n"
        f"Текст із файлу (builtin):\n{file_text_builtin}\n\n"
        f"Текст із файлу (pandas):\n{file_text_pandas}\n"
    )

    output_to_file_builtin("data/output.txt", result_text)


if __name__ == "__main__":
    main()
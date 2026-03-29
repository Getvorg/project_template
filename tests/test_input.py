import unittest
from pathlib import Path

from app.io.input import input_from_file_builtin, input_from_file_pandas


class TestInputFunctions(unittest.TestCase):
    def setUp(self):
        self.test_dir = Path(__file__).resolve().parent
        self.txt_file = self.test_dir / "test_input.txt"
        self.csv_file = self.test_dir / "test_input.csv"
        self.empty_txt_file = self.test_dir / "empty.txt"
        self.empty_csv_file = self.test_dir / "empty.csv"

        self.txt_file.write_text(
            "Це тестовий текст для builtin.",
            encoding="utf-8"
        )

        self.csv_file.write_text(
            "text\nЦе тестовий текст для pandas",
            encoding="utf-8"
        )

        self.empty_txt_file.write_text("", encoding="utf-8")
        self.empty_csv_file.write_text("text\n", encoding="utf-8")

    def tearDown(self):
        for file_path in [
            self.txt_file,
            self.csv_file,
            self.empty_txt_file,
            self.empty_csv_file,
        ]:
            if file_path.exists():
                file_path.unlink()

    # 3 тести для input_from_file_builtin
    def test_input_from_file_builtin_reads_text(self):
        result = input_from_file_builtin(self.txt_file)
        self.assertEqual(result, "Це тестовий текст для builtin.")

    def test_input_from_file_builtin_reads_empty_file(self):
        result = input_from_file_builtin(self.empty_txt_file)
        self.assertEqual(result, "")

    def test_input_from_file_builtin_raises_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            input_from_file_builtin(self.test_dir / "missing.txt")

    # 3 тести для input_from_file_pandas
    def test_input_from_file_pandas_reads_text(self):
        result = input_from_file_pandas(self.csv_file)
        self.assertEqual(result, "Це тестовий текст для pandas")

    def test_input_from_file_pandas_empty_csv(self):
        result = input_from_file_pandas(self.empty_csv_file)
        self.assertEqual(result, "")

    def test_input_from_file_pandas_raises_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            input_from_file_pandas(self.test_dir / "missing.csv")


if __name__ == "__main__":
    unittest.main()
# Реализация простого класса для чтения файлов


class FileReader:
    def __init__(self, file_path):
        self._file_path = file_path

    def read(self):
        try:
            with open(self._file_path, 'r', encoding='utf-8', newline='') as fp:
                return fp.read()
        except FileNotFoundError:
            return ''

    def write(self, text):
        with open(self._file_path, 'w', encoding='utf-8', newline='') as fp:
            fp.write(text)

# Пример класса для чтения файла с магическими методами

import os
import uuid
import tempfile


class File:
    def __init__(self, path):
        self._current_position = 0
        self._path = os.path.abspath(path)
        if not os.path.exists(self._path):
            open(self._path, 'w').close()

    def __str__(self):
        return self._path

    def __iter__(self):
        return self

    def __next__(self):
        with open(self._path, 'r') as fp:
            fp.seek(self._current_position)
            line = fp.readline()
            if not line:
                self._current_position = 0
                raise StopIteration('EOF')
            self._current_position = fp.tell()
            return line

    def __add__(self, other):
        new_file = File(os.path.join(tempfile.gettempdir(), str(uuid.uuid4().hex)))
        new_file.write(self.read() + other.read())
        return new_file

    def read(self):
        with open(self._path, 'r') as fp:
            return fp.read()

    def write(self, s):
        with open(self._path, 'w') as fp:
            return fp.write(s)

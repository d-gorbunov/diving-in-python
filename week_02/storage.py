# Пример реализации файлового хранилища

import os
import json
import argparse
import tempfile


class Storage:
    def __init__(self):
        self._storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

    def _get_data(self):
        """
        Получение данных из файла
        :return: словарь с данными
        """
        if not os.path.exists(self._storage_path):
            return dict()

        with open(self._storage_path, 'r') as fp:
            return json.load(fp)

    def read(self, key):
        """
        Чтение значения из файла по ключу
        :param key: название ключа, по которому мы хотим получить данные
        :return:
        """
        data = self._get_data()
        values = data.get(key)
        if not values:
            return
        return ', '.join(values)

    def write(self, key, value):
        """
        Запись значения в файл по ключу
        :param key: ключ, для которого мы хотим записать значение
        :param value: значение для записи
        """
        data = self._get_data()
        if key in data:
            data[key] += [value]
        else:
            data[key] = [value]

        with open(self._storage_path, 'w') as fp:
            json.dump(data, fp, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--key')
    parser.add_argument('--value')
    args = parser.parse_args()
    storage = Storage()
    if args.key and args.value:
        storage.write(args.key, args.value)
    else:
        print(storage.read(args.key))



class JsonOperations:

    @staticmethod
    def read(name, ref='data/'):
        """Читает JSON файл.\n
        Аргументы:\n
        ref - путь к файлу (по умолчанию data/), \n
        name - имя файла без указания формата."""
        from json import load
        with open(ref + name + '.json') as json_import_data:
            data_file = load(json_import_data)
        return data_file

    @staticmethod
    def save(name, file, ref='data/'):
        """Сохраняет значение переменной в JSON файл.\n
        Аргументы: \n
        ref - ссылка на файл, \n
        name - имя файла без указания формата, \n
        file - переменная,
        значение которой сохраняется в JSON файл."""

        from json import dump
        with open(ref + name + '.json', 'w') as add_info_file:
            dump(file, add_info_file)


import json
from json import JSONDecodeError
from pathlib import Path

from narator.exceptions import NaratorException, UnableToReadConfigFile, UnableToWriteConfigFile


class DictionaryFile(dict):
    __slots__ = ('_path',)

    def __init__(self, file_path: str):
        super().__init__()
        self._path = Path(file_path)

        dictionary_data = self._load_data_from_file()
        if dictionary_data:
            super().update(dictionary_data)

    def _load_data_from_file(self) -> dict | None:
        if not self._path.exists():
            return None
        try:
            with open(self._path, 'r') as file:
                return json.load(file)
        except JSONDecodeError:
            return None
        except OSError as e:
            raise UnableToReadConfigFile('Unable to read config file.') from e

    def _save_data_to_file(self, data: dict) -> None:
        self._path.parent.mkdir(parents=True, exist_ok=True)
        try:
            with open(self._path, 'w') as file:
                json.dump(data, file)
        except OSError as e:
            raise UnableToWriteConfigFile('Unable to wrote config file.') from e
        except JSONDecodeError as e:
            raise NaratorException('Config data is not valid json.') from e

    def update(self, **kwargs) -> None:
        super().update(**kwargs)
        self._save_data_to_file(self)

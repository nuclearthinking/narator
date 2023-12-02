from pydantic_settings import BaseSettings

from narator.core.utils import get_config_dir
from narator.core.constants import CONFIG_FILE_NAME
from narator.core.dictionary_file import DictionaryFile


class SettingsFile(BaseSettings):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        file_path = get_config_dir() / CONFIG_FILE_NAME
        self._dictionary_file = DictionaryFile(file_path)
        self._load_settings_from_file()

    def _load_settings_from_file(self):
        if not self._dictionary_file:
            return

        all_settings = self.model_dump()
        defined_settings = self.model_dump(
            exclude_defaults=True,
            exclude_unset=True,
            exclude_none=True,
        )

        for key, value in self._dictionary_file.items():
            if key in defined_settings or key not in all_settings:
                continue
            setattr(self, key, value)

    def save_setting(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        self._dictionary_file.update(**kwargs)

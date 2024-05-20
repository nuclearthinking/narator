from narator.core.settings_file import SettingsFile


class _Settings(SettingsFile):
    yandex_token: str | None = None

    xtts_model_path: str = '/home/nuclearthinking/PycharmProjects/RU-XTTS-DonuModel'
    xtts_config_path: str = 'resources/xtts_ru/config.json'

    default_xtts_model_name: str = 'tts_models/multilingual/multi-dataset/xtts_v2'
    default_xtts_vocoder_name: str = 'vocoder_models/universal/libri-tts/fullband-melgan'


settings = _Settings()

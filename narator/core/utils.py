from pathlib import Path

from narator.core.constants import CONFIG_FILE_NAME


def get_config_dir():
    path = Path.home() / CONFIG_FILE_NAME
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
    return path

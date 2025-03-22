import json
import os


class ConfigReader:
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        self.config_file_path = os.path.join(self.CURRENT_DIR, "config.json")
        self.config_data = self._read_config()

    def _read_config(self):
        with open(self.config_file_path, 'r') as file:
            return json.load(file)

    def get_config(self, section: str = None):
        if section:
            return self.config_data.get(section)
        return self.config_data

    def get_value(self, section: str, key: str):
        section_data = self.get_config(section)
        if section_data is None:
            raise KeyError(f"Секция '{section}' не найдена в конфигурации")
        return section_data.get(key)

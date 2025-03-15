import json
import os


class ConfigReader:
    def __init__(self, config_file_path):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.config_file_path = os.path.join(current_dir, config_file_path)
        self.config_data = self._read_config()

    def _read_config(self):
        try:
            with open(self.config_file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Конфигурационный файл не найден: {self.config_file_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Некорректный формат JSON в файле: {self.config_file_path}")

    def get_config(self, section: str = None):
        if section:
            return self.config_data.get(section)
        return self.config_data

    def get_value(self, section: str, key: str):
        section_data = self.get_config(section)
        if section_data is None:
            raise KeyError(f"Секция '{section}' не найдена в конфигурации")
        return section_data.get(key)

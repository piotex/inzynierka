import json
from os.path import exists


class AppSettings:
    @staticmethod
    def get_default_settings_path() -> str:
        tmp_app_settings = "AppSettings.json"
        return os.path.abspath(os.getcwd()) + "\\static\\" + tmp_app_settings

    @staticmethod
    def read_settings(path: str = get_default_settings_path()) -> AppSettingsModel:
        if not exists(path):
            settings = AppSettingsModel()
            AppSettings.save_settings(settings, path)
            return settings

        with open(path, "r") as file:
            data = json.load(file)
            return AppSettingsModel(**data)

    @staticmethod
    def save_settings(settings: AppSettingsModel, path: str = get_default_settings_path()):
        """Save instance attributes to JSON file."""
        with open(path, "w") as file:
            json.dump(settings.__dict__, file, indent=4)

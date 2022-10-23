import json
from os.path import exists
from models.User import User


class UserList:
    @staticmethod
    def get_default_settings_path() -> str:
        tmp_app_settings = "UserList.json"
        #return os.path.abspath(os.getcwd()) + "\\db\\" + tmp_app_settings
        return "C:\\Users\\pkubon\\OneDrive - Capgemini\\Desktop\\inżynierka_web\\db\\" + tmp_app_settings

    @staticmethod
    def read_user_list(path: str = get_default_settings_path()) -> list[User]:
        if not exists(path):
            usr_list = []
            UserList.save_user_list(usr_list, path)
            return usr_list

        with open(path, "r") as file:
            data = json.load(file)
            return [User(**usr) for usr in data]

    @staticmethod
    def save_user_list(user_list: list[User], path: str = get_default_settings_path()):
        """Save instance attributes to JSON file."""
        with open(path, "w") as file:
            json.dump([usr.__dict__ for usr in user_list], file, indent=4)

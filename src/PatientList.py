import json
import os
from os.path import exists

from models.Patient import Patient


class PatientList:
    @staticmethod
    def get_default_settings_path() -> str:
        tmp_app_settings = "PatientList.json"
        #return os.path.abspath(os.getcwd()) + "\\db\\" + tmp_app_settings
        return "C:\\Users\\pkubon\\OneDrive - Capgemini\\Desktop\\inżynierka_web\\db\\" + tmp_app_settings

    @staticmethod
    def read_patient_list(path: str = get_default_settings_path()) -> list[Patient]:
        if not exists(path):
            pat_list = []
            PatientList.save_patient_list(pat_list, path)
            return pat_list

        with open(path, "r") as file:
            data = json.load(file)
            return [Patient(**patient) for patient in data]

    @staticmethod
    def save_patient_list(patient_list: list[Patient], path: str = get_default_settings_path()):
        """Save instance attributes to JSON file."""
        with open(path, "w") as file:
            json.dump([patient.__dict__ for patient in patient_list], file, indent=4)

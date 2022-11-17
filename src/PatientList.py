import json
import os
from os.path import exists

from models.Exam import Exam
from models.Patient import Patient


class PatientList:
    @staticmethod
    def get_default_settings_path() -> str:
        tmp_app_settings = "PatientList.json"
        return "db/" + tmp_app_settings

    @staticmethod
    def read_patient_list(path: str = get_default_settings_path()) -> list[Patient]:
        if not exists(path):
            pat_list = []
            PatientList.save_patient_list(pat_list, path)
            return pat_list

        with open(path, "r") as file:
            data = json.load(file)
            patient_list = [Patient(**patient) for patient in data]
            for patient in patient_list:
                patient.exam_history = [Exam(**exam) for exam in patient.exam_history]

            return patient_list

    @staticmethod
    def save_patient_list(patient_list: list[Patient], path: str = get_default_settings_path()):
        """Save instance attributes to JSON file."""
        res = []
        for patient in patient_list:
            tmp = patient.__dict__
            tmp["exam_history"] = [exam.__dict__ for exam in patient.exam_history]
            res.append(tmp)

        with open(path, "w") as file:
            json.dump(res, file, indent=4)

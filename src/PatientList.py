import json
import copy
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
                tmp_exam_history = []
                for exam in patient.exam_history:
                    tmp_exam_history.append(Exam(**exam))
                patient.exam_history = tmp_exam_history

            return patient_list

    @staticmethod
    def save_patient_list(patient_list: list[Patient], path: str = get_default_settings_path()):
        """Save instance attributes to JSON file."""

        res = []
        patient_list_copy = copy.deepcopy(patient_list)
        for patient in patient_list_copy:
            tmp = patient.__dict__
            exam_list = []
            for exam in patient.exam_history:
                exam_list.append(exam.get_dict())

            tmp["exam_history"] = exam_list
            res.append(tmp)

        with open(path, "w") as file:
            json.dump(res, file, indent=4)

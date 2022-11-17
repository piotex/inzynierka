from models.Exam import Exam
from src.PatientList import PatientList

from models.Patient import Patient


def test_save_patient_list_1():
    file_path = "C:\\Users\\pkubon\\OneDrive - Capgemini\\Desktop\\inz_web\\db\\test_PatientList.json"
    img_path_def = '../static/def/'
    data = [
        Patient(id=123, name="Peter", surname="Kub-on", image=img_path_def + "def_pers_icon.png",
                exam_history=[
                    Exam(id=1, date="2022-11-20", image="path", result="No demand"),
                ]),
    ]

    tmp = PatientList.save_patient_list(data, path=file_path)
    assert 1 == 1


def test_read_patient_list_1():
    file_path = "C:\\Users\\pkubon\\OneDrive - Capgemini\\Desktop\\inz_web\\db\\test_PatientList.json"
    img_path_def = '../static/def/'
    read_patient_list = PatientList.read_patient_list(path=file_path)
    data = [
        Patient(id=123, name="Peter", surname="Kub-on", image=img_path_def + "def_pers_icon.png",
                exam_history=[
                    Exam(id=1, date="2022-11-20", image="path", result="No demand"),
                ]),
    ]
    print(read_patient_list)

    assert data == read_patient_list


def test_save_patient_list():
    file_path = "C:\\Users\\pkubon\\OneDrive - Capgemini\\Desktop\\inz_web\\db\\test_PatientList.json"
    img_path_def = '../static/def/'
    data = [
        Patient(id=123, name="Peter", surname="Kub-on", image=img_path_def + "def_pers_icon.png",
                exam_history=[
                    Exam(id=1, date="2022-11-20", image="path", result="No demand"),
                    Exam(id=2, date="2022-11-20", image="path", result="No demand"),
                    Exam(id=3, date="2022-11-20", image="path", result="No demand"),
                ]),
        Patient(id=124, name="Adam", surname="Smith", image=img_path_def + "def_pers_icon.png",
                exam_history=[
                    Exam(id=1, date="2022-11-20", image="path", result="No demand"),
                    Exam(id=2, date="2022-11-20", image="path", result="No demand"),
                    Exam(id=3, date="2022-11-20", image="path", result="No demand"),
                ]),
        Patient(id=125, name="Jan", surname="Bond", image=img_path_def + "def_pers_icon.png",
                exam_history=[
                    Exam(id=1, date="2022-11-20", image="path", result="No demand"),
                    Exam(id=2, date="2022-11-20", image="path", result="No demand"),
                    Exam(id=3, date="2022-11-20", image="path", result="No demand"),
                ]),
    ]

    tmp = PatientList.save_patient_list(data, path=file_path)
    assert 1 == 1


def test_read_patient_list():
    file_path = "C:\\Users\\pkubon\\OneDrive - Capgemini\\Desktop\\inz_web\\db\\test_PatientList.json"
    img_path_def = '../static/def/'
    read_patient_list = PatientList.read_patient_list(path=file_path)
    data = [
        Patient(id=123, name="Peter", surname="Kub-on", image=img_path_def + "def_pers_icon.png",
                exam_history=[
                    Exam(id=1, date="2022-11-20", image="path", result="No demand"),
                    Exam(id=2, date="2022-11-20", image="path", result="No demand"),
                    Exam(id=3, date="2022-11-20", image="path", result="No demand"),
                ]),
        Patient(id=124, name="Adam", surname="Smith", image=img_path_def + "def_pers_icon.png",
                exam_history=[
                    Exam(id=1, date="2022-11-20", image="path", result="No demand"),
                    Exam(id=2, date="2022-11-20", image="path", result="No demand"),
                    Exam(id=3, date="2022-11-20", image="path", result="No demand"),
                ]),
        Patient(id=125, name="Jan", surname="Bond", image=img_path_def + "def_pers_icon.png",
                exam_history=[
                    Exam(id=1, date="2022-11-20", image="path", result="No demand"),
                    Exam(id=2, date="2022-11-20", image="path", result="No demand"),
                    Exam(id=3, date="2022-11-20", image="path", result="No demand"),
                ]),
    ]
    assert data == read_patient_list

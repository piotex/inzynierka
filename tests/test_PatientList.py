from src.PatientList import PatientList

from models.Patient import Patient


def test_save_patient_list():
    IMG_PATH_DEF = '../static/def/'
    data = [
        Patient(id=123, name="Peter", surname="Kub-on", image=IMG_PATH_DEF + "def_pers_icon.png",
                exam_history=["11%", "15%", "25%", "30%", "34%", "55%"]),
        Patient(id=124, name="Adam", surname="Smith", image=IMG_PATH_DEF + "def_pers_icon.png",
                exam_history=["211%", "15%", "25%", "30%", "34%", "55%"]),
        Patient(id=125, name="Jan", surname="Bond", image=IMG_PATH_DEF + "def_pers_icon.png",
                exam_history=["311%", "15%", "25%", "30%", "34%", "55%"])
    ]

    tmp = PatientList.save_patient_list(data)
    assert 1 == 1

def test_read_patient_list():
    IMG_PATH_DEF = '../static/def/'
    readed = PatientList.read_patient_list()
    data = [
        Patient(id=123, name="Peter", surname="Kub-on", image=IMG_PATH_DEF + "def_pers_icon.png",
                exam_history=["11%", "15%", "25%", "30%", "34%", "55%"]),
        Patient(id=124, name="Adam", surname="Smith", image=IMG_PATH_DEF + "def_pers_icon.png",
                exam_history=["211%", "15%", "25%", "30%", "34%", "55%"]),
        Patient(id=125, name="Jan", surname="Bond", image=IMG_PATH_DEF + "def_pers_icon.png",
                exam_history=["311%", "15%", "25%", "30%", "34%", "55%"])
    ]
    assert data == readed

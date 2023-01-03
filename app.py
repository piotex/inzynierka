import os
import sys
import cv2
import numpy as np
from flask import Flask, request, render_template
from datetime import datetime
from models.Exam import Exam
from models.Patient import Patient
from src.PatientList import PatientList
from src.UserList import UserList

import tensorflow as tf

PATIENT_LIST = []
LOGGED_USERS_IP_TAB = {}
app = Flask(__name__)


def render_valid_template(template_name, req_ip, **context):
    global LOGGED_USERS_IP_TAB
    if req_ip in LOGGED_USERS_IP_TAB:
        return render_template(template_name, logged_user=LOGGED_USERS_IP_TAB[req_ip], **context)
    return render_template('login.html', **context)


@app.route('/patient_list', methods=['GET', 'POST'])
def patient_list():
    global PATIENT_LIST
    return render_valid_template('patient_list.html', request.remote_addr, patient_list=PATIENT_LIST)


def get_img_path(request_file) -> str:
    try:
        request_file.save(os.path.abspath(os.getcwd() + "/static/uploads/" + request_file.filename))
        return "../static/uploads/" + request_file.filename
    except Exception as e:
        print(e, file=sys.stderr)
        return "../static/def/def_pers_icon.png"


@app.route('/patient_edit', methods=['GET', 'POST'])
def patient_edit():
    global PATIENT_LIST
    tmp_id = int(request.form.get("id"))
    tmp_name = request.form.get("name")
    tmp_surname = request.form.get("surname")
    tmp_image = request.form.get("image_txt")

    if tmp_name is None or tmp_surname is None:
        for elem in PATIENT_LIST:
            if elem.id == tmp_id:
                return render_valid_template('patient_edit.html', request.remote_addr, patient=elem)

    try:
        if request.files["image"].filename != "":
            tmp_image = get_img_path(request.files["image"])

    except Exception as e:
        print(e, file=sys.stderr)

    for i in range(len(PATIENT_LIST)):
        if PATIENT_LIST[i].id == tmp_id:
            # PATIENT_LIST[i] = Patient(id=PATIENT_LIST[i].id, name=tmp_name, surname=tmp_surname, image=tmp_image,
            #                           exam_history=PATIENT_LIST[i].exam_history)
            PATIENT_LIST[i].name = tmp_name
            PATIENT_LIST[i].surname = tmp_surname
            PATIENT_LIST[i].image = tmp_image

            print(PATIENT_LIST[i])
            print(PATIENT_LIST[i])
            print(PATIENT_LIST[i])
            PatientList.save_patient_list(PATIENT_LIST)

    return render_valid_template('patient_list.html', request.remote_addr, patient_list=PATIENT_LIST)


def get_new_patient_id() -> int:
    global PATIENT_LIST
    tmp_id = 0
    for i in range(len(PATIENT_LIST)):
        if PATIENT_LIST[i].id >= tmp_id:
            tmp_id = PATIENT_LIST[i].id + 1
    return tmp_id


@app.route('/patient_add', methods=['GET', 'POST'])
def patient_add():
    global PATIENT_LIST
    tmp_surname = request.form.get("surname")
    tmp_name = request.form.get("name")
    tmp_image = get_img_path(request.files["image"])
    tmp_id = get_new_patient_id()

    patient1 = Patient(id=tmp_id, name=tmp_name, surname=tmp_surname, image=tmp_image, exam_history=[])
    PATIENT_LIST.insert(0, patient1)
    PatientList.save_patient_list(PATIENT_LIST)

    return render_valid_template('patient_list.html', request.remote_addr, patient_list=PATIENT_LIST)


@app.route('/patient_delete', methods=['GET', 'POST'])
def patient_delete():
    global PATIENT_LIST
    tmp_id = int(request.form.get("id"))
    for elem in PATIENT_LIST:
        if elem.id == tmp_id:
            PATIENT_LIST.remove(elem)
            print("pat-----list")
            print(PATIENT_LIST)
            PatientList.save_patient_list(PATIENT_LIST)
            print("pat-----list---2")
            print(PATIENT_LIST)

    return render_valid_template('patient_list.html', request.remote_addr, patient_list=PATIENT_LIST)


@app.route('/patient_history', methods=['GET', 'POST'])
def patient_history():
    global PATIENT_LIST
    tmp_id = int(request.form.get("id"))

    for patient in PATIENT_LIST:
        if patient.id == tmp_id:
            return render_valid_template('patient_history.html', request.remote_addr, patient=patient)

    return render_valid_template('patient_list.html', request.remote_addr, patient_list=PATIENT_LIST)


@app.route('/patient_examine', methods=['GET', 'POST'])
def patient_examine():
    global PATIENT_LIST
    tmpppp_labels = ["Łagodna demencja", "Umiarkowana demencja", "Brak demencji", "Bardzo łagodna demencja"]
    img_array_to_examine = []
    tmp_id = int(request.form.get("id"))
    patient_idx = None
    tmp_response = ""

    for i in range(len(PATIENT_LIST)):
        if PATIENT_LIST[i].id == tmp_id:
            patient_idx = i

    try:
        tmp_file = request.files["brain_image"]
        file_to_examine = os.getcwd() + "/static/uploads/" + tmp_file.filename
        tmp_file.save(file_to_examine)

        img_size = 80
        img_1 = cv2.imread(file_to_examine)
        img_2 = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
        img_array = cv2.resize(img_2, (img_size, img_size))
        img_array_to_examine.append(img_array)
        img_array_to_examine = np.array(img_array_to_examine)

        file_name = os.getcwd() + '/tf_models/altzheimer_inz_model.h5'

        model_loaded = tf.keras.models.load_model(file_name)
        prediction = model_loaded.predict(img_array_to_examine)
        # print(prediction, sys.stderr)
        predicted_label = np.argmax(prediction)

        tmp_response = tmpppp_labels[predicted_label]
        exam = Exam(id=1, result=tmp_response, image=file_to_examine, date=datetime.today().strftime('%Y-%m-%d'))
        PATIENT_LIST[patient_idx].exam_history.insert(0, exam)
        PatientList.save_patient_list(PATIENT_LIST)
    except Exception as e:
        print(e, file=sys.stderr)

    return render_valid_template('patient_examine.html', request.remote_addr, patient=PATIENT_LIST[patient_idx], response=tmp_response)


@app.route('/login', methods=['GET', 'POST'])
def login():
    global PATIENT_LIST, LOGGED_USERS_IP_TAB
    tmp_login = request.form.get("login")
    tmp_pwd = request.form.get("pwd")

    user_list = UserList.read_user_list()
    for user in user_list:
        if user.login == tmp_login and user.password == tmp_pwd:
            LOGGED_USERS_IP_TAB[request.remote_addr] = user
            PATIENT_LIST = PatientList.read_patient_list()
            return render_valid_template('home.html', request.remote_addr)

    if tmp_login is None:
        tmp_login = ""
    if tmp_pwd is None:
        tmp_pwd = ""

    return render_valid_template('login.html', request.remote_addr, login=tmp_login, pwd=tmp_pwd)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    global LOGGED_USERS_IP_TAB
    del LOGGED_USERS_IP_TAB[request.remote_addr]
    return render_valid_template('login.html', "")


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index():
    return render_valid_template('home.html', request.remote_addr)


if __name__ == '__main__':
    app.run()

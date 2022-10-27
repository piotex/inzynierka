import os
import sys

import cv2
import numpy as np
from flask import Flask, request, render_template
from models.Patient import Patient
from src.PatientList import PatientList
from src.UserList import UserList

import tensorflow as tf

LOGGED_IN = False
IMG_PATH_DEF = '../static/def/'
IMG_PATH_UPL = '../static/uploads/'
PATIENT_LIST = []
app = Flask(__name__)


@app.route('/patient_list', methods=['GET', 'POST'])
def patient_list():
    global IMG_PATH_DEF, PATIENT_LIST
    return render_template('patient_list.html', patient_list=PATIENT_LIST)


@app.route('/patient_edit', methods=['GET', 'POST'])
def patient_edit():
    global PATIENT_LIST, IMG_PATH_UPL
    tmp_id = int(request.form.get("id"))
    tmp_name = request.form.get("name")
    tmp_surname = request.form.get("surname")
    tmp_image = request.form.get("image")

    if tmp_name is None or tmp_surname is None:
        for elem in PATIENT_LIST:
            if elem.id == tmp_id:
                return render_template('patient_edit.html', patient=elem)

    try:
        tmp_file = request.files["image"]
        tmp_path = os.path.abspath(os.getcwd()) + "\\static\\uploads\\" + tmp_file.filename
        tmp_file.save(tmp_path)
        tmp_image = IMG_PATH_UPL + tmp_file.filename
    except Exception as e:
        print(e, file=sys.stderr)

    for i in range(len(PATIENT_LIST)):
        if PATIENT_LIST[i].id == tmp_id:
            PATIENT_LIST[i] = Patient(id=tmp_id, name=tmp_name, surname=tmp_surname, image=tmp_image, exam_history=[])
    return render_template('patient_list.html', patient_list=PATIENT_LIST)


@app.route('/patient_add', methods=['GET', 'POST'])
def patient_add():
    global IMG_PATH_UPL, PATIENT_LIST
    tmp_surname = request.form.get("surname")
    tmp_name = request.form.get("name")
    tmp_image = ""
    tmp_id = 0

    for i in range(len(PATIENT_LIST)):
        if PATIENT_LIST[i].id >= tmp_id:
            tmp_id = PATIENT_LIST[i].id + 1

    try:
        tmp_file = request.files["image"]
        tmp_file.save(os.path.abspath(os.getcwd()) + "\\static\\uploads\\" + tmp_file.filename)
        tmp_image = IMG_PATH_UPL + tmp_file.filename
    except Exception as e:
        print(e, file=sys.stderr)

    patient1 = Patient(id=tmp_id, name=tmp_name, surname=tmp_surname, image=tmp_image, exam_history=[])
    PATIENT_LIST.insert(0, patient1)

    return render_template('patient_list.html', patient_list=PATIENT_LIST)


@app.route('/patient_delete', methods=['GET', 'POST'])
def patient_delete():
    global IMG_PATH_UPL, PATIENT_LIST
    tmp_id = int(request.form.get("id"))
    for elem in PATIENT_LIST:
        if elem.id == tmp_id:
            PATIENT_LIST.remove(elem)

    return render_template('patient_list.html', patient_list=PATIENT_LIST)


@app.route('/patient_history', methods=['GET', 'POST'])
def patient_history():
    global PATIENT_LIST, IMG_PATH_UPL
    tmp_id = int(request.form.get("id"))

    for patient in PATIENT_LIST:
        if patient.id == tmp_id:
            return render_template('patient_history.html', patient=patient)

    return render_template('patient_list.html', patient_list=PATIENT_LIST)


@app.route('/patient_examine', methods=['GET', 'POST'])
def patient_examine():
    global PATIENT_LIST, IMG_PATH_UPL
    tmp_id = int(request.form.get("id"))
    patient_idx = None
    tmp_response = ""

    for i in range(len(PATIENT_LIST)):
        if PATIENT_LIST[i].id == tmp_id:
            patient_idx = i

    try:
        tmp_file = request.files["brain_image"]
        file_to_examine = "C:\\_programs\\inz_brain_imgs\\" + tmp_file.filename
        tmp_file.save(file_to_examine)

        img_size = 80
        img_1 = cv2.imread(file_to_examine)
        img_2 = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
        img_array = cv2.resize(img_2, (img_size, img_size))
        xxxx = []
        xxxx.append(img_array)
        img_to_examine = np.array(xxxx)

        file_name = os.getcwd() + '\\tf_models\\altzheimer_inz_model.h5'
        model_loaded = tf.keras.models.load_model(file_name)
        prediction = model_loaded.predict(img_to_examine)
        print(prediction, sys.stderr)
        predicted_label = np.argmax(prediction[i])
        tmpppp_labels = ["MildDemented", "ModerateDemented", "NonDemented", "VeryMildDemented"]

        tmp_response = tmpppp_labels[predicted_label]
        print(tmp_response, sys.stderr)
        PATIENT_LIST[patient_idx].exam_history.insert(0, tmp_response)
    except Exception as e:
        print(e, file=sys.stderr)

    return render_template('patient_examine.html', patient=PATIENT_LIST[patient_idx], response=tmp_response)


@app.route('/login', methods=['GET', 'POST'])
def login():
    global LOGGED_IN
    if LOGGED_IN:
        return render_template('home.html')

    tmp_login = request.form.get("login")
    tmp_pwd = request.form.get("pwd")

    user_list = UserList.read_user_list()
    for user in user_list:
        if user.login == tmp_login and user.password == tmp_pwd:
            LOGGED_IN = True
            return render_template('home.html')

    if tmp_login is None:
        tmp_login = ""
    if tmp_pwd is None:
        tmp_pwd = ""

    return render_template('login.html', login=tmp_login, pwd=tmp_pwd)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    global LOGGED_IN
    LOGGED_IN = False
    return render_template('login.html')


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index():
    global LOGGED_IN
    if LOGGED_IN:
        return render_template('home.html')
    return render_template('login.html')


if __name__ == '__main__':
    # todo: how to read patientlist to global list / other options?
    # global PATIENT_LIST
    # PATIENT_LIST = PatientList.read_patient_list()

    app.run()

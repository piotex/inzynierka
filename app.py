import os
import sys

from flask import Flask, request, render_template, send_file, send_from_directory

from models.User import User

LOGGED_IN = False
IMG_PATH_DEF = '../static/def/'
IMG_PATH_UPL = '../static/uploads/'
USER_LIST = [
    User(id=123, name="Peter", surname="Kubon", image=IMG_PATH_DEF + "def_pers_icon.png", role="patient"),
    User(id=124, name="Adam", surname="Smith", image=IMG_PATH_DEF + "def_pers_icon.png", role="patient"),
    User(id=125, name="Jan", surname="Bond", image=IMG_PATH_DEF + "def_pers_icon.png", role="doctor")
]

app = Flask(__name__)


@app.route('/get_users', methods=['GET', 'POST'])
def get_users():
    global IMG_PATH_DEF, USER_LIST
    return render_template('patient_list.html', user_list=USER_LIST)


@app.route('/edit_user', methods=['GET', 'POST'])
def edit_user():
    global USER_LIST, IMG_PATH_UPL
    tmp_id = int(request.form.get("id"))
    tmp_name = request.form.get("name")
    tmp_surname = request.form.get("surname")
    tmp_image = request.form.get("image")

    if tmp_name is None or tmp_surname is None:
        for elem in USER_LIST:
            if elem.id == tmp_id:
                return render_template('edit_patient.html', user=elem)

    try:
        tmp_file = request.files["image"]
        tmp_path = os.path.abspath(os.getcwd()) + "\\static\\uploads\\" + tmp_file.filename
        tmp_file.save(tmp_path)
        tmp_image = IMG_PATH_UPL + tmp_file.filename
    except Exception as e:
        print(e, file=sys.stderr)

    for i in range(len(USER_LIST)):
        if USER_LIST[i].id == tmp_id:
            USER_LIST[i] = User(id=tmp_id, name=tmp_name, surname=tmp_surname, image=tmp_image, role="patient")
    return render_template('patient_list.html', user_list=USER_LIST)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    global IMG_PATH_UPL, USER_LIST
    tmp_surname = request.form.get("surname")
    tmp_name = request.form.get("name")
    tmp_image = ""
    tmp_id = 0

    for i in range(len(USER_LIST)):
        if USER_LIST[i].id >= tmp_id:
            tmp_id = USER_LIST[i].id+1

    try:
        tmp_file = request.files["image"]
        tmp_file.save(os.path.abspath(os.getcwd()) + "\\static\\uploads\\" + tmp_file.filename)
        tmp_image = IMG_PATH_UPL + tmp_file.filename
    except Exception as e:
        print(e, file=sys.stderr)

    user1 = User(id=tmp_id, name=tmp_name, surname=tmp_surname, image=tmp_image, role="patient")
    USER_LIST.insert(0, user1)

    return render_template('patient_list.html', user_list=USER_LIST)


@app.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    global IMG_PATH_UPL, USER_LIST
    tmp_id = int(request.form.get("id"))
    for elem in USER_LIST:
        if elem.id == tmp_id:
            USER_LIST.remove(elem)

    return render_template('patient_list.html', user_list=USER_LIST)


@app.route('/history_user', methods=['GET', 'POST'])
def history_user():
    global IMG_PATH_UPL, USER_LIST
    surname = request.form.get("id")
    raise Exception("not implemented - examine_user")
    return render_template('patient_list.html', user_list=USER_LIST)


@app.route('/examine_user', methods=['GET', 'POST'])
def examine_user():
    global USER_LIST, IMG_PATH_UPL
    tmp_id = int(request.form.get("id"))

    try:
        tmp_file = request.files["brain_image"]
        tmp_path = os.path.abspath(os.getcwd()) + "\\static\\uploads\\brain_img\\" + tmp_file.filename
        tmp_file.save(tmp_path)

    except Exception as e:
        print(e, file=sys.stderr)

    return render_template('examine_user.html', user_list=USER_LIST)


@app.route('/login', methods=['GET', 'POST'])
def login():
    global LOGGED_IN
    if LOGGED_IN:
        return render_template('home.html')

    tmp_login = request.form.get("login")
    tmp_pwd = request.form.get("pwd")
    if tmp_login == "admin" and tmp_pwd == "admin":
        LOGGED_IN = True
        return render_template('home.html')

    if tmp_login is None:
        tmp_login = ""
    if tmp_pwd is None:
        tmp_pwd = ""

    return render_template('login.html', login=tmp_login, pwd=tmp_pwd)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index():
    global LOGGED_IN
    if LOGGED_IN:
        return render_template('home.html')
    return render_template('login.html')


if __name__ == '__main__':
    app.run()

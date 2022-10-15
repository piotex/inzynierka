import os
from flask import Flask, request, render_template, send_file, send_from_directory

from models.User import User

UPLOAD_FOLDER = './upload'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

LOGGED_IN = False




@app.route('/test_dev', methods=['GET', 'POST'])
def test_dev():
    user1 = User(id=9997, name="Peter", surname="Kubon", image="../static/img.jpg", role="patient")
    user2 = User(id=9997, name="Adam", surname="Smith", image="../static/img.jpg", role="patient")
    user3 = User(id=9997, name="Jan", surname="Bond", image="../static/img.jpg", role="doctor")

    user_list = [user1, user2, user3]
    return render_template('patient_list.html', user_list=user_list)


@app.route('/test_dev_1', methods=['GET', 'POST'])
def test_dev_1():
    surname = request.form.get("surname")
    name = request.form.get("name")
    file = request.files["image"]
    if file.filename != '':
        file.save("C:\\Users\\pkubon\\OneDrive - Capgemini\\Desktop\\inżynierka_web\\static\\" + file.filename)

    user1 = User(id=9997, name=name, surname=surname, image="../static/"+file.filename, role="patient")
    user_list = [user1]
    return render_template('patient_list.html', user_list=user_list)
    

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home.html')


@app.route('/home', methods=['GET', 'POST'])
def login():
    return render_template('home.html')


@app.route('/login_validation', methods=['GET', 'POST'])
def login_validation():
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

    return render_template('index.html', login=tmp_login, pwd=tmp_pwd)


@app.route('/get_image')
def get_image():
    # return send_file("static/img.jpg", mimetype='image/jpg')
    return "<img src=\"static/img.jpg\" alt=\"Girl in a jacket\" width=\"500\" height=\"600\">"


@app.route('/idk', methods=['GET', 'POST'])
def upload_file():
    bb = "\\"
    if request.method == 'POST':
        if 'file1' not in request.files:
            return 'there is no file1 in form!'
        file1 = request.files['file1']
        path = os.path.join(UPLOAD_FOLDER, file1.filename)
        file1.save(path)
        return render_template("index.html", user_image=path)

    return '''
    <h1>Upload new File</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file1">
      <input type="submit">
    </form>
    '''


if __name__ == '__main__':
    app.run()

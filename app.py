import os
from flask import Flask, request, render_template, send_file

UPLOAD_FOLDER = './upload'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/get_image')
def get_image():
    # return send_file("static/img.jpg", mimetype='image/jpg')
    return "<img src=\"static/img.jpg\" alt=\"Girl in a jacket\" width=\"500\" height=\"600\">"


@app.route('/', methods=['GET', 'POST'])
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

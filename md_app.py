from flask import Flask, request, render_template
import waitress
import logging
import utility.log_decorator as log
from utility.json_operator import Operator
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'D://'

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        files = request.files.getlist('file')
        for file in files:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'Upload Successful!'
    return render_template('upload.html')

@log.log_exception
def main():
    json_oper = Operator("config", "config.json")
    conf = json_oper.load_as_dict()
    if conf["mode"] == "debug":
        logging.basicConfig(level=logging.INFO)
    logging.info('Starting Waitress server')
    waitress.serve(app, host=conf["hostname"], port=conf["port"])
    logging.info('Waitress server stopped')

if __name__ == '__main__':
    main()

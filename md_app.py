from flask import Flask, request, render_template, jsonify
import waitress
import logging
import utility.log_decorator as log
from utility.json_operator import Operator
from werkzeug.utils import secure_filename
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
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
@app.route('/video_list/<int:id>', methods=["GET"])
def video(id):
    return get_video_list(id)

@app.route('/video_list', methods=['GET'])
def video_all():
    return get_video_list()

def get_video_list(id=0):
    # Get the directory path from the query parameter 'directory'
    directory_path = request.args.get('dir')

    if directory_path:
        # Check if the specified directory exists
        if os.path.exists(directory_path) and os.path.isdir(directory_path):
            # Get a list of all files in the directory
            file_list = os.listdir(directory_path)
            print(file_list)
            # Return the file list as JSON
            if (id == 0):
                return jsonify(file_list)
            else:
                return jsonify(file_list[id])
        else:
            return jsonify({"error": "Directory not found."}), 404
    else:
        return jsonify({"error": "Missing 'directory' query parameter."}), 400

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

from flask import Flask
import waitress
import logging
import utility.log_decorator as log
from utility.json_operator import Operator

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

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

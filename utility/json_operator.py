import json
import os
from .log_decorator import log_exception

class Operator:
    def __init__(self, pathname: str, filename: str):
        self.__pathname = pathname
        self.__filename = filename
        path = os.path.join(pathname, filename)
        if os.path.isabs(path):
            self.__fullname = path
        else:
            cwd = os.getcwd()
            self.__fullname = os.path.join(cwd, path)

    @log_exception
    def load_as_dict(self):
        with open(self.__fullname) as f:
            self.data = json.load(f)
        return self.data

    def write(self, data):
        try:
            if type(data) is dict:
                with open(self.__fullname) as f:
                    json.dump(data, f, indent=4, sort_keys=True)
            else:
                json_data = json.dumps(data, indent=4, sort_keys=True)
                with open('data.json', 'w') as f:
                    f.write(json_data)
            return True
        except Exception as e:
            # log_exception_message(e)
            return False
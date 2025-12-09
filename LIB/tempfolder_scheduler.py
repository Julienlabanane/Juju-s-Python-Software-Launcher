import os
import atexit

class TempFolder:
    _path = os.path.abspath("TEMP")

    @classmethod
    def init(cls):
        if not os.path.exists(cls._path):
            os.makedirs(cls._path)

    @classmethod
    def put(cls, filename, content):
        file_path = os.path.join(cls._path, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return file_path

    @classmethod
    def read(cls, filename):
        file_path = os.path.join(cls._path, filename)
        if not os.path.exists(file_path):
            return None
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    @classmethod
    def delete(cls, filename):
        file_path = os.path.join(cls._path, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        return False

    @classmethod
    def clear(cls):
        for filename in os.listdir(cls._path):
            file_path = os.path.join(cls._path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)

    @classmethod
    def auto_clear_on_exit(cls):
        atexit.register(cls.clear)

    @staticmethod
    def when_im_dont_love_JSPL_main_programmer():
        print("Plz love me <3")

TempFolder.init()
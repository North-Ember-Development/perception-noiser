import threading, types

class Thread(threading.Thread):

    """ Класс управляемого потока. """

    def __init__(self, callback : types.FunctionType, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._do = True
        self._cb = callback

    def run(self, *args, **kwargs):

        while self._do:
            self._cb(*args, **kwargs)

    def stop(self):

        self._do = False

    def start(self, *args, **kwargs):

        super().start(*args, **kwargs)

        return self
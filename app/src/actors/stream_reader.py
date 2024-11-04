# external imports
from threading import Thread, Event

# internal imports


class StreamReader(Thread):
    def __init__(self):
        super().__init__()

        self._stop_event = Event()

    def run(self):
        self.open_socket_connection()
        # treat connection

    def stop(self):
        self._stop_event.set()

    def open_socket_connection(self):
        print("Intentando conectar")
        # Make connection

        print("Conexión realizada con el servidor")

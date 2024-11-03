# external imports
from threading import Thread

# internal imports


class StreamReader(Thread):
    def __init__(self, url: str, port: int):
        super().__init__()
        self.url = url
        self.port = port

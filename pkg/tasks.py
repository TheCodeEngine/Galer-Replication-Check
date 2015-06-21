import subprocess

class Command:
    def __init__(self, host, command):
        self.host = host
        self.command = command

    def _run(self):
        pass
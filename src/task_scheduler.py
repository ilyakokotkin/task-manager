import subprocess

class TaskScheduler:
    def __init__(self, path_to_task):
        self.path_to_task = path_to_task

    def start_task(self):
        subprocess.Popen(self.path_to_task)

    def end_task(self):
        subprocess.call(['taskkill', '/F', '/IM', 'WhatsApp.exe'])
import subprocess
import os
import schedule
from dotenv import load_dotenv


class TaskScheduler:
    def __init__(self):
        load_dotenv() 
        self.path_to_task = os.getenv('PATH_TO_TASK')
        self.task_to_kill = os.getenv('TASK_TO_KILL')
        self.remaining_jobs = 3

    def start_task(self):
        subprocess.Popen(self.path_to_task)
        self.remaining_jobs -= 1

    def end_task(self):
        subprocess.call(['taskkill', '/F', '/IM', self.task_to_kill])
      
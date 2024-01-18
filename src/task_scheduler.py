import subprocess
import os
import schedule
from dotenv import load_dotenv


class TaskScheduler:
    def __init__(self):
        load_dotenv() 
        self.path_to_task = os.getenv('PATH_TO_TASK')
        self.task_to_kill = os.getenv('TASK_TO_KILL')
        self.end_job = None

    def start_task(self):
        subprocess.Popen(self.path_to_task)

    def end_task(self):
        subprocess.call(['taskkill', '/F', '/IM', self.task_to_kill])
        # Cancel the scheduled job if it's set
        if self.end_job:
            schedule.cancel_job(self.end_job)
            self.end_job = None  

    def schedule_end_task(self, time_str):
        # Schedule the end task and store the job
        self.end_job = schedule.every().day.at(time_str).do(self.end_task).tag('end_task')
import subprocess
import schedule

class TaskScheduler:
    def __init__(self, path_to_task):
        self.path_to_task = path_to_task
        self.end_job = None  

    def start_task(self):
        subprocess.Popen(self.path_to_task)

    def end_task(self):
        subprocess.call(['taskkill', '/F', '/IM', 'WhatsApp.exe'])
        # Cancel the scheduled job if it's set
        if self.end_job:
            schedule.cancel_job(self.end_job)
            # Reset the end_job to None
            self.end_job = None  

    def schedule_end_task(self, time_str):
        # Schedule the end task and store the job
        self.end_job = schedule.every().day.at(time_str).do(self.end_task).tag('end_task')
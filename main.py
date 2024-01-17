import schedule
import time
from .src.task_scheduler import TaskScheduler

def main():
    path_to_task = 'C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2401.3.0_x64__cv1g1gvanyjgm\\WhatsApp.exe'
    task_scheduler = TaskScheduler(path_to_task)

    schedule.every().day.at('09:30').do(task_scheduler.start_task)
    schedule.every().day.at('09:40').do(task_scheduler.end_task)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

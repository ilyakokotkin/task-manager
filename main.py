import schedule
import time
from src.task_scheduler import TaskScheduler

def main():
    # Define the path to the task 
    path_to_task = 'C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2401.3.0_x64__cv1g1gvanyjgm\\WhatsApp.exe'
    
    try:
        task_scheduler = TaskScheduler(path_to_task)
        print(f"TaskScheduler initialized with the path: {path_to_task}")
    except Exception as e:
        print(f"Failed to initialize TaskScheduler: {e}")
        return
    
    try:
        # Schedule the task to start and end at specified times
        schedule.every().day.at('09:41').do(task_scheduler.start_task)
        schedule.every().day.at('09:42').do(task_scheduler.end_task)
        print("Tasks have been scheduled successfully.")
    except Exception as e:
        print(f"Failed to schedule tasks: {e}")
        return
    
    print("Task Scheduler is running. Press Ctrl+C to exit.")
    try:
        # Run scheduled tasks
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Task Scheduler has been terminated.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

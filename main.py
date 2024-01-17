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
        schedule.every().day.at('10:13').do(task_scheduler.start_task)

        schedule.every().day.at('10:14').do(task_scheduler.end_task)
        
        print("Tasks have been scheduled successfully.")

    except Exception as e:
        print(f"Failed to schedule tasks: {e}")
        return
    
    print("Task Scheduler is running. Waiting for tasks to complete.")
    try:
        # Run scheduled tasks
        while True:
            schedule.run_pending()
            time.sleep(1)

            # Check if there is no more jobs scheduled
            if not schedule.jobs:
                break

    except Exception as e:
        print(f"An error occurred: {e}")
    
    print("Task Scheduler has completed its tasks and will now terminate.")

if __name__ == "__main__":
    main()

import pytest
from unittest.mock import patch, MagicMock
from src.task_scheduler import *
import main

# Test initialization of TaskScheduler
@patch('main.TaskScheduler')
def test_main_initialization(mock_task_scheduler):
    with patch('builtins.print') as mock_print:
        main.main()
        mock_task_scheduler.assert_called_with('C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2401.3.0_x64__cv1g1gvanyjgm\\WhatsApp.exe')
        mock_print.assert_called_with("TaskScheduler initialized with the path: C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2401.3.0_x64__cv1g1gvanyjgm\\WhatsApp.exe")

# Test scheduling tasks
@patch('main.TaskScheduler')
def test_main_scheduling(mock_task_scheduler):
    mock_scheduler = MagicMock()
    with patch('main.schedule', mock_scheduler):
        with patch('builtins.print') as mock_print:
            main.main()
            assert mock_scheduler.every().day.at('09:41').do.called
            assert mock_scheduler.every().day.at('09:42').do.called
            mock_print.assert_called_with("Tasks have been scheduled successfully.")

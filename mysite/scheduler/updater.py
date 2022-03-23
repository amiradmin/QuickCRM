from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from scheduler import tasks
from scheduler.models import TimesheetChecker

def start():
    scheduler = BackgroundScheduler()
    # scheduler.add_job(tasks.timesheet_check_interval, 'interval', minutes=30)
    tes_task = TimesheetChecker.objects.last()
    print(tes_task)
    scheduler.add_job(tasks.timesheet_check_interval, 'date', run_date=tes_task.date)
    # scheduler.add_job(tasks.timesheet_check_interval, 'interval', seconds=5)
    scheduler.start()
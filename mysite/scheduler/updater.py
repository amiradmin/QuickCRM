from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from scheduler import tasks

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(tasks.timesheet_check_interval, 'interval', minutes=30)
    # scheduler.add_job(tasks.timesheet_check_interval, 'interval', seconds=5)
    scheduler.start()
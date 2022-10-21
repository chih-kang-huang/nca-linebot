from apscheduler.schedulers.blocking import BlockingScheduler
import urllib.request
import datetime


sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='mon-fri', minute='*/25')
def scheduled_job():
    # test
    print('======= APScheduler CRON=======')
    print('This job runs every day */25min.')
    
    # datetime 檢查時間

    print(f'{datetime.datetime.now().ctime()}')
    print('========== APScheduler CRON =========')
    

    url = "https://eatwhat-in-ncu.herokuapp.com/"
    conn = urllib.request.urlopen(url)


    for key, value in conn.getheaders():
        print(key, value)


sched.start()

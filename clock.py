from apscheduler.schedulers.blocking import BlockingScheduler
import urllib.request
import datetime


sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='mon,tue,wed,thu,fri,sun', hour='0,1,2,3,4,5,6,7,8,9,10,16,17,18,19,20,21,22,23', minute='*/25')
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

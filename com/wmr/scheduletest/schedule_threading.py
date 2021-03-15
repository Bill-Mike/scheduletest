# -*- coding:utf-8 -*-

import schedule
import time,threading

def job(name):
    print(threading.Thread().getName()+": her name is:", name)
    return


schedule.every(10).seconds.do(job, "seconds")
schedule.every().hour.do(job, "hour")
schedule.every().day.at("11:40").do(job, "day")
schedule.every(5).to(10).days.do(job, "5days~10days")
schedule.every().monday.do(job, "monday this time run")
schedule.every().wednesday.at("13:15").do(job, "wednesday 13:15 run")

while True:
    schedule.run_pending()
    time.sleep(1)
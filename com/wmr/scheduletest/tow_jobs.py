# -*- coding:utf-8 -*-

import schedule, threading, time

def job1(name):
    print("job1 is running" + name)
    return

def job2(name):
    print("job2 is running" + name)
    return

schedule.every(10).seconds.do(job1, "seconds")

i = 0
while True:
    schedule.run_pending()
    if i == 10:
        schedule.every(5).seconds.do(job2,"seconds")
    i += 1
    if i == 100:
        schedule.jobs.remove(schedule.jobs.__getitem__(1))
    time.sleep(3)


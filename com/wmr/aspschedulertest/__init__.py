# -*- coding:utf-8 -*-
'''
APScheduler 调度框架测试
四大组件：
    触发器(trigger)：
        包含调度逻辑，每一个作业有他自己的触发器，用于决定接下来哪一个作业运行。除了他们自己初始配置以外，触发器完全是无状态的。
    作业存储（job store）：
        存储被调度的作业，默认的作业存储是简单地把作业保存在内存中，其他的作业存储是将作业保存到数据库中。和一个作业的数据将在保存在持久化作业存储时被序列化，并加载时被反序列化。调度器不能共享同一个作业存储
    执行器（executor）：
        处理作业的运行，他们通常在作业中提交指定的可调度对象到一个线程或进程池来进行。当作业完成时，执行器将会通知调度器
    调度器（scheduler）：
        是其他的组成部分。你通常在引用只有一个调度器，应用的开发者通常不会直接处理作业存储、调度器和触发器。相反调度器提供了处理这些的合适接口。配置作业存储和执行器可以在调度器中完成，例如调价、修改和移除作业、
        你需要选择合适的调度器，这取决于你的应该用环境和你使用aspscheduler的目的。通常最常用的两个：
            BlockingScheduler:当调度器事你应用中唯一要运行的东西时使用。
            backgroundScheduler:当不运行其他框架时使用，并希望调度器在你应用的后台执行。

配置调度器
    ASPScheduler提供了许多的方式来配置调度器，你可以使用一个配置字典作为参数关键字的方式传入。你可以先创建调度器再配置和添加作业，这样你可以在不同的环境中得到更大的灵活性。
    下面是一个简单实用BlockingScheduler,并使用默认内存和默认执行器。（MemoryJobStore,ThreadPoolExecutor）,其中线程池的最大线程数为10，配置完成后使用start（）方法来启动
'''

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import threading, time

def my_job():
    print(threading.current_thread().getName() + "hello world")
    time.sleep(4)

sched = BackgroundScheduler()
sched.add_job(my_job, 'interval', seconds=5)
sched.start()
while True:
    time.sleep(100000)


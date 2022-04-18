import sentEmail
from apscheduler.schedulers.blocking import BlockingScheduler


def sent():
    #sentEmail.sentforecast("北京")
    #sentEmail.sentforecast("沈阳")
    sentEmail.sentforecast("测试")
if __name__ == "__main__":
    # scheduler = BlockingScheduler()
    # scheduler.add_job(sent,"interval",days=1)
    # scheduler.start()
    sent()

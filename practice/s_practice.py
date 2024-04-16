import schedule
import time

def message():
    print("스케쥴 실행중...")

schedule.every(1).seconds.do(message)

while True:
    schedule.run_pending()
    time.sleep(1)

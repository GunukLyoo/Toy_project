import schedule
import time

def message():
    print("스케쥴 실행중...")

def message2(text):
    print(text)

#schedule.every(1).seconds.do(message)

schedule.every(2).seconds.do(message2, '2초마다 알려줄게요')

while True:
    schedule.run_pending()
    #time.sleep(1)

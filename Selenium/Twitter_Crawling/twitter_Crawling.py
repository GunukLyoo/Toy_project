from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#트위터 사용자 페이지의 첫번째 트윗을 크롤링하여 자동으로 번역하는 프로그램이다.

#url = 'https://twitter.com/suisei_hosimati'
url = 'https://twitter.com/kobokanaeru'
options = webdriver.ChromeOptions()
options.add_argument("headless")

driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(4)

name = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[1]//div[@data-testid="tweetText"]')
print(name.text)
print(type(name.text))

te = name.text

#te = name.find_element(by='data-testid', 'tweetText')
#print(te)

url2 = 'https://papago.naver.com/?sk=auto&tk=ko'
driver.get(url2)
time.sleep(3)

textbox = driver.find_element(By.ID, 'txtSource')
textbox.send_keys(te)

time.sleep(3)

resultbox = driver.find_element(By.ID, 'txtTarget')
print(resultbox.text)

driver.quit()

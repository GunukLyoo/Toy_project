from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

print('네이버 페이 증권 기준 현재가를 보기 원하는 주식의 코드를 입력하시오')
code = input()
url = 'https://finance.naver.com/item/sise.naver?code=' + code

driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

name = driver.find_element(By.XPATH, '//*[@id="middle"]/div[1]/div[1]/h2/a')
print(name.text)

search = driver.find_element(By.ID, '_nowVal')

now = search.text
    
print('현재가: ' + now)

search = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/span')

yesterday = search.text

print('전일가: ' + yesterday)

diff = int(yesterday) - int(now)
print('전일대비: ' + str(diff))

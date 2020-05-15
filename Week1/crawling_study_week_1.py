#crawling_study_week_1

###################################################################
###interpark_tour
###인터파크 투어 사이트에서 여행지를 입력 후 검색 -> 결과
###로그인 시 PC Web site에서 처리가 어려운 경우 -> 모바일로 로그인 진입
###################################################################

#0_set up
#installing selenium
#pip install selenium
driver_path = 'C:/Users/JAEHUN_KANG/Desktop/crawling_study/ch2/chrome_driver/' #chrome_driver.exe가 있는 경로
chrome_driver_name = 'chromedriver.exe'
main_url = 'http://tour.interpark.com/'
key_word = '파리'

#1_importing modules
from selenium import webdriver as wd
import os

#2_loading_driver
os.chdir(driver_path)
os.getcwd()
driver = wd.Chrome(executable_path=chrome_driver_name)

#사전에 필요한 정보를 load
#Database or Shell or Batch 파일에서 인자로 받아서 setting
#crawling 오래하면 temp 파일이 많이 쌓임 -> 주기적으로 비워줘야 함

#3_web site 접속
driver.get(main_url)

#4_검색창을 찾아서 검색어를 입력
driver.find_element_by_id('SearchGNBText').send_keys(key_word)

#5_검색 버튼 클릭
#3강부터..

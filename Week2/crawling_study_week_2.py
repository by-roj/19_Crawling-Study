#crawling_study_week_1

###################################################################
###interpark_tour
###인터파크 투어 사이트에서 여행지를 입력 후 검색 -> 결과
###로그인 시 PC Web site에서 처리가 어려운 경우 -> 모바일로 로그인 진입
###################################################################

#0_set up
#installing selenium
#pip install selenium
driver_path = '/Users/yoo/Downloads/' #chrome_driver.exe가 있는 경로
chrome_driver_name = './chromedriver'
main_url = 'http://tour.interpark.com/'
key_word = '파리'

#1_importing modules
from selenium import webdriver as wd
import os

#2_loading_driver
os.getcwd()
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
#수정 하고 싶을 때! 뒤에 내용 붙는거 방지하기 위해 --> .clear() --> send_keys('content')

#5_검색 버튼 클릭
driver.find_element_by_css_selector('button.search-btn').click()

#잠시 대기! --> 페이가 로드되고 나서 데이터를 즉각적으로 획득하는 행위는
#명시적 대기 --> 특정 요소가 로케이트 때 까지 대기
from selenium.webdriver.common.by import By
#명시적 대기를 위해
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

#사전에 필요한 정보를 로드 --> 디비혹스 웹, 배치 파일에서 인자로 받아서 셋팅
main_url = "http://tour.interpark.com/"
keyword = '파리'

try:
    element = WebDriverWait(driver, 10).until(
        #지정한 한 개 요소가 올라오면 웨이트 종료
        EC.presence_of_element_located(By.CLASS_NAME, 'oTravelBox')
    )
except Exception as e:
    print('오류 발생', e)

#암묵적 대기 --> DOM이 다 로드 될 때까지 대기 하고 먼저 로드되면 바로 진행

#요소를 찾을 특정 시간 동안 DOM 폴링을 지시 (발견되면 진행)
driver.implicitly_wait(10)
#절대기 대기 --> time.sleep(10) --> 클라우드 페어 (디도스 방어 솔루션)

#더보기 눌러서 게시판 진입하기
driver.find_element_by_css_selector('.oTravelBox>.boxList>.moreBtnWrap>.moreBtn').click()

#게시판에서 데이터 가져올 때
#데이터가 많으면 --> 세션 (로그인을 해서 접되는 사이트면) 관리
#특정 단위별로 로그아웃 로그인 계속 시도
#특정 게시물이 사라질경우 --> 팝업 발생 (없는..게시물..) --> 팝업 처리 검토
#게시판 스캔시 --> 임계점을 모르는게 문제! (어디가 끝이냐?)
#게시판 스캔 --> 메타 정보 획득 --> loop를 돌려서 일괄적으로 방문 접근 처리

#searchModule.SetCategoryList(1, '') 스크립트 실행
#16은 임시값 (게시물이 넘어갔을 때 현상 확인을 위해 숫자를 오버해서 넣음)
for page in range(1, 16)
    try:
        #자바 스크립트 구동하기
        driver.execute_script("searchModule.SetCategoryList(%s, '')" % page)
        time.sleep(2)
        print("%s 페이지 이동" % page)
    except Exception as e1:
        print ( '오류', e1 )

#자제 -->

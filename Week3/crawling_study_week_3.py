#crawling_study_week_1

###################################################################
###interpark_tour
###인터파크 투어 사이트에서 여행지를 입력 후 검색 -> 결과
###로그인 시 PC Web site에서 처리가 어려운 경우 -> 모바일로 로그인 진입
###################################################################

#0_set up
#installing selenium
#pip install selenium
driver_path = 'C:/YBIGTA/Crawling/190330/' #chrome_driver.exe가 있는 경로
chrome_driver_name = 'chromedriver.exe'
main_url = 'http://tour.interpark.com/'
key_word = '로마'

#1_importing modules
from selenium import webdriver as wd
import os

#2_loading_driver
os.getcwd()
os.chdir(driver_path)
os.getcwd()
driver = wd.Chrome(executable_path=chrome_driver_name)

#3_web site 접속
driver.get(main_url)

#4_검색창을 찾아서 검색어를 입력
driver.find_element_by_id('SearchGNBText').send_keys(key_word)

#5_검색 버튼 클릭
driver.find_element_by_css_selector('button.search-btn').click()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from Tour import TourInfo

main_url = 'http://tour.interpark.com/'
keyword = '로마'
# 상품 정보를 담는 리스트(Tourinfo 리스트 - Tourinfo 객체들을 모아서 담는 리스트)
tour_list = []

try:
    element = WebDriverWait(driver, 10).until(
        #지정한 한 개 요소가 올라오면 웨이트 종료
        EC.presence_of_element_located((By.CLASS_NAME, 'oTravelBox'))
    )
except Exception as e:
    print('오류 발생', e)

driver.implicitly_wait(10)

#더보기 눌러서 게시판 진입하기
driver.find_element_by_css_selector('.oTravelBox>.boxList>.moreBtnWrap>.moreBtn').click()

#searchModule.SetCategoryList(1, '') 스크립트 실행
#16은 임시값 (게시물이 넘어갔을 때 현상 확인을 위해 숫자를 오버해서 넣음)

for page in range(1, 2):#16):   # 너무 많으므로 일단 한 바퀴만 돌려봄
    try:
        #자바 스크립트 구동하기
        driver.execute_script("searchModule.SetCategoryList(%s,'')" % page)
        time.sleep(2)
        print("%s 페이지 이동" % page)

        #-----------------------5강------------------------#
        # 여러 사이트에서 정보를 수집할 경우 공통 정보 정의 단계 필요
        # 상품명, 코멘트, 기간1, 기간2, 가격, 평점, 썸네일, 링크(상품상세정보)
        boxItems = driver.find_elements_by_css_selector('.oTravelBox>.boxList>li')
        for li in boxItems:
               # 이미지를 링크값을 사용할것인가? or 직접 다운로드해서 우리 서버에 업로드(ftp)할 것인가? 에 대해서도 고민할 수 있음
               # 이미지가 썸네일과 뒤에 아이콘에서 한번 더 나옴. 하지만 첫번째로 나오는 것만 사용할 것이기 때문에 element로 해도 됨
               print('썸네일', li.find_element_by_css_selector('img').get_attribute('src'))    # get_attribute() : 요소의 속성값 획득
               print('링크', li.find_element_by_css_selector('a').get_attribute('onclick'))  # 얘도 마찬가지로 첫번째 a태그만 사용
	           # 간단하게 상품명만 뽑아보기(이게 되면 나머지도 다 되는거!)
               print('상품명', li.find_element_by_css_selector('h5.proTit').text)
               # 나머지도 해보기
               print('코멘트', li.find_element_by_css_selector('.proSub').text)    # proSub가 안겹치니까 이렇게 해도됨
               print('가격', li.find_element_by_css_selector('.proPrice').text)

               # 한 칸 띄면 자손 개념
               for info in li.find_elements_by_css_selector('.info-row .proInfo'):
                        print(info.text)
               print('='*100)
               # 단계가 끝날때마다 데이터 모음
               obj = TourInfo(
                    li.find_element_by_css_selector('h5.proTit').text,
                    li.find_element_by_css_selector('.proPrice').text,
                    li.find_elements_by_css_selector('.info-row .proInfo')[1].text,
                    li.find_element_by_css_selector('a').get_attribute('onclick'),
                    li.find_element_by_css_selector('img').get_attribute('src')
               )
               tour_list.append(obj)
    except Exception as e1:
        print ( '오류', e1 )

print(tour_list, len(tour_list))

# 다 성공적으로 실행되면, range를 다시 16까지로 잡고 해보기
# 다음 강의 : 수집한 정보 개수를 루프 => 페이지 방문 => 콘텐츠 획득(상품상세정보) => DB

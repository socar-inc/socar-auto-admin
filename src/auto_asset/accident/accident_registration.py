from selenium import webdriver
from pages.login_page import LoginPage
from pages.accident_page import AccidentPage

# 사용자 입력값
id = input("이메일을 입력하세요: ")
pw = input("비밀번호를 입력하세요: ")
secret = input("시크릿키를 입력하세요: ")
reservation_id = input("예약번호를 입력하세요: ")

# WebDriver 실행
driver = webdriver.Chrome()
driver.get("https://accident.socar.me/")
print("[LOG] Chrome WebDriver 실행 완료.")

# 로그인 수행
login_page = LoginPage(driver)
login_page.login(id, pw, secret)
print(f"[LOG] Keycloak 로그인 성공!")

# 사고 등록 페이지 조작
accident_page = AccidentPage(driver)
accident_page.open_accident_registration()
accident_page.search_reservation(reservation_id)
print(f"[LOG] 예약 조회 완료!")

# 신고자 정보 입력
accident_page.fill_accident_report()
accident_page.fill_accident_location()
accident_page.complete_registration()

# 사고 ID 확인 후 종료
accident_id = accident_page.get_accident_id()

# 브라우저 종료
driver.quit()
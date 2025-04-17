from selenium import webdriver

from socar_auto_admin.accident.pages.accident_page import AccidentPage
from socar_auto_admin.accident.pages.login_page import LoginPage


def run_selenium_automation(email, password, secret, reservation_id):
    # WebDriver 실행
    driver = webdriver.Chrome()
    driver.get("https://accident.socar.me/")
    print("[LOG] Chrome WebDriver 실행 완료.")

    # 로그인 수행
    login_page = LoginPage(driver)
    login_page.login(email, password, secret)
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
    driver.quit()

    return accident_id
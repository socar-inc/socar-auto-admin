import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from src.auto_asset.utils.wait_utils import wait_for_element


class ReporterTab:
    """신고자 정보 입력을 위한 클래스"""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.tab = wait_for_element(driver, By.ID, "2")

        if "is-active" not in self.tab.get_attribute("class"):
            print("[LOG] 신고자 탭이 활성화되지 않음")
            self.driver.quit()
        print("[LOG] 신고자 탭이 활성화됨")

    def select_reservation_person(self):
        """예약자 선택"""
        wait_for_element(self.driver, By.XPATH, "//div[@role='tabpanel']//span[contains(text(), '예약자')]").click()

    def select_driver_type(self):
        """사고 차량 운전자 등록 - 등록 유형 선택"""
        wait_for_element(self.driver, By.XPATH, "//div[@role='tabpanel']//h4[text()='사고차량 운전자 등록']/following-sibling::form//input[@placeholder='등록유형을 선택하세요']").click()
        wait_for_element(self.driver, By.XPATH, "//div[@class='el-select-dropdown el-popper' and not(contains(@style, 'display: none;'))]//span[text()='예약자']").click()

    def select_accident_datetime_unknown(self):
        """사고 일시 미상 선택"""
        wait_for_element(self.driver, By.XPATH, "//div[@role='tabpanel']//span[text()='사고일시 미상']").click()


class AccidentPage:
    """사고 등록 관련 페이지"""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_accident_registration(self):
        """사고 등록 메뉴로 이동"""
        wait_for_element(self.driver, By.XPATH, "//*[text()='directions_car']").click()
        wait_for_element(self.driver, By.XPATH, "//span[text()='사고등록']").click()

        # 새 탭으로 전환
        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[-1])
        print(f"[LOG] 사고 등록 페이지로 이동 완료! 현재 URL: {self.driver.current_url}")

    def search_reservation(self, reservation_id: str):
        """예약 조회"""
        wait_for_element(self.driver, By.XPATH, "//input[@placeholder='예약ID를 입력해주세요.']").send_keys(reservation_id)
        wait_for_element(self.driver, By.XPATH, "//span[contains(text(), '예약 검색')]").click()
        time.sleep(2)  # 예약 조회 결과가 나타날 때까지 대기
        wait_for_element(self.driver, By.XPATH, "//span[contains(text(), '다음')]").click()

    def fill_accident_report(self):
        """차량/예약 조회 및 신고자 정보 입력"""
        reporter_tab = ReporterTab(self.driver)
        reporter_tab.select_reservation_person()
        reporter_tab.select_driver_type()
        reporter_tab.select_accident_datetime_unknown()

    def fill_accident_location(self):
        """사고 위치 및 반납 정보 입력"""
        accident_location = wait_for_element(self.driver, By.ID, "3")
        if "is-active" not in accident_location.get_attribute("class"):
            print("[LOG] 사고 위치 탭이 활성화되지 않음")
            self.driver.quit()

        wait_for_element(accident_location, By.XPATH, "//div[@role='tabpanel']//span[contains(text(),'쏘카존')]").click()

        return_location = wait_for_element(self.driver, By.ID, "4")
        if "is-active" not in return_location.get_attribute("class"):
            print("[LOG] 반납 위치 탭이 활성화되지 않음")
            self.driver.quit()

        wait_for_element(return_location, By.XPATH, "//div[@role='tabpanel']//span[contains(text(),'쏘카존 직접 반납')]").click()
        wait_for_element(self.driver, By.XPATH, "//span[contains(text(), '다음')]").click()
        print("[LOG] 차량/예약 조회 완료!")

    def complete_registration(self):
        """사고 조사 완료"""
        wait_for_element(self.driver, By.XPATH, "//span[contains(text(), '사고등록 완료')]").click()
        print("[LOG] 사고조사 완료!")


    def get_accident_id(self):
        """등록된 사고 ID 가져오기"""
        accident_id = wait_for_element(self.driver, By.XPATH, "//div[text()='사고']//following-sibling::div").text
        print(f"[LOG] 등록된 사고 ID: {accident_id}")
        return accident_id

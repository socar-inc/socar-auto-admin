import time
import pyotp
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from utils.wait_utils import wait_for_element


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login(self, id: str, pw: str, secret: str):
        """Keycloak 로그인 수행"""
        wait_for_element(self.driver, By.ID, "username").send_keys(id)
        wait_for_element(self.driver, By.ID, "password").send_keys(pw)
        wait_for_element(self.driver, By.ID, "kc-login").click()

        # OTP 생성 및 입력
        totp = pyotp.TOTP(secret)
        otp_code = totp.now()
        print(f"[LOG] 생성된 OTP 코드: {otp_code}")
        wait_for_element(self.driver, By.ID, "otp").send_keys(otp_code)
        self.driver.find_element(By.ID, "kc-login").click()
        time.sleep(3)

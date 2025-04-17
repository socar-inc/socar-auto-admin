from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(driver: WebDriver, by, value, timeout=10):
    """요소가 로드되고 시각적으로 보이는지까지 기다리는 함수"""
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, value)))
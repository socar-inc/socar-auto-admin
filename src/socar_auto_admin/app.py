from flask import Flask, request, redirect, url_for, render_template_string
from selenium import webdriver
from accident.pages.login_page import LoginPage
from accident.pages.accident_page import AccidentPage

app = Flask(__name__)

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





@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        secret = request.form["secret"]
        reservation_id = request.form["reservation_id"]

        try:
            accident_id = run_selenium_automation(email, password, secret, reservation_id)
            print(f"자동화 완료! 사고 ID: {accident_id}")
        except Exception as e:
            print(f"자동화 중 오류 발생: {str(e)}")

        return redirect(url_for('index'))

    return '''
        <h2>사고 자동 등록</h2>
        <form method="post">
            이메일: <input type="text" name="email"><br>
            비밀번호: <input type="password" name="password"><br>
            시크릿키: <input type="text" name="secret"><br>
            예약번호: <input type="text" name="reservation_id"><br>
            <input type="submit" value="자동화 실행">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)

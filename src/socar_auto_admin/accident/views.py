from flask import request, redirect, url_for, render_template
from . import accident_blueprint
from utils.automation import run_selenium_automation

@accident_blueprint.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        id = request.form["id"]
        password = request.form["password"]
        secret = request.form["secret"]
        reservation_id = request.form["reservation_id"]

        try:
            accident_id = run_selenium_automation(id, password, secret, reservation_id)
            print(f"자동화 완료! 사고 ID: {accident_id}")
        except Exception as e:
            print(f"자동화 중 오류 발생: {str(e)}")

        return redirect(url_for("accident.registration"))

    return render_template("registration.html")

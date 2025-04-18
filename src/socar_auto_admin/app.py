from flask import Flask, request, redirect, url_for, render_template_string, render_template
from socar_auto_admin.accident import accident_blueprint
from socar_auto_admin.utils.automation import run_selenium_automation

app = Flask(__name__, template_folder="home/templates")

# 사고 등록 라우트 등록
app.register_blueprint(accident_blueprint)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)

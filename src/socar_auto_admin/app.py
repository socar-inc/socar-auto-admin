from flask import Flask, request, redirect, url_for, render_template_string
from socar_auto_admin.accident import accident_blueprint
from socar_auto_admin.utils.automation import run_selenium_automation

run_selenium_automation

app = Flask(__name__)

# 사고 등록 라우트 등록
app.register_blueprint(accident_blueprint)

@app.route("/")
def home():
    return '''
        <h1>쏘카 관리자 자동화 (QA)</h1>
        <ul>
            <li><a href="/accident/registration">사고 자동 등록</a></li>
        </ul>
    '''

if __name__ == "__main__":
    app.run(debug=True)

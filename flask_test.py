from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")

@app.route("/sign_up/submit", methods=["POST"])
def sign_up_submit():
    # 회원가입 정보를 수집합니다.
    username = request.form["username"]
    password = request.form["password"]
    email = request.form["email"]

    # 회원가입 정보를 데이터베이스에 저장합니다.
    # (데이터베이스 저장 코드는 생략합니다.)

    # 회원가입 성공 메시지를 표시합니다.
    return render_template("sign_up_success.html", username=username)


# 포스트 모더니즘 스타일의 CSS를 적용합니다.


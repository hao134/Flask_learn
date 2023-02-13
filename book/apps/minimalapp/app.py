import logging
import os

from email_validator import EmailNotValidError, validate_email
from flask import (
    Flask,
    current_app,
    flash,
    g,
    make_response,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail, Message

app = Flask(__name__)
# add secret key
app.config["SECRET_KEY"] = "2AZSMss3p5QPbcY2hBsJ"
app.logger.setLevel(logging.DEBUG)
# 避免中斷重新導向
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
# 在debugtoolbarextension 設置應用程式
toolbar = DebugToolbarExtension(app)

# 增加mail類別的組態
app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER")
app.config["MAIL_PORT"] = os.environ.get("MAIL_PORT")
app.config["MAIL_USE_TLS"] = os.environ.get("MAIL_USE_TLS")
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER")

# 登錄flask-mail擴充套件
mail = Mail(app)


@app.route("/")
def index():
    return "Hello, Flaskbook!"


@app.route("/hello/<name>", methods=["GET"], endpoint="hello-endpoint")
def hello(name):
    return f"Hello, {name}"


@app.route("/name/<Name>")
def show_name(Name):
    return render_template("index.html", Name=Name)


with app.test_request_context():
    # /
    print(url_for("index"))
    # /hello/world
    print(url_for("hello-endpoint", name="world"))
    # /name/ichiro?page=1
    print(url_for("show_name", Name="ichiro", page="1"))
    print(url_for("static", filename="style.css"))

# 獲取應用程式內文並加入堆疊
ctx = app.app_context()
ctx.push()

# 變成可存取current_app
print("current_app name:", current_app.name)


# 在全域的暫時領域設定值
g.connection = "connection"
print(g.connection)

with app.test_request_context("/users?updated=true"):
    # output true
    print(request.args.get("updated"))


@app.route("/contact")
def contact():
    # get response item
    response = make_response(render_template("contact.html"))

    # setting cookie
    response.set_cookie("flaskbook key", "flaskbook value")

    # setting session
    session["username"] = "ichiro"

    return response


@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        # use form to get form's value
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]

        # input detection:
        is_valid = True

        if not username:
            flash("必須填寫使用者名稱")
            is_valid = False
        if not email:
            flash("必須填寫郵件位址")
            is_valid = False
        try:
            validate_email(email)
        except EmailNotValidError:
            flash("請輸入正確的郵件格式")
            is_valid = False

        if not description:
            flash("必須填寫諮詢內容")
            is_valid = False

        if not is_valid:
            return redirect(url_for("contact"))
        # 傳送郵件
        send_email(
            email,
            "感謝您來信詢問。",
            "contact_mail",
            username=username,
            description=description,
        )

        # redirect to contact endpoint
        flash("諮詢內容已傳送。感謝您來信諮詢")
        return redirect(url_for("contact_complete"))

    return render_template("contact_complete.html")


def send_email(to, subject, template, **kwargs):
    """傳送郵件的函數"""
    msg = Message(subject, recipients=[to])
    msg.body = render_template(template + ".txt", **kwargs)
    msg.html = render_template(template + ".html", **kwargs)
    mail.send(msg)

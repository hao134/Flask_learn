from flask import Flask, current_app, g, render_template, request, url_for

app = Flask(__name__)


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

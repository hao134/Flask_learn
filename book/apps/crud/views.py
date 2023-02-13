from flask import Blueprint, render_template

# 使用Blueprint建立crud應用程式
crud = Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static",
)


# 建立index端點並回傳index.html
@crud.route("/")
def index():
    return render_template("crud/index.html")

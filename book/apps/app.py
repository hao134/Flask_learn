from flask import Flask


# create create_app function
def create_app():
    # create flask 實體
    app = Flask(__name__)

    # 由 crud 套件匯入views
    from apps.crud import views as crud_views

    # 使用 register_blueprint，將views 的 crud 登入至應用程式
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app

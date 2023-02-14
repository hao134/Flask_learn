from pathlib import Path

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

# 建立 SQLAlchemy的實體
db = SQLAlchemy()
# 建立 CSRFProtect的實體
csrf = CSRFProtect()


# create create_app function
def create_app():
    # create flask 實體
    app = Flask(__name__)
    # 設定應用程式的組態
    sqlite_path = f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}"
    app.config.from_mapping(
        SECRET_KEY="2AZSMss3p5QPbcY2hBsJ",
        SQLALCHEMY_DATABASE_URI=sqlite_path,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        # 設定在控制台日誌輸出SQL
        SQLALCHEMY_ECHO=True,
        # WTF_CSRF_SECRET_KEY 設定隨機值
        WTF_CSRF_SECRET_KEY="AuwzyszU5sugKN7NZs6f",
    )

    # 連結 SQLAlchemy和應用程式
    db.init_app(app)
    # 連結 Migrate 和應用程式
    Migrate(app, db)
    # 使用 csrf.init_app函數連結應用程式。
    csrf.init_app(app)

    # 由 crud 套件匯入views
    from apps.crud import views as crud_views

    # 使用 register_blueprint，將views 的 crud 登入至應用程式
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app

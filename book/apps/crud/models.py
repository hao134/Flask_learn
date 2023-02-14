from datetime import datetime

from apps.app import db
from werkzeug.security import generate_password_hash


# 建立繼承 db.Model 的 User 類別
class User(db.Model):
    # 指定表格名稱
    __tablename__ = "users"
    # 定義 column 內容
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index=True)
    email = db.Column(db.String, unique=True, index=True)
    password_hash = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    # 設置密碼的屬性
    @property
    def password(self):
        raise AttributeError("無法加載")

    # 藉由設置密碼的setter函數，設定經過雜湊處理的密碼
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

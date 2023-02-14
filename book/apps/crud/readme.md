## Note

### flask SQLlchemy 對應sql 語法
```python
# ////取得一件紀錄
db.session.query(User).first()
# ////取得primary key 為2的紀錄
db.session.query(User).get(2)
# ////取得紀錄總數
db.session.query(User).count()
# ////單頁顯示10件時，顯示第2分頁的內容
db.session.query(User).paginate(2, 10, False)
# //// where(use filter_by) 取得id為2、Username 為 admin的紀錄
db.session.query(User).filter_by(id=2, username="admin").all()
# //// where(use filter) 取得id為2、Username 為 admin的紀錄
db.session.query(User).filter(User.id == 2, User.username == "admin").all()
# //// LIMIT 指定取得的紀錄件數為1件
db.session.query(User).limit(1).all()
# //// OFFSET 由第3件紀錄取得1件紀錄
db.session.query(User).limit(1).offset(2).all()
# //// ORDER BY 排序 username
db.session.query(User).order_by("username").all()
# //// GROUP BY 建立 username的群組
db.session.query(User).group_by("username").all()
# //// INSERT
user = User(username="test", email="test@email.com", password="password")
db.session.add(user)
db.session.commit()
# //// UPDATE
user = db.session.query(User).filter_by(id=1).first()
user.username = "test2"
user.email = "test@email.com"
user.password = "password2"
db.session.add(user)
db.session.commit()
# //// DELETE
user = db.session.query(User).filter_by(id=1).delete()
db.session.commit()
```
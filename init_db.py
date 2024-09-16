from app import create_app
from extensions import db
from models import User, Post, Comment

app = create_app()

with app.app_context():
    db.create_all()
    
    # 检查是否已存在管理员用户
    admin_user = User.query.filter_by(username='admin').first()
    if not admin_user:
        # 创建管理员用户
        admin_user = User(username='admin', email='admin@example.com')
        admin_user.set_password('123456')
        db.session.add(admin_user)
        db.session.commit()
        print("管理员用户已添加。")
    else:
        print("管理员用户已存在。")
    
    print("数据库表已创建。")
    print("用户名: admin")
    print("密码: 123456")
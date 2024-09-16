# myblog/app.py
from flask import Flask
from config import Config
from extensions import db, login_manager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    with app.app_context():
        from routes import main as main_blueprint
        app.register_blueprint(main_blueprint)
        
        # 移除这行，因为我们现在在 run.py 中处理数据库创建
        # db.create_all()

    return app

@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(int(user_id))
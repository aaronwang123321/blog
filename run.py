# myblog/run.py
import os
import logging
from app import create_app, db
from models import User, Post

app = create_app()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_db():
    with app.app_context():
        db.create_all()
        
        # 检查是否已存在管理员用户
        admin_user = User.query.filter_by(username='admin').first()
        if not admin_user:
            try:
                # 创建管理员用户
                admin_user = User(username='admin', email='admin@example.com')
                admin_user.set_password('123456')
                db.session.add(admin_user)
                db.session.commit()
                logger.info("管理员用户已添加。")
            except Exception as e:
                logger.error(f"创建管理员用户时出错: {str(e)}")
                db.session.rollback()
        else:
            logger.info("管理员用户已存在。")
        
        logger.info("数据库初始化完成。")

if __name__ == "__main__":
    db_path = os.path.join(app.root_path, 'blog.db')
    print(f"数据库文件路径: {db_path}")
    
    if not os.path.exists(db_path):
        logger.info("数据库不存在，正在创建并初始化...")
        init_db()
    else:
        logger.info("数据库已存在，跳过初始化步骤。")
    
    app.run(debug=True)
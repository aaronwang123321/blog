# myblog/routes.py
from flask import render_template, url_for, flash, redirect, request, Blueprint
from models import Post, User, Comment  # 确保 User 模型在 models.py 中定义
from forms import LoginForm, PostForm, CommentForm  # 假设 LoginForm 和 PostForm 在 forms.py 中定义
from flask_login import login_user, logout_user, login_required, current_user
from extensions import db

# 创建蓝图
main = Blueprint('main', __name__)

@main.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', posts=posts)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if user.check_password(form.password.data):
                login_user(user, remember=form.remember_me.data)
                next_page = request.args.get('next')
                return redirect(next_page or url_for('main.index'))
            else:
                print(f"密码验证失败: {form.password.data}")
        else:
            print(f"用户不存在: {form.username.data}")
        flash('Invalid username or password.')
    return render_template('login.html', title='登录', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))  # 修改这里

@main.route('/add', methods=['GET', 'POST'])
@login_required
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Post published.')
        return redirect(url_for('main.index'))  # 修改这
    return render_template('add_post.html', title='发布新文章', form=form)

@main.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(content=form.content.data, author=current_user, post=post)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been added!', 'success')
        return redirect(url_for('main.post', post_id=post.id))
    comments = post.comments.order_by(Comment.date_posted.desc()).all()
    return render_template('post.html', title=post.title, post=post, form=form, comments=comments)

# ... 其他路由 ...
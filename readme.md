## 代码编写说明

### 结构
myblog/
│
├── app.py                # 主 Flask 应用配置和工厂函数
├── config.py             # 配置文件
├── models.py             # SQLAlchemy 模型定义
├── forms.py              # WTForms 表单类定义
├── templates/            # 存放所有 HTML 模板文件
│   ├── base.html         # 基础模板，包含共用结构如导航栏和页脚
│   ├── index.html        # 首页模板
│   ├── post.html         # 显示单个博客文章的模板
│   ├── add.html          # 添加新文章的表单模板
│   ├── edit.html         # 编辑文章的表单模板
│   ├── login.html        # 登录表单模板
│   └── ...
│
├── static/               # 存放静态文件如 CSS, JavaScript, images 等
│   ├── css/              # CSS 文件
│   │   └── main.css
│   └── ...
├── migrations/           # 数据库迁移文件（Flask-Migrate）
│   ├── __init__.py
│   ├── alembic.ini
│   ├── env.py
│   └── versions/         # 存放自动生成的迁移脚本
│       └── ...
├── run.py                # 运行应用的脚本
└── requirements.txt       # 项目依赖列表

### 详细说明：
- **app.py**: 主 Flask 应用文件，包含路由、视图函数等。
- **models.py**: 包含 SQLAlchemy 模型定义。
- **forms.py**: 包含表单类，通常使用 WTForms 来定义。
- **templates/**: 存放所有的 HTML 模板文件，使用 Jinja2 模板引擎。
    - **base.html**: 基础模板，包含共用结构，如导航栏（navbar）和页脚（footer）。
    - **index.html**: 首页模板，显示博客文章列表。
    - **post.html**: 显示单个博客文章的详细内容。
    - **add.html**: 添加新文章的表单。
    - **edit.html**: 编辑文章的表单。
    - **login.html**: 用户登录表单。
- **static/**: 存放静态文件，如 CSS、JavaScript 文件和图片等。
    - **css/**: 存放 CSS 文件。
- **migrations/**: 如果使用 Flask-Migrate 进行数据库迁移，这个目录会包含迁移脚本和配置文件。
- **config.py**: 包含应用的配置，如数据库配置、密钥等。
- **run.py**: 一个简单的脚本，用于运行 Flask 应用，通常用于生产环境。
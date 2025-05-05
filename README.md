# NeuralFlow Backend API

## 项目简介
NeuralFlow Backend API 是一个基于 FastAPI 框架开发的后端服务，提供用户管理和其他功能的 RESTful API 接口。项目使用 MySQL 和 MongoDB 双数据库架构，支持异步操作。

## 技术栈
- FastAPI: 现代、快速的 Web 框架
- SQLAlchemy: SQL ORM 工具
- PyMongo/Motor: MongoDB 驱动（支持同步和异步操作）
- Uvicorn: ASGI 服务器
- Pydantic: 数据验证

## 项目结构
```
.
├── app/                     # 主应用程序目录
│   ├── __init__.py         # 应用程序初始化文件，包含数据库连接等配置
│   ├── main.py             # 应用程序入口文件，包含FastAPI实例和基础配置
│   ├── api/                # API路由层，处理HTTP请求和响应
│   ├── service/            # 业务逻辑层，实现具体的业务功能
│   ├── core/               # 核心配置和工具
│   └── models/             # 数据模型定义
└── requirements.txt        # 项目依赖清单
```

## 环境要求
- Python 3.6+
- MySQL
- MongoDB

## 安装与运行

1. 创建并激活虚拟环境：
```bash
python -m venv venv
.\venv\Scripts\activate
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 配置数据库：
- MySQL 连接 URL：`mysql+pymysql://user:password@localhost:3306/neuralflow`
- MongoDB 连接 URL：`mongodb://localhost:27017`

4. 运行应用：
```bash
python -m app.main
```
或
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## API 文档
启动服务后，可以访问以下地址查看 API 文档：
- Swagger UI：http://localhost:8000/docs
- ReDoc：http://localhost:8000/redoc

## 已实现的 API 接口
### 用户管理
- POST `/user/login` - 用户登录
- POST `/user/register` - 用户注册

### 系统状态
- GET `/health` - 健康检查
- GET `/` - 欢迎页面

## 开发指南
1. 新增 API 接口时，在 `app/api` 目录下创建相应的路由文件
2. 业务逻辑实现在 `app/service` 目录下
3. 数据模型定义在 `app/models` 目录下
4. 核心配置和工具函数放在 `app/core` 目录下

## 注意事项
- 开发环境中 CORS 已配置为允许所有源，生产环境请适当调整
- 数据库连接信息应该通过环境变量或配置文件管理
- 建议添加日志记录和异常处理机制

        
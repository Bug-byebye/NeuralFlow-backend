from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient

# FastAPI 实例
app = FastAPI(
    title="NeuralFlow Backend API",
    description="NeuralFlow 后端 API 服务",
    version="1.0.0"
)

# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MySQL 配置
MYSQL_URL = "mysql+pymysql://user:password@localhost:3306/neuralflow"
mysql_engine = create_engine(MYSQL_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=mysql_engine)
Base = declarative_base()

# MongoDB 配置
MONGODB_URL = "mongodb://localhost:27017"
mongo_client = MongoClient(MONGODB_URL)
mongo_db = mongo_client.neuralflow
# 异步 MongoDB 客户端
async_mongo_client = AsyncIOMotorClient(MONGODB_URL)
async_mongo_db = async_mongo_client.neuralflow

# MySQL 数据库依赖
def get_mysql_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# MongoDB 数据库依赖
def get_mongo_db():
    return mongo_db
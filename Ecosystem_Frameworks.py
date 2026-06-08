# Ecosystem_Frameworks.py
# Reference Guide: Web Frameworks, Databases, Task Queues, Data Science, and Machine Learning in Python

# ==========================================
# 1. WEB FRAMEWORKS
# ==========================================

# --- FastAPI (Modern, Fast Web API using Type Hints) ---
# Install: `pip install fastapi uvicorn`
# --- FastAPI App Example ---
# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/")
# def read_root():
#     return {"message": "Hello World"}

# --- Flask (Micro web framework) ---
# Install: `pip install Flask`
# --- Flask App Example ---
# from flask import Flask
# app = Flask(__name__)
# @app.route("/")
# def hello():
#     return "Hello World!"

# --- Django (Full-stack batteries-included web framework) ---
# Install: `pip install django`
# Setup: `django-admin startproject myproject`

# ==========================================
# 2. DATABASES & ORMs (SQLAlchemy, Alembic)
# ==========================================

# --- SQLAlchemy (Object Relational Mapper) ---
# Install: `pip install sqlalchemy`
# --- SQLAlchemy Model Example ---
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.orm import declarative_base
# Base = declarative_base()
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)

# --- Alembic (Database migrations tool for SQLAlchemy) ---
# Setup: `alembic init alembic`
# Create migration: `alembic revision --autogenerate -m "create users table"`
# Run migration: `alembic upgrade head`

# ==========================================
# 3. TASK QUEUES (Celery, RQ, Redis)
# ==========================================
# Used for running background, long-running, or asynchronous tasks.

# --- Celery with Redis broker ---
# Install: `pip install celery redis`
# --- Celery Task Example ---
# from celery import Celery
# app = Celery('tasks', broker='redis://localhost:6379/0')
# @app.task
# def add(x, y):
#     return x + y

# ==========================================
# 4. DATA SCIENCE (NumPy, pandas, Jupyter)
# ==========================================
#
# --- NumPy (Multi-dimensional arrays) ---
# Install: `pip install numpy`
#
# --- pandas (Data Analysis tables / DataFrames) ---
# Install: `pip install pandas`
# --- Pandas Example ---
# import pandas as pd
# df = pd.DataFrame({"name": ["Alice", "Bob"], "score": [95, 88]})
# print(df.mean(numeric_only=True))

# ==========================================
# 5. MACHINE LEARNING & AI (scikit-learn, PyTorch)
# ==========================================

# --- scikit-learn (Classical Machine Learning algorithms) ---
# Install: `pip install scikit-learn`
# --- Linear Regression Model Example ---
# from sklearn.linear_model import LinearRegression
# model = LinearRegression()

# --- PyTorch (Deep Learning / Neural Networks library) ---
# Install: Check pytorch.org for specific GPU (CUDA) or CPU build install commands.
# --- PyTorch Tensor Example ---
# import torch
# tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
# print(tensor)

print("Ecosystem_Frameworks references configured!")

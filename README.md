# Python ETL Pipeline: API to PostgreSQL

## 📌 Project Overview

This project is a modular ETL (Extract, Transform, Load) pipeline built using Python. It extracts product data from a public API, transforms and cleans the data, and loads it into a PostgreSQL database.

The goal of this project is to demonstrate real-world data engineering concepts including API ingestion, data transformation, and database loading using a modular and scalable architecture.

---

## 🏗️ Architecture

API → Extract Layer → Transform Layer → Load Layer → PostgreSQL

---

## ⚙️ Tech Stack

- Python
- Pandas
- Requests
- SQLAlchemy
- PostgreSQL
- Psycopg2

---

## 📁 Project Structure

data_pipeline_project/

├── main.py # Pipeline orchestrator  
├── config.py # Configuration (API + DB connection)  
├── extract.py # API data extraction logic  
├── transform.py # Data cleaning and transformation  
├── load.py # Load data into PostgreSQL  
├── requirements.txt  
└── README.md

---

## 🚀 Features

- Extracts data from a public REST API
- Handles API errors and timeouts
- Transforms nested JSON into structured tabular format
- Modular ETL pipeline design (Extract, Transform, Load separation)
- Loads cleaned data into PostgreSQL database
- Uses append mode for incremental data loading

---

## 📊 Dataset Structure

Final transformed dataset includes:

- product_id
- title
- price
- category
- rating
- rating_count

---

## 🛠️ Setup Instructions

### 1. Clone repository

git clone https://github.com/choudhrydaniyal/data-pipeline-project
cd data_pipeline_project

---

### 2. Install dependencies

pip install -r requirements.txt

---

### 3. Configure database

Update `config.py`:

API_URL = "https://fakestoreapi.com/products"

DB_URL = "postgresql+psycopg2://username:password@localhost:5432/database_name"

---

### 4. Create PostgreSQL table (optional)

CREATE TABLE products (
product_id INT PRIMARY KEY,
title TEXT,
price NUMERIC(10,2),
category TEXT,
rating FLOAT,
rating_count INT
);

---

### 5. Run pipeline

python main.py

---

## 🔄 How It Works

### Extract

Fetches data from API using requests.

### Transform

- Flattens nested JSON
- Extracts required fields
- Handles missing values safely

### Load

- Converts data into DataFrame
- Loads into PostgreSQL using SQLAlchemy
- Uses append mode for incremental loading

---

## 📌 Learning Outcomes

- API integration in Python
- Data transformation using pandas
- SQL database integration
- ETL pipeline architecture
- Modular Python project design

---

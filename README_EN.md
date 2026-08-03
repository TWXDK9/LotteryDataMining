# LotteryDataMining 🎲

[English](README_EN.md) | [中文](README.md)

A Python-based lottery data collection, cleaning, and data mining project.

---

## Project Introduction

LotteryDataMining is a data mining project developed with Python.

The project focuses on collecting historical lottery data, processing raw webpage information, building structured datasets, and performing statistical analysis.

The complete workflow includes:

```
Data Collection → HTML Parsing → Data Cleaning → Data Storage → Data Analysis
```

This project is mainly developed for learning and research purposes in:

- Web Scraping
- Data Processing
- Data Mining
- Statistical Analysis


---

## Data Source

The dataset is collected from the Sina Lottery SSQ trend webpage.

Source:

Sina Lottery - Double Color Ball Trend Data

The collected data includes:

- Lottery issue numbers
- Red ball numbers
- Blue ball numbers
- Historical trend information
- Statistical information from lottery charts


---

## Project Features

## 1. Data Collection

The project uses Python web scraping technology to collect lottery information.

Functions include:

- Sending HTTP requests
- Retrieving webpage HTML source code
- Extracting lottery trend tables
- Collecting historical lottery records


---

## 2. HTML Data Parsing

The project uses HTML parsing techniques to extract useful information from webpages.

Main operations:

- Locate lottery data tables
- Parse HTML elements
- Extract winning numbers
- Convert raw webpage data into structured information


---

## 3. Data Cleaning and Processing

Using Pandas for data processing:

Functions include:

- Data organization
- Data cleaning
- Data formatting
- Dataset generation


Example dataset:

|Issue|Red 1|Red 2|Red 3|Red 4|Red 5|Red 6|Blue|
|-|-|-|-|-|-|-|-|
|2023042|10|17|20|23|27|30|10|


---

## 4. Data Storage

The project supports exporting processed data into:

- CSV format
- Excel format


Generated datasets can be used for further:

- Statistical analysis
- Data visualization
- Machine learning experiments


---

# Project Structure

```
LotteryDataMining/

├── spider.py              # Web crawler for collecting lottery webpage data
│
├── extract_ssq.py         # Extract and process lottery numbers
│
├── requirements.txt       # Python package dependencies
│
├── environment.yml        # Conda environment configuration
│
├── README.md              # Chinese documentation
│
├── README_EN.md           # English documentation
│
└── .gitignore             # Git ignore configuration
```


---

# Technology Stack

## Programming Language

- Python 3.11


## Libraries

|Library|Purpose|
|-|-|
|Requests|HTTP requests and webpage access|
|BeautifulSoup4|HTML parsing|
|Pandas|Data processing and analysis|
|OpenPyXL|Excel file processing|
|HTML5lib|HTML parser support|


---

# Environment Setup

## Method 1: Using Conda (Recommended)

Create the environment:

```bash
conda env create -f environment.yml
```

Activate environment:

```bash
conda activate datamining
```


---

## Method 2: Using pip

Install dependencies:

```bash
pip install -r requirements.txt
```


---

# Usage

## Step 1: Collect Lottery Data

Run:

```bash
python spider.py
```

This script will:

- Request lottery webpage data
- Obtain HTML source code
- Save raw webpage information


---

## Step 2: Extract Lottery Numbers

Run:

```bash
python extract_ssq.py
```

This script will:

- Parse lottery records
- Extract red and blue ball numbers
- Generate structured datasets


Example output:

```
ssq_result.csv
```


Dataset format:

```
Issue,Red1,Red2,Red3,Red4,Red5,Red6,Blue
2023042,10,17,20,23,27,30,10
```


---

# Data Mining Applications

The generated dataset can be further used for:

## Statistical Analysis

Including:

- Number frequency analysis
- Hot and cold number analysis
- Distribution analysis
- Historical trend analysis


## Data Visualization

Possible visualization methods:

- Frequency charts
- Trend charts
- Distribution plots


## Machine Learning Research

Possible extensions:

- Feature engineering
- Classification models
- Random Forest
- XGBoost
- Time series analysis


---

# Project Workflow

```
Sina Lottery Website

        |
        v

Python Requests

        |
        v

HTML Source Code

        |
        v

BeautifulSoup Parsing

        |
        v

Data Cleaning

        |
        v

Pandas Processing

        |
        v

Structured Dataset

        |
        v

Data Mining Analysis
```


---

# Disclaimer

Lottery results are random.

This project is created only for:

- Data mining learning
- Programming practice
- Statistical analysis research

The analysis results do not represent actual lottery prediction or guarantee winning results.


---

# Future Improvements

Future development plans:

- Add automated data update function
- Build visualization dashboard
- Add statistical analysis notebooks
- Explore machine learning models
- Improve data processing pipeline


---

# Author

TWXDK9


---

# License

This project is for educational and research purposes only.

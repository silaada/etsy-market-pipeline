# etsy-market-pipeline

The aim of this project is to visualize Etsy market data on natural stone jewelry enriched by AI. 
The outcome is planned to determine the trends and price analysis in natural stone jewelry marketplace. 
This project can also be seen as part of my Analytics portfolio. 

## Tech Stack

Python (requests, pandas): ingestion

DuckDB: local analytical database

dbt: transformations and tests (planned)

## Setup

**Requirements**: Git, Python 3.13, an approved Etsy Open API v3 app.


- Make sure to have an approved ETSY_API_KEY and ETSY_SHARED_SECRET in hand 
- Clone the repository 
```
   git clone https://github.com/silaada/etsy-market-pipeline.git
   cd etsy-market-pipeline
```
- Create and activate a virtual environment 
```
   py -m venv .venv
   source .venv/Scripts/activate   # Windows (Git Bash)
   source .venv/bin/activate       # macOS / Linux
```
- Install dependencies (see requirements.txt)
```
   python -m pip install -r requirements.txt
```
- Create your `.env` file from the template and add your Etsy credentials, *ETSY_API_KEY* and *ETSY_SHARED_SECRET*:
```
   cp .env.example .env
```


## Status

Week 1: project setup ✅





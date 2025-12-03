# Movie-Critic-Ratings-Prediction

This project analyzes movie metadata and builds regression models to predict **critic ratings**. The goal is to explore which types of movie features are most predictive of critic scores.

## Structure
```
FINAL_PROJECT/
├── data/
│   └── movie_raw.csv
│
├── EDA_and_cleaning.ipynb
├── feature_and_modeling.ipynb
├── requirements.txt
└── README.md
```

## Workflow
- **Data Cleaning & EDA (`EDA_and_cleaning.ipynb`)**
    - Load data from `data/movie_raw.csv`
    - Remove invalid rows, converted dates, removed target‑leakage variables
    - Performed exploratory data analysis
- **Feature Engineering (`feature_and_modeling.ipynb`)**
    - Created numeric, pre‑release features
    - Train / Test Split
        - Train set: movies released before 2010
        - Test set: movies released in 2010 or later
- **Modeling (`feature_and_modeling.ipynb`)**
    - Trained six linear regression models
- **Evaluation **
    - Compared models using R², MAE, RMSE
    - Analyze feature importance


## Usage

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run Exploratory Data Analysis and Cleaning
Run ```EDA_and_cleaning.ipynb```. Processed data will be stored at ```data/movie_processed.csv```.

### Feature Engineering and Modeling
Run ```feature_and_modeling.ipynb```.

## Author
Selina Wang

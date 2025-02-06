## Bengaluru House Price Prediction

This project aims to predict house prices in Bengaluru using regression-based machine learning techniques. The dataset consists of 13,320 rows and 9 features: area_type, availability, location, size, society, total_sqft, bath, balcony, and price. The target variable is price, while the other features serve as predictors.

### Data Preprocessing & Feature Engineering

Handling Missing Values – Fill or remove missing data.

Feature Engineering – Create the BHK feature from size.

Cleaning total_sqft – Convert non-numeric values into digits.

Outlier Removal – Identify and remove outliers by comparing total_sqft and price.

Encoding Categorical Features – Convert area_type and location into numerical representations.

### Model Building

After preprocessing, multiple regression models were evaluated, with Linear Regression providing the best predictions.

#### Technologies Used

Python

Pandas, NumPy

Matplotlib, Seaborn

Scikit-Learn

Streamlit

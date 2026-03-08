 🏠 House Price Prediction System

A Machine Learning web application that predicts house prices based on key housing features such as area, number of bedrooms, bathrooms, house age, and distance to the city center.
The model is built using **Linear Regression** and deployed with **Streamlit** for real-time predictions.

##Project Overview

This project demonstrates an **end-to-end machine learning pipeline** including data generation, preprocessing, model training, evaluation, and deployment. The application allows users to input housing parameters and instantly receive predicted house prices.

The system is designed to simulate **1,500+ global housing records** including properties from multiple countries.

## Features

* Predict house prices using **Linear Regression**
* Trained on **1,500+ housing records**
* Supports **multiple countries**
* **Real-time prediction interface** using Streamlit
* Model evaluation using **R² Score and Mean Squared Error**
* Data preprocessing and normalization
* Interactive and user-friendly UI

##  Machine Learning Workflow

1. Data Generation (1500+ housing records)
2. Data Preprocessing
3. Feature Engineering
4. Train-Test Split
5. Data Normalization using **StandardScaler**
6. Model Training using **Linear Regression**
7. Model Evaluation
8. Deployment with **Streamlit**

## 📊 Model Evaluation Metrics

The model performance is evaluated using:

* **R² Score (Coefficient of Determination)**
* **Mean Squared Error (MSE)**

These metrics measure how accurately the model predicts housing prices.

## Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn

## Excution steps
I have excuted in anoconda promt
open vs code and save your file
1.open anaconda prompt in your laptop
2.cd downloads
3.dir ,this for checking the file of code
4.activate your file,activate house_env
5.pip install streamlit pandas numpy scikit-learn
6.streamlit run House_price_prediction.py
now you can see this
#Local URL: http://localhost:8501 open your output


##  Example Input

Users can input:

* Area (sqft)
* Number of Bedrooms
* Number of Bathrooms
* Age of House
* Distance to City Center
* Country

The system then predicts the **estimated house price**.

## 📈 Future Improvements

* Use real housing datasets (Kaggle / government datasets)
* Implement advanced models like **Random Forest or XGBoost**
* Deploy application on **Streamlit Cloud**
* Add visualizations and price trend graphs

gineer | Machine Learning Enthusiast


⭐ If you found this project helpful, please consider giving it a star!

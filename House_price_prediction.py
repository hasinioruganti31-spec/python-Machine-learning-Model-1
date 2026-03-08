import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

st.set_page_config(page_title="House Price Prediction - India", layout="centered")
st.title("🏠 House Price Prediction - India")
st.write("Predict house prices using Linear Regression (Synthetic Data)")

# Data Generation, here i have given only 5 cities 
cities = ["Hyderabad", "Mumbai", "Delhi", "Bangalore", "Chennai"]

data = []

for city in cities:
    for _ in range(100):
        area = np.random.randint(600, 3000)  # square feet
        bedrooms = np.random.randint(1, 6)
        bathrooms = np.random.randint(1, 5)
        age = np.random.randint(0, 20)

        # Base price per sq.ft for different cities
        if city == "Mumbai":
            price_per_sqft = 15000
        elif city == "Delhi":
            price_per_sqft = 12000
        elif city == "Bangalore":
            price_per_sqft = 10000
        elif city == "Chennai":
            price_per_sqft = 8000
        else:  # Hyderabad
            price_per_sqft = 9000

        price = (area * price_per_sqft) \
                + (bedrooms * 500000) \
                + (bathrooms * 300000) \
                - (age * 100000)

        data.append([city, area, bedrooms, bathrooms, age, price])

df = pd.DataFrame(
    data,
    columns=["City", "Area_sqft", "Bedrooms", "Bathrooms", "House_Age", "Price"]
)

#  Show Dataset 
if st.checkbox("Show Dataset"):
    st.dataframe(df.head(20))
    st.write("Total Records:", df.shape[0])

#  Encoding 
df_encoded = pd.get_dummies(df, drop_first=True)

X = df_encoded.drop("Price", axis=1)
y = df_encoded["Price"]

#  Train Model 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

#  User Input 
st.subheader("Enter Property Details")

city_input = st.selectbox("Select City", cities)
area_input = st.slider("Area (sq.ft)", 500, 4000, 1200)
bedrooms_input = st.slider("Number of Bedrooms", 1, 6, 2)
bathrooms_input = st.slider("Number of Bathrooms", 1, 5, 2)
age_input = st.slider("House Age (years)", 0, 30, 5)

input_data = pd.DataFrame([{
    "City": city_input,
    "Area_sqft": area_input,
    "Bedrooms": bedrooms_input,
    "Bathrooms": bathrooms_input,
    "House_Age": age_input
}])

#  Encode Input 
input_encoded = pd.get_dummies(input_data)
input_encoded = input_encoded.reindex(columns=X.columns, fill_value=0)

#  Prediction of price
if st.button("Predict Price"):
    prediction = model.predict(input_encoded)[0]
    st.success(f"🏠 Estimated House Price: ₹ {prediction:,.0f}")

st.write("---")
st.caption("Synthetic India Housing Data | Linear Regression Model")
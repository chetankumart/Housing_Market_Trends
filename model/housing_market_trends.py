import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler


# import matplotlib.pyplot as plt
# import seaborn as sns
def to_camel_case(text):
    # Split the string into words and capitalize each word except the first one
    words = text.split()
    return ('_'.join(word.capitalize() for word in words[1:])).lower()


def train_housing_model():
    # Load training data (assuming it's already uploaded in your Google Colab environment)
    data = pd.read_csv('USA_Housing.csv')

    if len(data) > 0:
        # data.columns = [to_camel_case(col) for col in data.columns]
        # Assuming 'Price' is the target variable and the rest are features
        X = data.drop('Price', axis=1)
        y = data['Price']

        # Convert categorical data if necessary and remove non-numeric columns
        X = pd.get_dummies(X, drop_first=True)  # Example for categorical conversion
        X = X.select_dtypes(include=[np.number])  # Remove non-numeric columns

        # Select features to scale
        # features = data[['area_house_age', 'area_number_of_bedrooms']]

        # Scale the features
        scaler = StandardScaler()
        # scaler.fit(features)
        X_scaled = scaler.fit_transform(X)

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

        # Initialize models
        linear_model = LinearRegression()
        gb_model = GradientBoostingRegressor(random_state=42)
        rf_model = RandomForestRegressor(random_state=42)

        # Train models
        linear_model.fit(X_train, y_train)
        gb_model.fit(X_train, y_train)
        rf_model.fit(X_train, y_train)

        return rf_model
        # # Linear Regression
        # linear_model = LinearRegression()
        # linear_model.fit(X_train, y_train)
        # linear_predictions = linear_model.predict(X_test)
        # linear_mse = mean_squared_error(y_test, linear_predictions)
        # linear_r2 = r2_score(y_test, linear_predictions)
        #
        # # Gradient Boosting
        # gb_model = GradientBoostingRegressor(random_state=42)
        # gb_model.fit(X_train, y_train)
        # gb_predictions = gb_model.predict(X_test)
        # gb_mse = mean_squared_error(y_test, gb_predictions)
        # gb_r2 = r2_score(y_test, gb_predictions)
        #
        # # Random Forest
        # rf_model = RandomForestRegressor(random_state=42)
        # rf_model.fit(X_train, y_train)
        # rf_predictions = rf_model.predict(X_test)
        # rf_mse = mean_squared_error(y_test, rf_predictions)
        # rf_r2 = r2_score(y_test, rf_predictions)
        #
        # results = pd.DataFrame({
        #     'Model': ['Linear Regression', 'Gradient Boosting', 'Random Forest'],
        #     'MSE': [linear_mse, gb_mse, rf_mse],
        #     'R-squared': [linear_r2, gb_r2, rf_r2]
        # })
        # print(results)
    else:
        return None


if __name__ == "__main__":
    train_housing_model()

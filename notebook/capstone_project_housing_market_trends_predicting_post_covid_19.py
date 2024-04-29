# -*- coding: utf-8 -*-
"""Capstone Project - Housing Market Trends Predicting Post-COVID-19.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HSLvnFWohT63Phj4LLgElrEOkSX5LYlQ

# Capstone Project: Predicting Post-COVID-19 Housing Market Trends

## Description of the Data
The dataset used in this analysis is `USA_Housing.csv`, which contains various features related to housing such as average area number of rooms, area population, price, etc. This data will help us understand how different factors are influencing the housing market trends post-COVID-19.

## Importing Libraries
Essential libraries for data manipulation, visualization, and machine learning.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA

"""## Loading and Checking the Dataset
Data is loaded from 'Updated_Enhanced_USA_Housing_with_Dates.csv' and checked for initial rows.

"""

data = pd.read_csv('/content/drive/MyDrive/Capstone Project Details/Updated_Enhanced_USA_Housing_with_Dates.csv')
data.drop('Unnamed: 0', axis=1, inplace=True)
data.head()

"""## Visualizing Avg. Area Income Distribution
Histogram plot of 'Avg. Area Income' using matplotlib.
"""

# @title Avg. Area Income

from matplotlib import pyplot as plt
data['Avg. Area Income'].plot(kind='hist', bins=20, title='Avg. Area Income')
plt.gca().spines[['top', 'right',]].set_visible(False)

"""## Exploratory Data Analysis
Descriptive statistics of dataset to understand the distributions.



"""

data.describe()

"""## Data Visualization
Initial pairplot is commented out for brevity.

"""

# sns.pairplot(data)

import pandas as pd
import matplotlib.pyplot as plt

# Calculate missing values
missing_values = data.isnull().sum()
print(missing_values)

# Plot missing values for columns with any missing data
missing_data = missing_values[missing_values > 0]
ax = missing_data.plot(kind='bar', color='skyblue')
plt.title('Missing Values per Feature')

# Annotate each bar with the count of missing values
for p in ax.patches:
    ax.annotate(str(int(p.get_height())), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 10), textcoords='offset points')

plt.show()

"""## Handling Missing Values
Missing values per feature are calculated and visualized in a bar chart.
Dropping rows with NaN values and printing data count before and after.


"""

print(f'Data count before droping NaN - {len(data)}')
data.dropna(inplace=True)
print(f'Data count after droping NaN - {len(data)}')

"""## Data Visualization Continued
Histograms for 'Avg. Area Income' and 'Price' with KDE.

"""

import seaborn as sns

# Plot distribution for 'Avg. Area Income'
sns.histplot(data['Avg. Area Income'], kde=True)
plt.title('Distribution of Avg. Area Income')
plt.show()

# Plot distribution for 'Price'
sns.histplot(data['Price'], kde=True)
plt.title('Distribution of Price')
plt.show()

"""## Correlation Analysis
Correlation heatmap for numeric features in the dataset.
"""

# Compute correlation matrix for numeric columns only
numeric_data = data.select_dtypes(include=[np.number])  # Select only numeric columns
corr = numeric_data.corr()

#specify size of heatmap
fig, ax = plt.subplots(figsize=(15, 5))

# Generate a heatmap
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Housing Features')
plt.show()

"""## Boxplot Visualization
Boxplot for 'Avg. Area Number of Bedrooms'.
"""

# Boxplot for 'Avg. Area Number of Bedrooms'
sns.boxplot(x=data['Avg. Area Number of Bedrooms'])
plt.title('Boxplot of Avg. Area Number of Bedrooms')
plt.show()

"""## Scatter Plot Analysis
Scatter plot of 'Price' vs 'Avg. Area Income'.
"""

# Scatter plot for 'Price' vs 'Avg. Area Income'
sns.scatterplot(x='Avg. Area Income', y='Price', data=data)
plt.title('Price vs Avg. Area Income')
plt.show()

"""# Pairplot of Selected Features
Pairplot for a subset of housing features.
"""

# Select a subset of columns for the pairplot
subset_data = data[['Price', 'Avg. Area Income', 'Avg. Area Number of Rooms', 'Area Population']]

# Generate a pairplot
sns.pairplot(subset_data)
plt.suptitle('Pairplot of Selected Housing Features', y=1.02)  # Adjust y for title spacing
plt.show()

"""## Time Series Analysis
Line chart for housing price trend over time.
"""

forcast_data = data.copy()

data['Date'] = pd.to_datetime(data['Date'])  # Convert date column to datetime
data.sort_values('Date', inplace=True)  # Sort the data by date

sns.lineplot(x='Date', y='Price', data=data)
plt.title('Housing Price Trend Over Time')
plt.show()

"""## Forecasting Future Prices
ARIMA model to forecast housing prices from 2024 to 2028.
"""

# forcast_data['Date'] = pd.to_datetime(forcast_data['Date'])
# forcast_data.set_index('Date', inplace=True)
# forcast_data.sort_index(inplace=True)

# # Check the last date in your data
# print("Last date in data:", forcast_data.index[-1])

# # Fit the ARIMA model as before
# model = ARIMA(forcast_data['Price'], order=(1,1,0))
# model_fit = model.fit()

# # Calculate the number of months to forecast from the start of 2024 to the end of 2028
# last_date = pd.to_datetime('2024-01-01')

# forcast_years = 5

# forecast = model_fit.get_forecast(steps=forcast_years)
# forecast_index = pd.date_range(start=last_date, periods=forcast_years + 1, freq='Y')[1:]
# forecast_series = pd.Series(forecast.predicted_mean, index=forecast_index)

# # Plot the observed and forecasted values
# sns.lineplot(data=forcast_data['Price'], label='Observed')
# sns.lineplot(data=forecast_series, color='red', label='Forecast')
# plt.title('Housing Price Forecast to 2028')
# plt.ylabel('Price')
# plt.xlabel('Date')
# plt.legend()
# plt.show()

"""## House Age vs Price Comparison with Heat Map
Correlation heatmap including 'House Age'.

"""

data['House Age'] = 2023 - data['Year Built']
numeric_data = data.select_dtypes(include=[np.number])  # Select only numeric columns

correlation_matrix = numeric_data.corr()

#specify size of heatmap
fig, ax = plt.subplots(figsize=(15, 5))

sns.heatmap(correlation_matrix, annot=True)
plt.show()

"""## Feature Engineering with OneHotEncoder
OneHotEncoding non-numeric columns and combining with numeric features.

"""

from sklearn.preprocessing import OneHotEncoder

# Let's assume 'State' is a non-numeric column you want to include
encoder = OneHotEncoder()
X = data.drop(['Price','Address',], axis=1)
state_encoded = encoder.fit_transform(X[['State']])
state_encoded = encoder.fit_transform(X[['City']])
state_encoded = encoder.fit_transform(X[['Property Type']])
state_encoded = encoder.fit_transform(X[['Date']])

# Now, combine this with your numeric data (excluding 'State' from X if it was there)
X_numeric = data.select_dtypes(include=[np.number])
X_combined = np.hstack((X_numeric.values, state_encoded.toarray()))

"""## Target Variable Selection
Selecting 'Price' as the target variable for prediction.
"""

# X = data.drop(['Price','Address', 'City', 'Property Type', 'Date'], axis=1)
y = data['Price']

"""## Scaling the Input Features
StandardScaler applied to input features for normalization.
"""

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_combined)

"""## Model Implementation
Training and predicting with Linear Regression, Gradient Boosting, and Random Forest.

"""

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Linear Regression
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
linear_predictions = linear_model.predict(X_test)
linear_mse = mean_squared_error(y_test, linear_predictions)
linear_r2 = r2_score(y_test, linear_predictions)

# Gradient Boosting
gb_model = GradientBoostingRegressor(random_state=42)
gb_model.fit(X_train, y_train)
gb_predictions = gb_model.predict(X_test)
gb_mse = mean_squared_error(y_test, gb_predictions)
gb_r2 = r2_score(y_test, gb_predictions)

# Random Forest
rf_model = RandomForestRegressor(random_state=42)
rf_model.fit(X_train, y_train)
rf_predictions = rf_model.predict(X_test)
rf_mse = mean_squared_error(y_test, rf_predictions)
rf_r2 = r2_score(y_test, rf_predictions)

"""## Model Performance Comparison
Comparison of Mean Squared Error and R-squared across models.

"""

results = pd.DataFrame({
    'Model': ['Linear Regression', 'Gradient Boosting', 'Random Forest'],
    'MSE': [linear_mse, gb_mse, rf_mse],
    'R-squared': [linear_r2, gb_r2, rf_r2]
})
print(results)

"""## Additional Models for Educational Purposes
Applying and comparing SVM and KNN models.
"""

# Plotting for visual comparison
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.bar(results['Model'], results['R-squared'], color='b')
plt.title('R-squared Comparison')
plt.subplot(1, 2, 2)
plt.bar(results['Model'], results['MSE'], color='r')
plt.title('MSE Comparison')
plt.show()

"""# Final Model Comparison
 Combined results from all models and visual comparison of performance metrics.

##Applying Additional Models for Comparison
###Support Vector Machines (SVM)
*   **Objective**: To find the hyperplane that best divides a dataset into classes (for classification) or fits the data (for regression).

*   **Why Not Chosen for Main Analysis**: SVMs can be highly effective but are generally more suited to classification tasks. In regression, they can be computationally intensive, especially for large datasets, and might not perform as well with a high number of features or data points due to increased training time and complexity.
"""

# Initialize and train the model
svm_model = SVR(kernel='linear')
svm_model.fit(X_train, y_train)

# Predict and evaluate
svm_predictions = svm_model.predict(X_test)
svm_mse = mean_squared_error(y_test, svm_predictions)
svm_r2 = r2_score(y_test, svm_predictions)

print("SVM MSE:", svm_mse)
print("SVM R-squared:", svm_r2)

"""##K-Nearest Neighbors (KNN)
*   **Objective:** To predict the output based on the 'K' nearest instances in the feature space.
*   **Why Not Chosen for Main Analysis:** KNN is very simple and effective for smaller datasets. However, it becomes impractical as the size of the dataset grows. It requires storing the entire dataset in memory, and the prediction time can be slow, which is a significant drawback for large datasets.


"""

from sklearn.neighbors import KNeighborsRegressor

# Initialize and train the model
knn_model = KNeighborsRegressor(n_neighbors=5)
knn_model.fit(X_train, y_train)

# Predict and evaluate
knn_predictions = knn_model.predict(X_test)
knn_mse = mean_squared_error(y_test, knn_predictions)
knn_r2 = r2_score(y_test, knn_predictions)

print("KNN MSE:", knn_mse)
print("KNN R-squared:", knn_r2)

"""##Comparison of All Models

"""

# Adding additional model results to the DataFrame
additional_results = pd.DataFrame({
    'Model': ['SVM', 'KNN'],
    'MSE': [svm_mse, knn_mse],
    'R-squared': [svm_r2, knn_r2]
})

# Combining results and displaying
all_results = pd.concat([results, additional_results], ignore_index=True)
print(all_results)

# Plotting for visual comparison of all models
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.bar(all_results['Model'], all_results['R-squared'], color='b')
plt.title('R-squared Comparison Across Models')
plt.subplot(1, 2, 2)
plt.bar(all_results['Model'], all_results['MSE'], color='r')
plt.title('MSE Comparison Across Models')
plt.show()

# Create a horizontal bar plot for R-squared values
plt.figure(figsize=(14, 7))
plt.subplot(1, 2, 1)
plt.barh(results['Model'], results['R-squared'], color='blue')
plt.xlabel('R-squared Score')
plt.title('R-squared Comparison Across Models')

# Sort by MSE in ascending order for logical high-to-low left-to-right visual comparison
all_results = results.sort_values(by='MSE')

# Create a horizontal bar plot for MSE values
plt.subplot(1, 2, 2)
plt.barh(all_results['Model'], all_results['MSE'], color='red')
plt.xlabel('Mean Squared Error')
plt.title('MSE Comparison Across Models')

plt.tight_layout()
plt.show()

"""## Persisting the Random Forest Model
Saving the trained Random Forest model using joblib.
"""

import numpy as np
from sklearn.linear_model import LinearRegression
import joblib  # For loading/saving models

# Load your model
joblib.dump(rf_model, '/content/drive/MyDrive/Capstone Project Details/rf_model.pkl')

"""## Loading Model Features
Retrieving feature names from the saved model.
"""

# Load the model
model = joblib.load('/content/drive/MyDrive/Capstone Project Details/rf_model.pkl')

# If the model is a scikit-learn pipeline where the final estimator is a model,
# and the training data included feature names:

if hasattr(model, 'feature_names_in_'):
    print(model.feature_names_in_)

# If the pipeline steps include transformers and a final estimator:
elif hasattr(model, 'named_steps') and 'final_estimator' in model.named_steps:
    estimator = model.named_steps['final_estimator']
    if hasattr(estimator, 'feature_names_in_'):
        print(estimator.feature_names_in_)
else:
  # Load the dataset
  data = pd.read_csv('/content/drive/MyDrive/Capstone Project Details/Updated_Enhanced_USA_Housing_with_Dates.csv')

  # Assuming the last column is the target variable
  features = data.columns[:-1]  # Adjust slicing as necessary
  print(features)

"""# User Input Function
Example function to collect user input for prediction.
"""

# If the model is not saved, ensure it's trained and replace the load with the model instance
model = joblib.load('/content/drive/MyDrive/Capstone Project Details/rf_model.pkl')  # Update path accordingly

# Function to accept user input
def get_user_input():
    # Example features (extending this to 99 features)
    features = np.zeros(4)  # Initialize all features with zeros or another default value

    # Prompt user for some key features
    year_built = float(input("Enter Year Built: "))
    bedrooms = float(input("Enter number of Bedrooms: "))
    bathrooms = float(input("Enter number of Bathrooms: "))
    salary = float(input("Enter salary: "))

    # Set these user-provided values in their respective positions
    features[0] = salary
    features[1] = bedrooms
    features[2] = bathrooms
    features[3] = year_built


    # Set other features as needed, possibly with default or imputed values
    # For example, if there are categorical features that need to be encoded or other numerical features:
    # features[2] = default_value_for_feature_3
    # features[3] = default_value_for_feature_4
    # ... until all 99 features are accounted for
    print(features.shape)
    return features.reshape(1, -1)  # Reshape for compatibility with model input


# Function to make a prediction
def make_prediction(input_data):
    prediction = model.predict(input_data)
    return prediction

# Main function to run the process
def main():
    user_input = get_user_input()  # Get user input
    prediction = make_prediction(user_input)  # Make prediction
    print(f"Predicted Output: {prediction[0]}")  # Print the predicted output

# Run the main function
if __name__ == "__main__":
    main()

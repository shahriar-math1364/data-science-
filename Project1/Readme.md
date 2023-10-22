# Used Car Price Regression Project

![Shakira](https://github.com/shahriar-math1364/data-science-/blob/main/Project1/usedcar.jpg)

## Project Overview
The dataset consists of various features of used cars, such as make, model, year, mileage, and more. These attributes serve as inputs for the model to predict the price of the vehicles.

## Table of Contents
- [Data](#data)
- [Installation](#installation)
- [Usage](#usage)
- [Data Preprocessing](#data-preprocessing)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Model Building](#model-building)
- [GridSearchCV for Hyperparameter Tuning](#gridsearchcv-for-hyperparameter-tuning) 
- [Evaluation](#evaluation)
- [Results](#results)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)

## Data
 Here's an outline of the main project components:


## Installation
List the necessary libraries and dependencies for running your project. You can include code snippets for installation.

## Usage

To utilize the project, follow these steps:

Clone the project repository from GitHub.
Install the required dependencies using pip install -r requirements.txt.
Run the Jupyter Notebook or Python script to build and train the regression model.
Input relevant data and obtain price predictions.
Make use of the model for accurate used car price estimation.

## Data Preprocessing

 - Unnecessary features, including 'id,' 'url,' 'image_url,' 'posting_date,' 'description,' 'VIN,' 'region_url,' 'county,' and 'model,' are removed.
    - Rows with missing values are dropped, resulting in a cleaner dataset.
    - Irrelevant columns, such as 'lat' and 'long,' are removed.
    - A new feature 'size-c' is created, combining 'compact' and 'subcompact' sizes.
    - Rows with prices less than 500 and years earlier than 2001 are filtered out.
    - The 'odometer' column is converted into intervals (e.g., 12 for an odometer reading between 120,000 and 130,000 miles).
    - A new column 'cyl1' is created by extracting the number of cylinders from the 'cylinders' column.
    - 'cyl1' values are standardized between 0 and 1.
    - Rows with 'title_status' values 'missing,' 'parts only,' or 'salvage' are replaced with 'mps.'
    - Categorical variables are one-hot encoded for use in machine learning models.
    - The 'year' column is scaled to values between 0 and 1 using MinMaxScaler.
    - Outliers in the dataset are identified based on 'odometer,' 'year,' 'condition,' and 'type,' and removed.


## Exploratory Data Analysis


## Model Building
The model building phase is focused on creating a regression model for used car price prediction. Key components of this phase include:

Selecting suitable regression algorithms, such as Linear Regression, Lasso, and Decision Tree Regressor.
Feature engineering to enhance model performance, including standardizing the 'year' and 'cylinders' features.
Training the model using the preprocessed dataset.
This section provides code and detailed insights into the model-building process, including the identification of the best-performing model.



## GridSearchCV for Hyperparameter Tuning:
To optimize the Decision Tree Regressor model, GridSearchCV is employed. This technique systematically explores various hyperparameters to determine the best configuration.
Hyperparameters such as 'criterion' (either 'mse' or 'friedman_mse') and 'splitter' ('best' or 'random') are included in the search space.
The model is evaluated using a 5-fold ShuffleSplit cross-validation strategy to ensure robust results.

## Evaluation


## Results


## Future Work


## Contributing

## License



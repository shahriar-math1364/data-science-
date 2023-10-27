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

![data](https://github.com/shahriar-math1364/data-science-/blob/main/Project1/Screenshot.png)

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

### Data Cleaning
- Columns like `lat` and `long` were considered irrelevant for our regression model and thus removed.
- Modifications were made to combine similar attributes, and new columns like `size-c` were introduced.
- Rows with suspicious data, like cars priced less than 500 or manufactured before 2001, were removed.
- Some columns underwent standardization processes using MinMaxScaler.

### Outlier Removal
- Outliers were identified using visualization tools such as scatterplots and boxplots.
- Specific criteria were set for outlier removal, based on attributes like `odo`, `year`, `condition`, and `type`.
- Entries with ambiguous attributes like `transmission` set to `other` were removed.

### Data Transformation
- One-hot encoding was applied to categorical variables, producing a new, transformed dataset.


## Exploratory Data Analysis
Exploratory data analysis uncovers insights by analyzing year-wise and odometer-wise price trends. Visualizations are used to discover data patterns and relationships between features and car prices.

![year-wise trend](https://github.com/shahriar-math1364/data-science-/blob/main/Project1/year-wise-trend.png)
![odometer reading vs price](https://github.com/shahriar-math1364/data-science-/blob/main/Project1/odometer-price.png)

Based on the graphs above, it is evident that there exist many outliers that need to be removed before training our model. 

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

Here are the results that we obtain:

![results](https://github.com/shahriar-math1364/data-science-/blob/main/Project1/result.png)

## Evaluation


## Results


## Future Work


## Contributing

## License



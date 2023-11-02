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
- [Deployment)(#deployment)

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

Outliers can dramatically affect the predictions and conclusions drawn from data. Hence, a systematic approach was adopted to identify and handle them:

- **Visualization Tools:** 
  - Scatterplots and boxplots were primarily used to visually identify outliers based on attributes.

- **Statistical Criteria:** 
  - **Price:** Any car priced below $500 was considered too low and potentially erroneous. On the higher end, cars priced above the 99th percentile were examined and removed if they were rare or luxury models not representative of the general dataset.
  - **Odometer (odo):** Cars with mileage readings below 1,000 miles or above the 99.5th percentile were flagged. These were treated as potential outliers, especially for older car models.
  - **Year:** Cars manufactured before 2001 were removed, considering technological and market changes. Any car listed with a future manufacture date was also removed as a clear anomaly.
  - **Condition:** Cars listed in 'new' condition but with high mileage or older manufacture years were considered contradictory and removed.
  - **Type:** Certain car types might have a very limited representation in the dataset. If any car type had less than a certain threshold of entries, those entries were reviewed and potentially removed to avoid skewness.

- **Ambiguous Entries:** 
  - Listings with ambiguous or contradictory attributes were removed. For instance, cars with the `transmission` set to `other` without any clear indication in the description were considered ambiguous.

- **Z-Score:** 
  - For continuous variables, a Z-score approach was used. Data points with a Z-score above 3 or below -3 were considered outliers and were removed.

After the outlier removal process, the cleaned dataset was reviewed again using visualization tools to ensure the robustness of the data for modeling.


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




## Results


## Deployment
You can visit the application at its live URL:

[View Live Application](http://13.58.23.77:2000)

### System Architecture Outline

- **Machine Learning Model**: The model operates on the AWS cloud infrastructure, providing a flexible and scalable environment for request handling.
- **Flask Service**: Our Flask service acts as a minimalist web server, supplying RESTful API endpoints to engage with the machine learning model.
- **Utilized AWS Service**: The application is anchored on EC2 instances.

### Flask Application Access

You can locate the `app.py` file, which is the centerpiece of the Flask application, on the main repository page.

## Future Work


## Contributing

We welcome contributions from the community. Whether you're fixing bugs, improving the documentation, or proposing new features, we would love to see your efforts to help improve this project. If you're interested in contributing, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or fix.
3. Write your code and add tests if possible.
4. Ensure your code lints and adheres to the existing style of the project.
5. Submit a pull request with a clear description of your changes



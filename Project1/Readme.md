# Used Car Price Regression Project

![Shakira](https://github.com/shahriar-math1364/data-science-/blob/main/Project1/images/usedcar.jpg)

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
- [Deployment](#deployment)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)


## Data
 Here's an outline of the main project components:

![data](https://github.com/shahriar-math1364/data-science-/blob/main/Project1/images/Screenshot.png)

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

![year-wise trend](https://github.com/shahriar-math1364/data-science-/blob/main/Project1/images/year-wise-trend.png)
![odometer reading vs price](https://github.com/shahriar-math1364/data-science-/blob/main/Project1/images/odometer-price.png)

Based on the graphs above, it is evident that there exist many outliers that need to be removed before training our model. 

## Model Building
To choose the best regression model for predicting used car prices, we evaluate multiple algorithms, including Linear Regression, Lasso Regression, and Decision Tree Regression, using cross-validation. We employ the ShuffleSplit method with five splits and measure the R-squared (R^2) score for each model.

After evaluating the models, we find that the Decision Tree Regression model performs the best with an R^2 score of approximately 0.83. This indicates that the model can explain about 83% of the variance in used car prices, making it a suitable choice for our prediction task.



## GridSearchCV for Hyperparameter Tuning:
To optimize the performance of our regression models, we employ GridSearchCV, a powerful technique that systematically explores various hyperparameters to determine the best configuration. This approach ensures that our models are fine-tuned for the best possible predictive accuracy.

#### Linear Regression

For the Linear Regression model, we search for the best hyperparameters by exploring the 'fit_intercept' parameter with values 'True' and 'False.' GridSearchCV evaluates different combinations using a 5-fold ShuffleSplit cross-validation strategy.

#### Lasso Regression

In the case of Lasso Regression, we tune hyperparameters like 'alpha' (with options 1 and 2) and 'selection' ('random' or 'cyclic'). GridSearchCV helps us find the optimal hyperparameters to improve model performance.

#### Decision Tree Regression

Similarly, for the Decision Tree Regression model, we optimize hyperparameters such as 'criterion' (either 'mse' or 'friedman_mse') and 'splitter' ('best' or 'random') using GridSearchCV. The model is evaluated with 5-fold cross-validation to ensure robust results.

Here are the results that we obtain:

![results](https://github.com/shahriar-math1364/data-science-/blob/main/Project1/images/result.png)




## Results
nnnnn

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



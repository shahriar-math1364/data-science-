# Used Car Price Regression Project

![Shakira](https://github.com/shahriar-math1364/data-science-/blob/main/Project1/images/usedcar.jpg)


## Project Overview

The world of buying and selling used cars is not only vast but also intricately varied. Factors such as make and model, year of manufacture, mileage, vehicle condition, and regional market trends are all pivotal in shaping the fair market value of a used car.

This project employs data science and machine learning techniques to construct a predictive model capable of accurately estimating used car prices. The dataset underpinning our analysis was originally sourced from Kaggle and provided by Austin Reese. For ease of access and to facilitate reproducibility of our analysis, the dataset has been made available directly via Google Drive.

Our aim is to create a valuable resource for buyers and sellers in the used car market. Accurate car valuations are crucial for sellers to set fair prices and for buyers to make cost-effective purchases, ensuring informed decision-making in the marketplace.

The dataset can be accessed through the following links:

- [Craigslist Cars+Trucks Data - Kaggle](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data)
- [Craigslist Cars+Trucks Data (CSV File) - Google Drive](https://drive.google.com/file/d/1xaEgaIWAkj5ETX3I4FAL6gMO1BS1_N3N/view?usp=drive_link)




### Objective

Our objective is to synthesize a tool of significant value for buyers and sellers within the used car bazaar. For the seller who seeks to negotiate a fair price, or the buyer in pursuit of a cost-effective purchase, an accurate valuation of a car's worth is indispensable for informed transactional decisions.



## Table of Contents
- [Data](#data)
- [Usage](#usage)
- [Data Preprocessing](#data-preprocessing)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Model Building](#model-building)
- [GridSearchCV for Hyperparameter Tuning](#gridsearchcv-for-hyperparameter-tuning) 
- [Results](#results)
- [Deployment](#deployment)
- [Future Work](#future-work)
- [Contributing](#contributing)



## Data
Our project relies on a comprehensive dataset that contains a wealth of information about used cars. Each entry in the dataset represents a specific vehicle and includes attributes such as:

- **Make and Model**: The manufacturer and model name of the car.
- **Year of Manufacture**: The year the car was built, which impacts its depreciation and technological features.
- **Mileage (Odometer Reading)**: The total distance the car has traveled, a critical indicator of wear and tear.
- **Condition**: The overall condition of the vehicle, which can range from 'new' to various stages of 'used.'
- **Fuel Type**: The type of fuel the car uses, which affects operating costs.
- **Title Status**: The legal status of the vehicle's title, which can impact its value.
- **Transmission Type**: The mechanism used for changing gears, which can affect driving experience and maintenance.
- **Drive Type**: The type of drive system (e.g., front-wheel drive, all-wheel drive) that affects performance.
- **Vehicle Type**: The category or body style of the car (e.g., sedan, SUV).
- **Paint Color**: The color of the vehicle, which may influence buyer preferences.
- **Size**: Information about the size of the car (e.g., compact, mid-size, full-size).
- **Region and State**: Geographic data providing insight into the car's location.

 Here's an an overview of the dataset:

![data](https://github.com/shahriar-math1364/data-science-/blob/main/Project1/images/Screenshot.png)



## Usage
Using the project is straightforward. Follow these steps:

1. **Clone the Repository:** Start by cloning the project repository from GitHub to your local machine.

2. **Install Dependencies:** After cloning, navigate to the project directory and use the **requirements.txt** file to install all the required dependencies, as mentioned in the Installation section.


3. **Run the Model:** Execute the Jupyter Notebook named **"regression-project.ipynb"** included in the repository. This notebook contains the code to build and train the regression model using the provided dataset.



## Exploratory Data Analysis
Exploratory data analysis uncovers insights by analyzing year-wise and odometer-wise price trends. Visualizations are used to discover data patterns and relationships between features and car prices.

![year-wise trend](https://github.com/shahriar-math1364/data-science-/blob/main/Project1/images/year-wise-trend.png)
![odometer reading vs price](https://github.com/shahriar-math1364/data-science-/blob/main/Project1/images/odometer-price.png)



## Data Preprocessing

### Data Cleaning
- Columns like `lat` and `long` were considered irrelevant for our regression model and thus removed.
- Modifications were made to combine similar attributes, and new columns like `size-c` were introduced.
- Rows with suspicious data, like cars priced less than 500 or manufactured before 2001, were removed.
- Some columns underwent **standardization** processes using **MinMaxScaler**.

### Outlier Removal

Outliers can dramatically affect the predictions and conclusions drawn from data. Hence, a systematic approach was adopted to identify and handle them:

- **Visualization Tools:** 
  - **Scatterplots** and **boxplots** were primarily used to visually identify outliers based on attributes.

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
One-hot encoding was applied to categorical variables, producing a new, transformed dataset.




Based on the graphs above, it is evident that there exist many outliers that need to be removed before training our model. 

## Model Building
To choose the best regression model for predicting used car prices, we evaluate multiple algorithms, including Linear Regression, Lasso Regression, and Decision Tree Regression, using cross-validation. We employ the ShuffleSplit method with five splits and measure the R-squared (R^2) score for each model.

After evaluating the models, we find that the Decision Tree Regression model performs the best with an R^2 score of approximately 0.83. This indicates that the model can explain about 83% of the variance in used car prices, making it a suitable choice for our prediction task.



## GridSearchCV for Hyperparameter Tuning:
To optimize the performance of our regression models, we employ **GridSearchCV**, a powerful technique that systematically explores various hyperparameters to determine the best configuration. This approach ensures that our models are fine-tuned for the best possible predictive accuracy.

#### Linear Regression

For the **Linear Regression model**, we search for the best hyperparameters by exploring the **'fit_intercept'** parameter with values **'True'** and **'False.'** GridSearchCV evaluates different combinations using a **5-fold ShuffleSplit** cross-validation strategy.

#### Lasso Regression

In the case of **Lasso Regression**, we tune hyperparameters like **'alpha'** (with options **1** and **2**) and **'selection'** ('random' or 'cyclic'). **GridSearchCV** helps us find the optimal hyperparameters to improve model performance.

#### Decision Tree Regression

Similarly, for the **Decision Tree Regression model**, we optimize hyperparameters such as **'criterion'** (either **'mse'** or **'friedman_mse'**) and **'splitter'** ('best' or 'random') using **GridSearchCV**. The model is evaluated with **5-fold cross-validation** to ensure robust results.

Here are the results that we obtain:

![results](https://github.com/shahriar-math1364/data-science-/blob/main/Project1/images/result.png)




## Results
### Linear Regression

- **R-squared (R²) Score**: 0.75
- **Description**: The **Linear Regression model** achieved an **R² score** of **0.75**, indicating that approximately **75%** of the variance in used car prices can be explained by the model. This demonstrates a moderate level of predictive accuracy.

### Lasso Regression

- **R-squared (R²) Score**: 0.72
- **Description**: The **Lasso Regression model** achieved an **R² score** of **0.72**, which represents a good fit to the data. This indicates that the model explains approximately **72%** of the variance in used car prices.

### Decision Tree Regression

- **R-squared (R²) Score**: 0.83
- **Description**: The **Decision Tree Regression model** outperformed other models with an **R² score** of **0.83**, suggesting a strong ability to predict used car prices. This model captures approximately **83%** of the variance in prices, indicating high predictive accuracy.

These results highlight the effectiveness of the **Decision Tree Regression model** in predicting used car prices. Further fine-tuning and optimization of models could potentially enhance predictive accuracy.

## Deployment

You can visit the application at its live URL:

[View Live Application](http://13.58.23.77:5000)


### System Architecture Outline

- **Machine Learning Model**: The model operates on the AWS cloud infrastructure, providing a flexible and scalable environment for request handling.
- **Flask Service**: Our Flask service acts as a minimalist web server, supplying RESTful API endpoints to engage with the machine learning model.
- **Utilized AWS Service**: The application is anchored on EC2 instances.

### Flask Application Access

You can locate the `app.py` file, which is the centerpiece of the Flask application, on the main repository page.




## Future Work
While this project has made significant strides in predicting used car prices, there are several avenues for future work and enhancements:

### 1. More Data Sources

- Expanding the dataset with additional sources of information can improve model accuracy. Collecting data on car maintenance history, accident reports, and ownership details can provide a more comprehensive view of a vehicle's condition.

### 2. Advanced Models

- Exploring more advanced machine learning techniques such as Random Forests, Gradient Boosting, or Neural Networks may lead to even more accurate price predictions. These models can capture complex relationships within the data.

### 3. Feature Engineering

- Further feature engineering, including creating new attributes and combining existing ones, can enhance the model's ability to capture valuable information from the data.

### 4. Text Data Analysis

- If the dataset includes textual descriptions of vehicles, natural language processing (NLP) techniques can be employed to extract additional insights. Sentiment analysis of user reviews or extracting key features from descriptions can be valuable.

### 5. Deployment

- Developing a user-friendly web application or API for real-time used car price predictions can make the model accessible to a broader audience, such as car buyers and sellers.

### 6. Continuous Model Improvement

- Implementing a continuous learning pipeline to update the model with new data regularly ensures that it remains accurate and relevant over time.

### 7. Geographic Insights

- Incorporating geographic data, such as regional market trends and location-specific factors, can improve the model's ability to predict prices accurately based on location.

These future work suggestions provide a roadmap for further enhancing the used car price prediction system. By implementing these improvements, the project can continue to evolve and offer more accurate and valuable insights for users.




## Contributing

We welcome contributions from the community. Whether you're fixing bugs, improving the documentation, or proposing new features, we would love to see your efforts to help improve this project. If you're interested in contributing, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or fix.
3. Write your code and add tests if possible.
4. Ensure your code lints and adheres to the existing style of the project.
5. Submit a pull request with a clear description of your changes



# Stress Predictor Classification Project

![Stress](https://github.com/shahriar-math1364/data-science-/blob/main/Project2/stress.jpg)

## Project Overview
This classification project aims to identify the leading predictors of stress in individuals. Stress is a common issue in today's fast-paced world, and understanding the factors that contribute to it can help individuals and organizations mitigate its effects. The project's primary goal is to build a predictive model that can classify whether an individual is likely to experience stress based on various features and variables.

## Table of Contents
- [Data](#data)
- [Installation](#installation)
- [Usage](#usage)
- [Data Preprocessing](#data-preprocessing)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Model Building](#model-building)
- [Evaluation](#evaluation)
- [Results](#results)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)

## Data
- The dataset used for this project is available [here](https://colab.research.google.com/drive/1wG7cYUX3TBkP-RDljvOlcAX18QhYWrOc).
- It includes information about individuals, their occupations, physical activity levels, sleep patterns, and more.
- The data is used for training and evaluating the stress prediction model. Here is an overview of the dataset:

![data](https://github.com/shahriar-math1364/data-science-/blob/main/Project2/images/Screenshot.png)



## Installation
- The project relies on popular Python libraries, including Pandas, Scikit-Learn, and XGBoost.
- To install the required dependencies, use `pip install -r requirements.txt`.

## Usage
- To replicate this project, you can follow the Jupyter Notebook, 'Classification project.ipynb,' available in this repository.
- The notebook provides a step-by-step guide on data preprocessing, feature selection, model training, and evaluation.


## Data Preprocessing

The data preprocessing step is crucial to ensure that the dataset is clean and suitable for machine learning model training. In this section, we describe the various preprocessing steps we performed:

### Handling Missing Values

The first step in data preprocessing is addressing missing data. We utilize the Pandas library to check for missing values within our dataset. A heatmap visualization is employed to visualize the distribution of missing values, providing a clear view of the completeness of our data. This transparency is essential for understanding the quality of the dataset and deciding how to handle missing values effectively.

### Feature Engineering

Feature engineering is a critical process that enhances the predictive power of machine learning models. In this project, we apply feature engineering techniques to our dataset:

- **One-Hot Encoding**: To handle categorical variables ('Gender', 'Occupation', 'BMI Category', 'Sleep Disorder'), we use Pandas' get_dummies function. This process converts categorical variables into binary values, making it easier to integrate these variables into our machine learning model. One-hot encoding is a standard method to handle categorical data, ensuring the model can work with these features effectively.

- **Min-Max Scaling**: To standardize numeric features ('Age', 'Sleep Duration', 'Quality of Sleep', 'Daily Steps', 'Heart Rate'), we utilize the MinMaxScaler from Scikit-Learn. Min-Max scaling transforms numeric attributes to a common scale, ensuring that all features contribute equally to the model's performance. This step promotes consistent and effective model training.

- **Restructuring 'Blood Pressure'**: The 'Blood Pressure' column is restructured into separate 'Systolic_BP' and 'Diastolic_BP' columns. This restructuring simplifies the data format, enabling more straightforward analysis and modeling. We perform this transformation to make the dataset more accessible and structured for model training.

### Feature Selection

Feature selection is a pivotal aspect of model performance improvement. In our project, we employ the SelectKBest method in combination with the ANOVA F-value score to identify the most relevant features for our machine learning models. We also create visualizations to depict the relationship between the number of features selected (k) and the resulting model accuracy. This helps us determine the optimal number of features for our models, balancing predictive power and model complexity.

Furthermore, we generate a bar plot to display the feature importance scores for the selected features. This visualization offers valuable insights into which attributes have the most significant impact on our predictive models. By understanding feature importance, we can make informed decisions about which attributes to retain or exclude in our model training process.


## Exploratory Data Analysis
- The EDA section explores the dataset, including data distribution and key insights. It also discusses the relationship between feature selection and model accuracy.

## Model Building
- This section covers the training of three machine learning models:
  - Support Vector Machine (SVM)
  - Logistic Regression
  - XGBoost with GridSearchCV for hyperparameter tuning.

## Evaluation
- The evaluation section presents the performance metrics for each model, including accuracy, a classification report, and a confusion matrix. It highlights the accuracy achieved by each model.

## Results
- The results section discusses the model with the highest accuracy, the XGBoost model after hyperparameter optimization. The project showcases this model as the best-performing one, with an accuracy of approximately 97%.

![xgboost](https://github.com/shahriar-math1364/data-science-/blob/main/Project2/images/report-xgboost.png)

## Future Work
- In the future, this project could be expanded by:
  - Collecting more data to improve model accuracy.
  - Implementing real-time stress level prediction for individuals.
  - Exploring additional machine learning algorithms for comparison.

## Contributing
- Contributions to this project are welcome. If you have ideas for improvements or new features, please feel free to open issues or submit pull requests.

## License
- This project is under the [MIT License](LICENSE).

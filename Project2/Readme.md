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
- The data is used for training and evaluating the stress prediction model.

## Installation
- The project relies on popular Python libraries, including Pandas, Scikit-Learn, and XGBoost.
- To install the required dependencies, use `pip install -r requirements.txt`.

## Usage
- To replicate this project, you can follow the Jupyter Notebook, 'Classification project.ipynb,' available in this repository.
- The notebook provides a step-by-step guide on data preprocessing, feature selection, model training, and evaluation.


## Data Preprocessing
- This section outlines the data preprocessing steps, including:
  - Creating dummy variables for categorical features.
  - Standardizing numeric features using MinMaxScaler.
  - Splitting the 'Blood Pressure' column into systolic and diastolic components.
  - Removing unnecessary columns to create a new DataFrame with normalized and numeric features.

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

## Future Work
- In the future, this project could be expanded by:
  - Collecting more data to improve model accuracy.
  - Implementing real-time stress level prediction for individuals.
  - Exploring additional machine learning algorithms for comparison.

## Contributing
- Contributions to this project are welcome. If you have ideas for improvements or new features, please feel free to open issues or submit pull requests.

## License
- This project is under the [MIT License](LICENSE).

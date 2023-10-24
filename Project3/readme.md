# Women Singers Classification Project with Support Vector Machine

![Project Image/GIF]

## Project Overview
The project is focused on the detection and recognition of celebrity faces from images. Leveraging the power of computer vision libraries, specifically OpenCV, the project provides the ability to preprocess images by cropping only the face section when two eyes are detected. This ensures that only useful features are fed into the machine learning models. The project also explores a method called Wavelet Transformation to extract features from an image that can be further used for classification.

The dataset comprises images of various female celebrities, like Rihanna, Katy Perry, etc., stored in folders named after the respective celebrity. The images are then preprocessed, and the cropped face sections are stored in separate folders.

For the classification task, the project utilizes various machine learning algorithms such as Support Vector Machines (SVM), Random Forest, Logistic Regression, K-Nearest Neighbors, and Decision Trees. Grid Search Cross Validation is performed on these models to identify the best hyperparameters for the given data. The performance of each model is then compared based on accuracy.

Finally, the best-performing model (in this case, an SVM model) is serialized using Python's pickle module for potential future use or deployment.

## Table of Contents
- [Data](#data)
- [Installation](#installation)
- [Usage](#usage)
- [Data Preprocessing](#data-preprocessing)
- [Feature Engineering](#feature-engineering)
- [Model Building](#model-building)
- [Evaluation](#evaluation)
- [Results](#results)
- [Deployment](#deployment) 
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)

## Data
The dataset used in this project contains information about women singers, including their biographical details, vocal characteristics, and music genres. It includes features such as age, vocal range, style, and more. The dataset consists of [number] rows and [number] columns. A detailed description of the features can be found in the data dictionary within the project repository.

## Installation
To run this project and the SVM classifier, you'll need to install the required Python libraries and dependencies. You can do this using pip:

## Data Preprocessing

- **Face Detection:** Leveraging Haarcascades from OpenCV, we identify the facial region in images. An image is valid only when two eyes are detected:

![eyes](https://github.com/shahriar-math1364/data-science-/blob/main/Project3/images/eyes.png)

- **Cropping:** Images are cropped to only contain the facial region, ensuring irrelevant features are excluded.
- **Wavelet Transformation:** To extract critical features, images undergo Wavelet Transformation, converting them into a machine-friendly format

## Model Building

**Wavelet Transformation:** Before model training, a critical step in feature extraction involves applying Wavelet Transform to the preprocessed images. Wavelet Transformation decomposes an image into different frequency sub-bands, effectively capturing both spatial and frequency information. This allows the model to discern intricate patterns in the image which might be challenging to capture with raw pixel values alone.

Various classification algorithms were then applied to the wavelet-transformed features:
- **Support Vector Machines (SVM):** SVMs are especially suited for high dimensional data, making them an excellent choice for image data post-wavelet transformation.
- **Random Forest**
- **Logistic Regression**
- **K-Nearest Neighbors (KNN)**
- **Decision Trees**


**Hyperparameter Tuning:** Grid Search Cross Validation was utilized for each algorithm to identify the optimal set of hyperparameters. Here is the result of the Grid Search:

![Gridsearch](https://github.com/shahriar-math1364/data-science-/blob/main/Project3/images/result.png)

## Results

The SVM emerged as the superior model, delivering the highest accuracy among all tested algorithms. 

## Deployment

The model has been successfully deployed to Google Cloud. This allows for real-time predictions and broadens the potential applications of our celebrity face recognition system. The deployment on Google Cloud ensures high availability and scalability, enabling users to access the model from anywhere and at any scale.

For access details, API documentation, and usage instructions related to the Google Cloud deployment, please refer to the [Deployment Documentation](link-to-your-deployment-documentation).

## Contributing

Contributions are welcomed! Please fork the project and create a pull request with your changes.

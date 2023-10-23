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
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)

## Data
The dataset used in this project contains information about women singers, including their biographical details, vocal characteristics, and music genres. It includes features such as age, vocal range, style, and more. The dataset consists of [number] rows and [number] columns. A detailed description of the features can be found in the data dictionary within the project repository.

## Installation
To run this project and the SVM classifier, you'll need to install the required Python libraries and dependencies. You can do this using pip:

## Data Preprocessing

- **Face Detection:** Leveraging Haarcascades from OpenCV, we identify the facial region in images. An image is valid only when two eyes are detected.
- **Cropping:** Images are cropped to only contain the facial region, ensuring irrelevant features are excluded.
- **Wavelet Transformation:** To extract critical features, images undergo Wavelet Transformation, converting them into a machine-friendly format

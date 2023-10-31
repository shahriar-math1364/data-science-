# Women Singers Classification Project with Support Vector Machine

![Project Image/GIF](https://github.com/shahriar-math1364/data-science-/blob/main/Project3/images/4.jpg)

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
The project is based on Python and requires several libraries, including:
- `opencv-python`
- `numpy`
- `matplotlib`
- `pywt`
- `scikit-learn`

You can install these packages using `pip`:


```bash
pip install opencv-python numpy matplotlib pywt scikit-learn
```


## Data Preprocessing

- **Face Detection:** Leveraging Haarcascades from OpenCV, we identify the facial region in images. An image is valid only when two eyes are detected:

![eyes](https://github.com/shahriar-math1364/data-science-/blob/main/Project3/images/eyes.png)

- **Cropping:** Images are cropped to only contain the facial region, ensuring irrelevant features are excluded.
- **Wavelet Transformation:** To extract critical features, images undergo Wavelet Transformation, converting them into a machine-friendly format

![before](https://github.com/shahriar-math1364/data-science-/blob/main/Project3/images/before-wave.png)
![after](https://github.com/shahriar-math1364/data-science-/blob/main/Project3/images/after-wave.png)

## Model Training Process

This section provides an in-depth overview of the model training process for celebrity image classification using a combination of raw and wavelet-transformed image features.

### Data Preparation

#### Cropped Image Collection
- Cropped images of various women celebrities are collected and organized into separate directories.
- Each directory corresponds to a specific celebrity, such as Katy Perry, Rihanna, etc.

#### Celebrity Data Mapping
- A Python dictionary named `celebrity_file_names_dict` is created to establish a mapping between celebrity names and lists of file paths to their respective cropped images.
- This mapping simplifies the organization and retrieval of images during the training process.

#### Class Labeling
- To facilitate supervised learning, class labels are assigned to each celebrity.
- Each celebrity is associated with a unique integer label.
- This step prepares the data for classification.

### Feature Extraction

#### Raw Images
- Raw color images are resized uniformly to a size of 32x32 pixels.
- The resized images are then flattened into a single 1D array of 4096 float values.
- This process prepares the raw image data for feature extraction.

#### Wavelet Transform Features
- The model training process leverages wavelet transform features.
- The `w2d` function is applied to each cropped image.
- The Haar wavelet is chosen, and the transform is performed at a level of 5.
- The resulting wavelet-transformed images are resized to 32x32 pixels and flattened into 1D arrays of 1024 float values.

### Data Concatenation

#### Combined Features
- Features extracted from both the raw images and wavelet-transformed images are concatenated for each image.
- This concatenation results in a combined feature vector of 5120 float values for each image.
- The combined feature vector encapsulates the information from both raw and wavelet-transformed representations.

### Data Splitting

#### Training and Testing Sets
- The dataset is divided into training and testing sets.
- The `train_test_split` function from scikit-learn is utilized for this purpose.
- This split ensures that a portion of the data is reserved for training the model, while the remainder is dedicated to evaluating its performance.

## Model Building

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

# Women Singers Classification Project with Support Vector Machine

![Project Image/GIF](https://github.com/shahriar-math1364/data-science-/blob/main/Project3/images/4.jpg)

## Project Overview
The project is focused on the detection and recognition of celebrity faces from images. Leveraging the power of computer vision libraries, specifically OpenCV, the project provides the ability to preprocess images by cropping only the face section when two eyes are detected. This ensures that only useful features are fed into the machine learning models. The project also explores a method called Wavelet Transformation to extract features from an image that can be further used for classification.

The dataset comprises images of various female celebrities, like Rihanna, Katy Perry, etc., stored in folders named after the respective celebrity. The images are then preprocessed, and the cropped face sections are stored in separate folders.

For the classification task, the project utilizes various machine learning algorithms such as Support Vector Machines (SVM), Random Forest, Logistic Regression, K-Nearest Neighbors, and Decision Trees. Grid Search Cross Validation is performed on these models to identify the best hyperparameters for the given data. The performance of each model is then compared based on accuracy.

Finally, the best-performing model (in this case, an SVM model) is serialized using Python's pickle module for potential future use or deployment.

## Table of Contents
- [Data](#data)
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

The dataset for this project consists of images of the mentioned singers: Katy Perry, Rihanna, Beyoncé, and Lady Gaga. These images were obtained using the FatCun tool, which facilitated the downloading of images from various online sources and search engine results.

### Preprocessing Steps

Before the model training process, the images underwent several preprocessing steps:

1. **Cropping:** The images were cropped to isolate the facial features of the singers. This step helped focus the model's analysis on the key visual characteristics necessary for distinguishing between the artists.

2. **Grayscale Conversion:** To simplify and standardize the data, the images were converted to grayscale, reducing the dimensionality of the dataset.

3. **Wavelet Transformation:** A wavelet transformation was applied to the images to extract relevant features and enhance certain visual characteristics. This transformation helps in capturing important patterns in the images.

These preprocessing steps were crucial to prepare the data for model training, ensuring that the model receives relevant and standardized input. The curated dataset of singer images is now ready to be used for training and developing a machine learning model capable of accurately classifying the four artists.



## Usage

Using the project is straightforward. Follow these steps:

1. **Clone the Repository**: Start by cloning the project repository from GitHub to your local machine.

2. **Install Dependencies**: After cloning, use the provided requirements.txt file to install all the required dependencies, as mentioned in the Installation section.

   ```bash
   pip install -r requirements.txt

3. **Open the Jupyter Notebook**: Launch your Jupyter Notebook environment and open the `women_celebrity.ipynb` notebook included in the repository.

4. **Execute the Notebook**: Inside the Jupyter Notebook, you'll find step-by-step instructions and code cells. Follow these instructions to explore the project, preprocess images, train the machine learning model, and perform singer classification.

Feel free to reach out if you have any questions or encounter any issues while using the project. Happy classifying!


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

## Wavelet Transform Features

To enable the machine learning model to effectively learn distinctive patterns and features from the singer's facial characteristics and expressions, we employ a process that involves wavelet transform features. Here's how this process works:

1. **Image Preprocessing**: Before feeding images into the model, we preprocess each cropped image using the `w2d` function. This function applies a series of operations to enhance important image details while reducing noise.

2. **Grayscale Conversion and Normalization**: Initially, the input color image is converted to grayscale. Subsequently, the image is converted to a floating-point representation and normalized to the range [0, 1]. This ensures consistent scaling across all images.

3. **Wavelet Transform**: The core of the preprocessing involves the wavelet transform, implemented using the PyWavelets library (`pywt`). This transform decomposes the grayscale image into a set of coefficients at various scales and orientations.

4. **Coefficients Manipulation**: To emphasize essential image features, the `coeffs_H` variable is derived from the coefficients obtained in the previous step. Notably, all coefficients at the lowest scale, which correspond to approximation coefficients, are set to zero. This selective manipulation preserves the image's critical details and edges.

5. **Reconstruction**: After processing the coefficients, the inverse wavelet transform (`pywt.waverec2`) is applied to reconstruct the image. This reconstructed image now contains enhanced details and edges, making it more suitable for analysis.

6. **Scaling and Flattening**: The reconstructed image is scaled back to the 8-bit unsigned integer format (`np.uint8`) and multiplied by 255 to restore its pixel value range. Furthermore, these processed images are resized uniformly to a standard size of 32x32 pixels. Finally, they are flattened into 1D arrays, each consisting of 1024 float values.

These wavelet-transformed and flattened images serve as the feature vectors for our machine learning model. They encapsulate vital information about the singer's facial characteristics, which the model leverages to classify singers effectively.

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


The project is deployed on Amazon Web Services (AWS), making use of its robust, scalable cloud computing resources to ensure high availability and performance. The application backend is a Flask app which serves as an interface to the machine learning model.

### Deployment Link


The deployed application is accessible at the following URL: ![Live Application]()

### Architecture Overview

- **Machine Learning Model**: Hosted on AWS, the model is scalable and can handle a variable number of requests.
- **Flask Application**: A lightweight web server that provides REST API endpoints for interacting with the machine learning model.
- **AWS Service**: EC2

### Accessing the Flask App

The `app.py` file is the Flask application's main file and can be found at this page.


## Contributing

Contributions are welcomed! Please fork the project and create a pull request with your changes.

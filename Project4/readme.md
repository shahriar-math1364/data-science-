# Tomato Disease Classification Project with Convolutional Neural Networks (CNN)

![tomato disease](https://github.com/shahriar-math1364/data-science-/blob/main/Project4/tomato%20disease.jpg)

## Project Overview
This project focuses on the automated classification of tomato plants affected by various diseases using Convolutional Neural Networks (CNN). The aim is to create a robust model capable of accurately identifying and categorizing diseases in tomato plants, which can be invaluable for early disease detection in agriculture.

## Table of Contents
- [Data](#data)
- [Installation](#installation)
- [Usage](#usage)
- [Data Preprocessing](#data-preprocessing)
- [Model Architecture](#model-architecture)
- [Training](#training)
- [Evaluation](#evaluation)
- [Results](#results)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)

## Data
The dataset used in this project consists of images of healthy tomato plants and various diseases, including [list diseases]. The dataset comprises a total of [number] images, which are divided into training, validation, and testing sets. More information about the dataset can be found in the data description in the project repository.

## Installation
To run this project and the CNN-based tomato disease classification model, you'll need to install the required Python libraries and dependencies. You can do this using pip:

```bash
pip install -r requirements.txt
```

## Data Preprocessing

1. **Loading & Visualization**: Data is directly loaded from the directory structure using TensorFlow's `image_dataset_from_directory`.
2. **Splitting**: Data is methodically split into training (80%), validation (10%), and test sets (10%).
3. **Augmentation**: To enhance model robustness, we applied horizontal and vertical flipping, and random rotation.
4. **Normalization**: All images are resized to 256x256 pixels and pixel values are rescaled to range [0,1].


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

## Model Building

The model architecture designed for this task is a multi-layered Convolutional Neural Network (CNN). Here's a breakdown of its components and the reasoning behind each choice:

### **Input Preprocessing Layers:**
- **Resizing and Rescaling Layer**: 
  - **Purpose**: Ensure all images have consistent dimensions and normalized values.
  - **Details**: Images are resized to a uniform 256x256 pixels and rescaled to have pixel values between [0,1]. This step ensures consistency in input data and aids in faster convergence during training.

### **Convolutional Layers:**
- **Purpose**: These layers learn spatial hierarchies of features.
  - **Configuration**: 
    - Total of five convolutional layers.
    - Each has a kernel size of 3x3.
    - Activation function: 'ReLU'.
    - Using multiple convolutional layers allows the model to learn intricate features and patterns. The ReLU activation helps counter the vanishing gradient problem and introduces non-linearity.

### **Pooling Layers:**
- **Purpose**: Reduction of spatial dimensions of feature maps, enabling fewer parameters and computational savings without significant feature loss.
  - **Configuration**: 
    - Max-pooling is used post each convolutional layer.
    - Pooling window size: 2x2.
    - Max-pooling ensures dominant spatial features are retained.

### **Flattening:**
- **Purpose**: Transitioning from 2D feature maps to 1D vector for dense layers.
  - The 2D feature map obtained post the final pooling step is converted to a 1D vector.

### **Dense (Fully Connected) Layers:**
- **Purpose**: Decision-making based on learned features from preceding layers.
  - **Configuration**: 
    - Initial dense layer: 64 units with 'ReLU' activation.
    - Output layer: 10 units (corresponding to 10 tomato classes) with 'Softmax' activation.
    - Softmax activation gives a probability distribution over classes, apt for multi-class classification.

### **Model Compilation:**
- **Optimizer**: Adam, known for its adaptive learning rate, potentially speeding up convergence.
- **Loss Function**: Sparse Categorical Crossentropy - ideal for multi-class, mutually exclusive classification.

### **Rationale:**
CNNs have excelled in image classification due to their ability to discern hierarchical spatial features in images. Starting from basic edge detectors, they proceed to understand advanced patterns. Our architecture, infused with multiple layers, aims to extract a diverse set of features from the tomato images, enhancing classification accuracy.

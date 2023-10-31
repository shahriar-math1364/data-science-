# Tomato Disease Classification Project with Convolutional Neural Networks (CNN)

![tomato disease](https://github.com/shahriar-math1364/data-science-/blob/main/Project4/tomato%20disease.jpg)

## Project Overview
Tomatoes are one of the most cultivated crops around the world. Identifying diseases in tomatoes at an early stage can help in ensuring their healthy growth and increasing yield. This project aims to classify different types of tomato diseases using Convolutional Neural Networks (CNN) by analyzing images of the leaves.


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


## Data
The dataset used in this project consists of images of healthy tomato plants and various diseases, including:

- Tomato Bacterial Spot
- Tomato Early Blight
- Tomato Late Blight
- Tomato Leaf Mold
- Tomato Septoria Leaf Spot
- Tomato Spider Mites (Two-Spotted Spider Mite)
- Tomato Target Spot
- Tomato Yellow Leaf Curl Virus
- Tomato Mosaic Virus
- Healthy Tomato

The dataset comprises a total of 14733 images, which are divided into training, validation, and testing sets. More detailed information about the dataset, including the distribution of images among different classes and the source of the dataset, can be found in the data description section of the project repository.

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

![CNN](https://github.com/shahriar-math1364/data-science-/blob/main/Project4/images/CNN.png)



### **Model Compilation:**
- **Optimizer**: Adam, known for its adaptive learning rate, potentially speeding up convergence.
- **Loss Function**: Sparse Categorical Crossentropy - ideal for multi-class, mutually exclusive classification.

### **Rationale:**
CNNs have excelled in image classification due to their ability to discern hierarchical spatial features in images. Starting from basic edge detectors, they proceed to understand advanced patterns. Our architecture, infused with multiple layers, aims to extract a diverse set of features from the tomato images, enhancing classification accuracy.

## Results

### Training and Validation

- The model was trained for a total of 50 epochs.
- Training accuracy reached 100%, demonstrating the model's ability to fit the training data effectively.
- Validation accuracy consistently exceeded 98%, indicating good generalization to unseen data.
- The loss function decreased progressively during training, further supporting the model's learning process.

![result](https://github.com/shahriar-math1364/data-science-/blob/main/Project4/images/epochs.png)

### Test Evaluation

- The trained model was evaluated on a separate test dataset.
- Test accuracy achieved an impressive 99.14%, demonstrating the model's ability to classify tomato images accurately.
- The test loss was computed at 0.0875, indicating minimal errors in prediction.

### Epoch-wise Performance

The model's performance was observed throughout each epoch:

- Epoch 1-10: Rapid convergence with 100% training accuracy.
- Epoch 11-20: High training and validation accuracy maintained.
- Epoch 21-30: Stable accuracy performance.
- Epoch 31-40: Continued high accuracy levels.
- Epoch 41-50: Model accuracy stabilized, indicating robust learning.

The model displayed resistance to overfitting, as evident from consistent validation and test accuracy.

These detailed results demonstrate the effectiveness of the tomato classification model, making it suitable for real-world tomato image classification tasks.


## Future Work

The Tomato Classification project is an ongoing effort, and there are several areas for future work and improvement:

1. **Fine-Tuning Hyperparameters:** Continue fine-tuning the model's hyperparameters to further enhance its performance. Experiment with different learning rates, batch sizes, and optimizer settings to optimize training.

2. **Transfer Learning:** Explore the potential of transfer learning by using pre-trained deep learning models like ResNet, Inception, or EfficientNet. Fine-tune these models on the tomato dataset for potentially better feature extraction.

3. **Data Augmentation:** Implement advanced data augmentation techniques such as CutMix, MixUp, or AutoAugment to improve model generalization and robustness, especially in handling diverse tomato conditions.

4. **Model Architectures:** Investigate alternative neural network architectures, such as convolutional neural networks (CNNs) with different depths and structures, to find the best architecture for tomato classification.

5. **Localization:** Extend the model to not only classify tomatoes but also detect and localize the regions of interest (tomatoes) within an image. This could be valuable for applications like tomato counting.

6. **Interpretability:** Implement model interpretability techniques to gain insights into why the model makes specific predictions. Tools like Grad-CAM or SHAP can help understand the model's decision-making process.


## Contributing

Contributions to the Tomato Classification project are highly encouraged and welcomed from the community. Whether you're interested in improving the model, fixing bugs, or adding new features, your contributions are valuable. Here's how you can contribute:

1. **Issue Reporting:** If you encounter any bugs, issues, or have suggestions for improvement, please open an issue on the project's GitHub repository. Provide detailed information about the problem and steps to reproduce it.

2. **Pull Requests:** If you have code changes, enhancements, or new features to contribute, fork the repository, create a new branch for your work, make your changes, and submit a pull request. Ensure that your code is well-documented and follows coding standards.

3. **Code Reviews:** Collaborate with other contributors by reviewing pull requests, providing feedback, and helping maintain code quality.

4. **Documentation:** Improve project documentation by fixing typos, clarifying instructions, or adding explanations to make it easier for users and contributors to understand and use the project.

5. **Testing:** Help ensure the stability and reliability of the project by writing and running tests for new features and bug fixes.

6. **Spread the Word:** If you find the Tomato Classification project useful, consider sharing it with others in the community who might benefit from it.

By contributing to this project, you're joining a community of developers and researchers working together to advance tomato classification technology, which has potential applications in agriculture and beyond.


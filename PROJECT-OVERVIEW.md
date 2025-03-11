# 🍎🍌 Fruit Classification using CNN & Transfer Learning 🍊🍇  

## 📌 Project Overview  
This project classifies various fruits using **Transfer Learning** with a **pre-trained MobileNetV2 CNN model**. The model leverages pre-learned features for better accuracy and efficiency.  

## 📂 Dataset  
The dataset is sourced from Kaggle:  
[🔗 Fruits Classification Dataset](https://www.kaggle.com/datasets/cheedipavankumar/fruits-classification)  

It contains labeled images of different fruit categories used for training, validation, and testing.  

## 🚀 Tech Stack  
- **Python** 🐍  
- **TensorFlow / Keras** 🤖  
- **MobileNetV2 (Pre-trained CNN)**  
- **NumPy, Pandas, Matplotlib** 📊  

## 🏗️ Model Architecture  
The model follows a **Transfer Learning** approach:  
1. **Pre-trained MobileNetV2** (excluding top layers) – Extracts high-level features  
2. **Custom Fully Connected Layers** – Adapts to fruit classification  
3. **Softmax Activation** – Predicts fruit category  

 

## ⚙️ Training & Optimization  
- **Image Preprocessing**: Resized to **128x128**, normalized  
- **Data Augmentation**: Rotation, shifting, zooming, flipping  
- **Fine-Tuning**: Last **few layers** of MobileNetV2 are trainable  
- **Regularization**: Dropout & L2 regularization  
- **Optimized with Adam (Learning Rate: 0.0005)**  
- **Callbacks**: Early Stopping, ReduceLROnPlateau, LearningRateScheduler  


### 🔹 CNN Architecture  
![CNN Model](README.md)  



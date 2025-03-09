# 🍎🍌 Fruit Classification using CNN & Transfer Learning 🍊🍇  

## 📌 Project Overview  
This project implements **Transfer Learning** to classify different types of fruits using a **pre-trained CNN model** (e.g., VGG16, ResNet, or MobileNet). The model leverages pre-learned features to improve accuracy and reduce training time.  

## 📂 Dataset  
The dataset used for this project is publicly available on Kaggle:  
[🔗 Fruits Classification Dataset](https://www.kaggle.com/datasets/cheedipavankumar/fruits-classification)  

It contains images of different fruit categories used for training and testing the CNN model.  


## 🚀 Tech Stack  
- **Python** 🐍  
- **TensorFlow / Keras** 🤖  
- **Transfer Learning (Pre-trained CNN models)**  
- **NumPy, Pandas, Matplotlib** 📊  

## 📂 Dataset  
The dataset contains images of various fruits, categorized into different classes. Each image is preprocessed and fed into the CNN model for training.  

## 🏗️ Model Architecture  
The Transfer Learning approach includes:  
1. **Pre-trained CNN Backbone** (e.g., VGG16) – Extracts high-level features  
2. **Custom Fully Connected Layers** – Adapts to fruit classification  
3. **Softmax Activation** – Predicts fruit category  

### 🔹 CNN Architecture  
![CNN Model](README.md)  

## 🏋️‍♂️ Model Training  
The model is trained using **Categorical Crossentropy Loss** and **Adam Optimizer**, with frozen pre-trained layers and fine-tuned top layers.  

```python
base_model = tf.keras.applications.VGG16(weights="imagenet", include_top=False)
base_model.trainable = False  # Freeze base model layers

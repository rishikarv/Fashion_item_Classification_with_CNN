
# 👗 Fabriq – Fashion Item Classification

**A Smarter Way to Recognize Fashion**

Fabriq is a deep learning-based Fashion Item Classification web application that identifies clothing and fashion accessories from uploaded images using a Convolutional Neural Network (CNN).

## ✨ Features

- Upload an image for fashion classification.
- Preview the uploaded image.
- Predict the fashion item's category.
- Display prediction confidence.
- Show the Top 3 predictions.
- Simple and interactive Streamlit interface.

## 🧠 Model Information

- **Model:** Convolutional Neural Network (CNN)
- **Dataset:** Fashion-MNIST
- **Framework:** TensorFlow / Keras
- **Image Size:** 28 × 28 pixels
- **Color Mode:** Grayscale
- **Number of Classes:** 10
- **Test Accuracy:** 90.47%

## 👕 Supported Categories

1. T-shirt / Top
2. Trouser
3. Pullover
4. Dress
5. Coat
6. Sandal
7. Shirt
8. Sneaker
9. Bag
10. Ankle Boot

## 🛠️ Technologies Used

- Python
- TensorFlow & Keras
- NumPy
- Pillow
- Streamlit

## 📂 Project Structure

```text
Fashion_Item_Classification/
│
├── app.py
├── fashion_cnn_model.keras
├── Fashion_item_Classification.ipynb
├── README.md
└── requirements.txt
```

## 🚀 Run Locally

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**2. Navigate to the project folder**

```bash
cd Fashion_Item_Classification
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the application**

```bash
streamlit run app.py
```

## 📊 Model Performance

The CNN model achieved approximately **90.47% test accuracy** on the Fashion-MNIST test dataset.

## 🎯 Project Objective

The objective of Fabriq is to demonstrate how deep learning and computer vision can be used to recognize and classify fashion items through an interactive web application.



**Fabriq – Making Fashion Recognition Smarter!**

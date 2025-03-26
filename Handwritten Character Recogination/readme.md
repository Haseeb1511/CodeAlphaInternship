## Dataset Link:
https://www.kaggle.com/datasets/sachinpatel21/az-handwritten-alphabets-in-csv-format

---

# ✍️ Handwritten Character Recognition (A-Z)  

This project is a **Deep Learning-based Handwritten Character Recognition system** that identifies English **alphabets (A-Z)** from images. It uses **TensorFlow/Keras** for training and is deployed as a **Streamlit Web App** with **Docker support** for easy deployment.  

---

## 🚀 Features  
✅ **Deep Learning Model** (CNN - Convolutional Neural Networks)  
✅ **Streamlit Web App** for real-time character recognition  
✅ **Image Upload Functionality**  
✅ **Dockerized Deployment for Cloud Hosting**  

---

## 📂 Dataset  
We use the **A-Z Handwritten Characters Dataset**, which consists of **28x28 grayscale images** of individual English alphabets.  

---

## 🛠 Installation  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/Haseeb1511/Handwritten-Character-Recognition.git
cd Handwritten-Character-Recognition
```

### 2️⃣ Install Dependencies  
```sh
pip install -r requirements.txt
```

---

## 🏃‍♂️ Running the Streamlit App  
```sh
streamlit run app.py
```
- The **web app** will open in your browser automatically.  
- You can **upload an image** of a handwritten letter, and the model will predict the alphabet.  

---

## 🖼 Web App Interface  
The **Streamlit app** allows users to:  
✅ Upload **handwritten character images**  
✅ Get **real-time predictions** using the trained model  
✅ View **confidence scores for predictions**  

---

## 🐳 Running with Docker  
### 1️⃣ Build the Docker Image  
```sh
docker build -t streamlit-app .
```

### 2️⃣ Run the Container Locally  
```sh
docker run -p 8501:8501 streamli-app
```

---

  

---

## 📈 Model Performance  
| Model | Accuracy |
|-------|----------|
| CNN (Convolutional Neural Network) | 98.2% |

---

## 📌 Future Improvements  
- **Improve Model Accuracy** using **Data Augmentation**  
- **Optimize Model Size** for Faster Inference  
- **Support for More Characters (Digits 0-9, Symbols)**  

---

## 📜 License  
This project is **open-source** under the **MIT License**.  

---

## 💡 Author  
**Haseeb Manzoor**  
GitHub: [Haseeb1511](https://github.com/Haseeb1511)  

---

## Mobile Price Prediction using Machine Learning  

## Project Overview  

This project aims to predict the price category of mobile phones based on various specifications such as battery power, RAM, storage, and connectivity. A **K-Nearest Neighbors (KNN)** model was trained using a dataset of mobile specifications and deployed via **Streamlit**. The application is hosted on **AWS EC2**, with the trained model stored on **S3**.  

## Features  

- **User Input**: Users can enter mobile specifications for price prediction.  
- **Machine Learning Model**: A trained **KNN** model predicts the price category.  
- **Web App Interface**: Built with **Streamlit** for a simple UI.  
- **Cloud Deployment**: Hosted on **AWS EC2** with the model stored on **S3**.  

## Tech Stack  

- **Python** (Scikit-learn, Pandas, NumPy, Joblib)  
- **Machine Learning** (K-Nearest Neighbors)  
- **Streamlit** (Web App UI)  
- **AWS** (EC2 for hosting, S3 for model storage)  

## 📂 Project Structure  

```
├── models/
│   ├── knn_model.pkl    # Trained KNN Model
│   ├── scaler.pkl       # StandardScaler object
│
├── dataset/
│   ├── mobile_data.csv  # Dataset used for training
│
├── notebooks/
│   ├── model_training.ipynb  # Jupyter Notebook for model training
│
├── app.py               # Streamlit web application
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
```

## ⚙️ Setup & Installation  

### 1️⃣ Clone the repository:  

```bash
git clone https://github.com/yourusername/mobile-price-prediction.git
cd mobile-price-prediction
```

### 2️⃣ Install dependencies:  

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the application locally:  

```bash
streamlit run app.py
```

## 🌐 Deployment on AWS EC2  

1. **Upload model files (`knn_model.pkl`, `scaler.pkl`) to an S3 bucket.**  
2. **Launch an EC2 instance** with Python & Streamlit installed.  
3. **Clone the GitHub repository** onto EC2.  
4. **Modify `app.py` to load models from S3.**  
5. **Run the Streamlit app** on EC2 and map it to a public IP.  

## 🤝 Contributing  

Feel free to fork this repo, create a feature branch, and submit a pull request!  


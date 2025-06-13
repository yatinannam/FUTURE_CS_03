# 🔐 Secure File Sharing System

This project was developed as **Task 3** of the **Future Interns Internship Program**. It is a beginner-friendly web application built using **Python Flask** that allows users to securely upload, encrypt, and download files using **AES encryption**.

## 🚀 Features
- Upload any file through the web interface
- AES encryption (CBC mode with IV)
- Decryption and secure download
- Clean and simple HTML frontend

## 🛠️ Tech Stack
- Python Flask
- PyCryptodome (AES)
- HTML & CSS (for frontend)
- dotenv (to load secure AES key)

## 🧪 How It Works
1. User uploads a file.
2. File is encrypted using AES with a unique IV.
3. Encrypted file is stored securely.
4. On download, the file is decrypted and sent to the user.

## 🔧 Setup Instructions
1. Clone the repository  
2. Install dependencies:  
   `pip install -r requirements.txt`
3. Create a `.env` file with your AES key:  
   `AES_KEY=1234567890123456`
4. Run the app:  
   `python app.py`

## 📁 Folders
- `uploads/` – for original files
- `encrypted/` – for encrypted versions
- `decrypted/` – for decrypted download temp files

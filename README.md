# Personally-Identifiable-Information-Redactor
# 🛡️ PII Redactor – AI-Powered Document Privacy Protection

An AI-powered document privacy solution that automatically detects and redacts Personally Identifiable Information (PII) from uploaded documents using a custom-trained YOLOv8 model. This project demonstrates how government portals can integrate real-time PII detection and redaction into document upload and download workflows to enhance citizen privacy and data security.

---

## ✨ Features

### 🔒 Automated PII Detection & Redaction

* Detects sensitive information from uploaded documents using a custom-trained YOLOv8 model
* Automatically masks detected PII with secure redaction blocks
* Generates a sanitized document ready for download
* Reduces the risk of accidental exposure of confidential information

### 🤖 AI-Powered Processing

* Custom-trained YOLOv8 object detection model
* Real-time document analysis and redaction
* Supports image extraction and processing from PDF documents
* High-speed inference for efficient document handling

### 📄 Document Workflow Simulation

* Demonstrates how government websites can integrate automated privacy protection
* Simulates secure document upload → AI analysis → redaction → download workflow
* Can be extended and integrated into existing government and enterprise portals

### 🎨 User-Friendly Interface

* Simple drag-and-drop file upload
* One-click document processing
* Downloadable redacted PDF output
* Responsive and easy-to-use web interface

---

## 🧠 Machine Learning Integration

* YOLOv8 custom-trained model for PII detection
* Computer Vision-based document analysis
* Bounding-box localization of sensitive information
* Automated redaction pipeline using OpenCV and image processing techniques

---

## 🧩 Technical Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### AI & Computer Vision

* YOLOv8 (Ultralytics)
* OpenCV
* Pillow (PIL)

### PDF Processing

* PyMuPDF (fitz)

### Data Handling

* NumPy

---

## 📋 Requirements

### Python Dependencies

* Flask
* ultralytics
* opencv-python
* pymupdf
* pillow
* numpy

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <repository-url>
cd pii-redactor
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

## 🔄 Workflow

1. User uploads a PDF document
2. Images are extracted from the document
3. YOLOv8 model scans for sensitive information
4. Detected PII is automatically redacted
5. A secure, redacted PDF is generated
6. User downloads the protected document

---

## 🎯 Use Cases

* Government document portals
* Citizen service platforms
* Digital document management systems
* Privacy-preserving document sharing
* Compliance and data protection workflows

---

## 🔮 Future Enhancements

* OCR-based text detection and redaction
* Aadhaar, PAN, Driving License, and Passport recognition
* Secure metadata removal
* Audit logging and compliance reporting
* Batch document processing
* Explainable AI visualizations
* Cloud deployment and API integration

---

## 👥 Team

**Proton Riders**
Smart India Hackathon Project

Built to enhance document privacy and support secure digital governance through AI-powered PII protection.

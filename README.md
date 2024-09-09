# 🔐 PII Detection and Document Analyzer

A comprehensive tool for detecting Personally Identifiable Information (PII) from documents such as Aadhaar cards, PAN cards, and driving licenses. This project uses OCR and NER (Natural Entity Recognition) to extract key details and display them on an enhanced dashboard. 🖥️

## Features ✨

- 🔍 **OCR (Optical Character Recognition)**: Extracts text from images of documents.
- 🧠 **NER (Named Entity Recognition)**: Identifies key entities like Name, Address, and Date of Birth.
- 🔢 **Aadhaar, PAN, and Driving License Detection**: Automatically identifies and validates Aadhaar, PAN, and driving license numbers using regex.
- 📸 **Photo and Signature Extraction**: Detects and displays the cardholder's photo and signature from the document.
- 📱 **QR Code Detection**: Scans and displays any data encoded in the document's QR code.
- 🖼️ **Enhanced Dashboard**: Presents all extracted information in a user-friendly format, including highlighted PII.

## Prerequisites ⚙️

Before running the project, ensure you have the following installed:

- 🐍 [Python 3.8+](https://www.python.org/downloads/)
- 📦 Required Python Libraries:
    - `pytesseract`
    - `opencv-python`
    - `Pillow`
    - `flask`
    - `spacy`

### Installing Python Libraries 📥

Use the following commands to install the required dependencies:

```bash
pip install pytesseract opencv-python Pillow flask spacy
python -m spacy download en_core_web_sm
```

Also, make sure you have [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed on your system.

## Setup and Usage 🚀

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repository/PII-Detect.git
   cd PII-Detect
   ```

2. **Run the Flask app**:
   ```bash
   python app.py
   ```

3. **Open your browser** and visit:
   ```
   http://127.0.0.1:5000
   ```

4. **Upload a Document** (e.g., Aadhaar, PAN card). The tool will extract relevant details and display them on the dashboard.

## How It Works 🛠️

1. **Text Extraction**: The uploaded image is processed using OCR to extract all visible text.
2. **Entity Detection**: We use spaCy’s NER model to detect entities such as names, addresses, and dates.
3. **Identifier Detection**: Regex patterns are used to detect specific identifiers like Aadhaar, PAN, and driving license numbers.
4. **Image Processing**: The photo and signature are extracted and displayed separately on the dashboard.
5. **QR Code Decoding**: If the document contains a QR code, it is scanned, and the data is shown on the dashboard.

## Dashboard Overview 📊

Once the document is uploaded, the following details are displayed on the dashboard:

- **Extracted Text**: The raw text obtained via OCR.
- **Identifiers**: Aadhaar, PAN, and driving license numbers.
- **Extracted Entities**: Important information like names, addresses, and dates.
- **QR Code Data**: Decoded data from any QR codes present.
- **Photo and Signature**: Displays the cardholder's photo and signature.

## Screenshots 📸

Here’s a preview of the enhanced dashboard:

![Dashboard Preview](https://via.placeholder.com/600x400)

## Troubleshooting 🛠️

- **Tesseract not found**: Make sure Tesseract is installed and properly added to your system path.
- **Incorrect Data Extraction**: The quality of OCR depends on the clarity of the image. Ensure that the uploaded document is clear and well-lit.

## Contributing 🤝

We welcome contributions to enhance the tool! Feel free to submit pull requests or raise issues for any bugs or features you'd like to see.

## License 📜

This project is licensed under the MIT License.

from flask import Flask, request, render_template, redirect, url_for
import os
from ocr import extract_text
from entity_recognition import extract_entities
from regex_detection import detect_identifiers
from qr_code import decode_qr_code

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Save uploaded file
        file = request.files['file']
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Process file (OCR, NER, QR Code, etc.)
        extracted_text = extract_text(file_path)
        entities = extract_entities(extracted_text)
        identifiers = detect_identifiers(extracted_text)
        qr_data = decode_qr_code(file_path)

        # Render the dashboard with extracted information
        return render_template('dashboard.html',
                               extracted_text=extracted_text,
                               entities=entities,
                               identifiers=identifiers,
                               qr_data=qr_data,
                               file_path=file_path)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)



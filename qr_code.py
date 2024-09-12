import cv2
from pyzbar.pyzbar import decode

def decode_qr_code(image_path):
    # Load the image
    img = cv2.imread(image_path)
    
    # Decode any QR codes found in the image
    qr_codes = decode(img)
    
    qr_data = []
    for qr_code in qr_codes:
        qr_data.append(qr_code.data.decode('utf-8'))

    return qr_data


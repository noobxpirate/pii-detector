import re

def detect_identifiers(text):
    aadhaar_pattern = r'\d{4} \d{4} \d{4}'  # Example Aadhaar pattern
    pan_pattern = r'[A-Z]{5}\d{4}[A-Z]{1}'  # Example PAN pattern
    dl_pattern = r'[A-Z]{2}\d{2} \d{4} \d{7}'  # Example DL pattern

    aadhaar = re.findall(aadhaar_pattern, text)
    pan = re.findall(pan_pattern, text)
    dl = re.findall(dl_pattern, text)

    return {
        'aadhaar': aadhaar,
        'pan': pan,
        'driving_license': dl
    }


# backend/chatpdf/utils/pdf_utils.py

import PyPDF2

def read_pdf(file_path):
    with open(file_path, 'rb') as f:
        # truy cập từng trang
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
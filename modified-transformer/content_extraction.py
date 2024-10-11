import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

# Example usage


pdf_path = r"C:\Users\TUF\OneDrive\Desktop\projects\Steps AI\from scratch\21 Lessons for the 21st Century ( PDFDrive ).pdf"
extracted_text = extract_text_from_pdf(pdf_path)
print(f"Extracted {len(extracted_text)} characters")
import pypdf  # Import pypdf (formerly PyPDF2)

def save_uploaded_file(uploaded_file):
    """
    Save the uploaded PDF to a temporary file.
    """
    file_path = f"temp/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = pypdf.PdfReader(file)  # Create PDF reader object
        text = ""
        for page_num in range(len(reader.pages)):  
            page = reader.pages[page_num]
            text += page.extract_text()  
    return text

def chunk_text(text, chunk_size=500):
    
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])
    return chunks

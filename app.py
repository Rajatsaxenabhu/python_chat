import streamlit as st
from pdf_utils import extract_text_from_pdf, chunk_text, save_uploaded_file
from embedding_utils import create_faiss_index, get_answer, get_embedding
import config

# Streamlit UI
st.title("PDF Search App")

# Sidebar for PDF Upload and Selection
with st.sidebar:
    # Upload multiple PDFs
    pdf_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

    # Allow the user to select which PDFs to use for embedding
    selected_pdfs = st.multiselect("Select PDFs to use for embedding", options=pdf_files, format_func=lambda x: x.name)

# Check if PDFs are uploaded
if pdf_files:
    # Store the extracted text and corresponding embeddings for each PDF
    pdf_texts = {}
    text_chunks_dict = {}
    embeddings_dict = {}
   

    # Process each uploaded PDF
    for pdf_file in pdf_files:
        temp_pdf_path = st.file_uploader(pdf_file)  # Save uploaded PDF to a temporary path
        pdf_text = extract_text_from_pdf(temp_pdf_path)  # Extract text from PDF
        text_chunks = chunk_text(pdf_text)  # Split the text into manageable chunks
        print("phase 111")
        
        # Get embeddings for each chunk
        embeddings = get_embedding(text_chunks)  # Generate embeddings for text chunks
        print("embedding end")
        # Store results in dictionaries for later use
        pdf_texts[pdf_file.name] = pdf_text
        text_chunks_dict[pdf_file.name] = text_chunks
        embeddings_dict[pdf_file.name] = embeddings
        print("phase 221")
    
    st.sidebar.write("PDF texts extracted and embeddings created.")

    # User query input in main area
    query = st.text_input("Enter your query:")

    # Check if selected PDFs exist
    if selected_pdfs:
        print("phase2")
        # Create FAISS indexes for each selected PDF
        faiss_indexes = {}
        for selected_pdf in selected_pdfs:
            faiss_index = create_faiss_index(embeddings_dict[selected_pdf.name])  # Generate FAISS index for selected PDFs
            faiss_indexes[selected_pdf.name] = faiss_index
        
        # Query handling
        if query:
            # Process the query across selected PDFs
            answers = {}
            for selected_pdf in selected_pdfs:
                faiss_index = faiss_indexes[selected_pdf.name]
                answer = get_answer(query, faiss_index, text_chunks_dict[selected_pdf.name])  # Retrieve answer from FAISS
                answers[selected_pdf.name] = answer

            # Display the answers from the selected PDFs
            for pdf_name, answer in answers.items():
                st.subheader(f"Answer from {pdf_name}:")
                st.write(answer)

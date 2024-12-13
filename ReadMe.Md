# QA ChatApp with PDF Upload and Embedding Search Using FAISS

This application allows users to upload multiple PDF files, extract their content, generate embeddings using Sentence-Transformers, and store those embeddings in a FAISS vector database. Users can then query the system with their questions, and the app will return the most relevant content from the uploaded PDFs based on the similarity to the query's embedding using FAISS for efficient similarity search.

---

## Features

- **PDF Upload**:  
  - Upload multiple PDF files to the app for processing.
  
- **Text Extraction**:  
  - Extracts text content from PDFs using the **PyPDF2** library.
  
- **Embedding Generation**:  
  - Converts the extracted text into embeddings using **Sentence-Transformers**.

- **FAISS Vector Database**:  
  - Stores and queries embeddings efficiently with **FAISS** for fast similarity search.
  
- **Query Processing**:  
  - Users can enter queries, and the app will return the most relevant content from the uploaded PDFs based on the similarity between the query and the document embeddings.

- **Real-Time Interaction**:  
  - Built using **Streamlit**, offering a user-friendly, interactive interface for seamless use.

---

## Technologies Used

- **Streamlit**: For creating the interactive web interface.
- **Sentence-Transformers**: For generating sentence embeddings that are used to compare query input with PDF content.
- **PyPDF2**: For extracting text from PDF files.
- **FAISS**: A library used to store embeddings in a vector database and perform efficient similarity search.
- **Python 3.x**: The programming language used for the backend and execution of models.

---

## Installation

Follow the steps below to set up and run the app locally:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Rajatsaxenabhu/python_chat.git
   ```
2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app**:

   ```bash
   streamlit run app.py
   ```

---
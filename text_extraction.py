import PyPDF2
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from sentence_transformers import SentenceTransformer

nltk.download('punkt')

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def chunk_text(text, chunk_size=100):
    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = []
    current_length = 0

    for sentence in sentences:
        sentence_tokens = word_tokenize(sentence)
        if current_length + len(sentence_tokens) > chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = sentence_tokens
            current_length = len(sentence_tokens)
        else:
            current_chunk.extend(sentence_tokens)
            current_length += len(sentence_tokens)

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

def embed_chunks(chunks):
    embeddings = model.encode(chunks)
    return embeddings

# Load the SBERT model
model = SentenceTransformer('all-MiniLM-L6-v2')


pdf_path1 = '/content/21 Lessons for the 21st Century ( PDFDrive ).pdf'
pdf_path2 = '/content/Homo Deus_ A Brief History of Tomorrow ( PDFDrive ).pdf'
pdf_path3 = '/content/Sapiens_ A Brief History of Humankind ( PDFDrive ).pdf'

text1 = extract_text_from_pdf(pdf_path1)
text2 = extract_text_from_pdf(pdf_path2)
text3 = extract_text_from_pdf(pdf_path3)
all_texts = text1 + text2 + text3

# Print the extracted text (entire books)
# print("Text from textbook 1:")
# print(text1)
# print("\nText from textbook 2:")
# print(text2[:1000])
# print("\nText from textbook 3:")
# print(text3[:1000])

chunks1 = chunk_text(text1)
chunks2 = chunk_text(text2)
chunks3 = chunk_text(text3)

embeddings1 = embed_chunks(chunks1)
embeddings2 = embed_chunks(chunks2)
embeddings3 = embed_chunks(chunks3)

print(embeddings1.shape)
print(embeddings2.shape)
print(embeddings3.shape)
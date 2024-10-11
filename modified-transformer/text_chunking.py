from content_extraction import extracted_text

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt')

def chunk_text(extracted_text, chunk_size=100):
    sentences = sent_tokenize(extracted_text)
    chunks = []
    current_chunk = ""
    
    for sentence in sentences:
        words = word_tokenize(sentence)
        if len(current_chunk.split()) + len(words) <= chunk_size:
            current_chunk += " " + sentence
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks

# Example usage
chunks = chunk_text(extracted_text)
print(f"Created {len(chunks)} chunks")
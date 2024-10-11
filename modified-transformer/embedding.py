from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_chunks(chunks):
    return model.encode(chunks)

# Example usage
embeddings = embed_chunks(chunks)
print(f"Created {len(embeddings)} embeddings of dimension {len(embeddings[0])}")



# from transformers import AutoTokenizer, AutoModel
# import torch
#
# # Load a pre-trained model and tokenizer
# tokenizer = AutoTokenizer.from_pretrained("distilbert-base-nli-stsb-mean-tokens")
# model = AutoModel.from_pretrained("distilbert-base-nli-stsb-mean-tokens")
#
#
# def embed_text(text):
#     # Tokenize the input text
#     inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
#
#     # Get model outputs
#     with torch.no_grad():
#         outputs = model(**inputs)
#
#     # Use the mean of the last hidden states as embeddings
#     embeddings = outputs.last_hidden_state.mean(dim=1)
#     return embeddings
#
#
# # Example usage
# text = "This is a test sentence."
# embedding = embed_text(text)
# print(embedding.shape)  # Should print (1, 768)

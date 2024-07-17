# milvus-raptor-indexing-RAG

The complete table including the practical tools, frameworks, libraries, and models mentioned in the Project:


| Category                 | Tools/Frameworks/Libraries/Models    | Usage                                        | Documentation/Resource Link |
|--------------------------|--------------------------------------|----------------------------------------------|-----------------------------|
| Programming Language     | Python                               | Main programming language                    | N/A                         |
| Content Extraction       | PyPDF2                               | Extracting text from PDF files               | [PyPDF2 Documentation](https://pypdf2.readthedocs.io/en/latest/) |
|                          | pdfplumber                           | Advanced PDF text extraction                 | [pdfplumber Documentation](https://github.com/jsvine/pdfplumber) |
|                          | PyPDF                                | Extracting text from PDF documents           | [PyPDF Documentation](https://github.com/mstamy2/PyPDF2) |
| Text Processing          | NLTK                                 | Natural Language Toolkit for text processing | [NLTK Documentation](https://www.nltk.org/) |
|                          | Gensim                               | Topic modeling and document similarity       | [Gensim Documentation](https://radimrehurek.com/gensim/) |
| Embedding Models         | SBERT                                | Sentence-BERT for generating vector embeddings| [Sentence-Transformers Documentation](https://www.sbert.net/) |
|                          | BERT                                 | Pre-trained transformer model for natural language understanding tasks | [BERT Paper](https://arxiv.org/abs/1810.04805) |
| Vector Database          | MILVUS with RAPTOR indexing          | Vector storage and indexing                  | [MILVUS Documentation](https://milvus.io/docs/) |
| Clustering               | Scikit-learn                         | Gaussian Mixture Models for clustering       | [Sklearn GMM Documentation](https://scikit-learn.org/stable/modules/mixture.html) |
| Language Models          | GPT-3.5-turbo                        | Summarization                                | [OpenAI GPT-3.5 Documentation](https://beta.openai.com/docs/) |
|                          | An LLM of your choice (e.g., GPT-3.5, GPT-4, or an open-source alternative) | Question answering                          | [OpenAI GPT-3.5 Documentation](https://beta.openai.com/docs/) |
| Retrieval Techniques     | Pyserini                             | BM25 retrieval                               | [Pyserini Documentation](https://pyserini.io/) |
|                          | Sentence-Transformers                | Bi-encoder retrieval                         | [Sentence-Transformers Documentation](https://www.sbert.net/) |
|                          | Implement SPIDER (if chosen)         | Semantic Passage Retrieval                   | [SPIDER Paper](https://arxiv.org/abs/2006.06031) |
| User Interface (optional)| Streamlit or Gradio                  | Creating a user interface                    | [Streamlit Documentation](https://docs.streamlit.io/), [Gradio Documentation](https://www.gradio.app/) |
| Version Control          | Git and GitHub                       | Version control and code submission          | N/A                         |




## Detailed breakdown of the topics and subtopics you should focus on:

1. Natural Language Processing (NLP) basics
    - What is NLP?
    - Text preprocessing techniques:
        - Tokenization
        - Lowercasing
        - Removing punctuation and special characters
        - Stopword removal
        - Stemming and lemmatization


    - Part-of-speech tagging
    - Named Entity Recognition (NER)
    - Syntactic parsing


2. Vector representations of text (embeddings)
    - Concept of word embeddings
    - One-hot encoding
    - Word2Vec
    - GloVe (Global Vectors for Word Representation)
    - FastText
    - Sentence embeddings (e.g., SBERT)


3. Information Retrieval techniques
     - Boolean retrieval
     - TF-IDF (Term Frequency-Inverse Document Frequency)
     - Vector Space Model
     - BM25 (Best Matching 25)
     - Semantic search basics


4. Clustering algorithms, particularly Gaussian Mixture Models (GMMs)
     - Introduction to clustering
     - K-means clustering
     - Hierarchical clustering
     - Gaussian Mixture Models:
         - Probability distributions
         - Expectation-Maximization (EM) algorithm
         - Soft clustering concept




5. Hierarchical data structures (tree structures)
   - Basic tree concepts
   - Binary trees
   - N-ary trees
   - Tree traversal algorithms
   - Recursive algorithms on trees


6. Query expansion techniques
   - Synonyms and antonyms
   - Stemming and lemmatization in query expansion
   - WordNet for query expansion
   - Relevance feedback methods


7. Ranking and re-ranking algorithms
   - Relevance scoring
   - PageRank algorithm (conceptual understanding)
   - Learning to Rank (basic concept)
   - Re-ranking using machine learning


8. Language Model fundamentals
   - N-gram language models
   - Neural language models: basic concepts
   - Transformer architecture: high-level understanding
   - Transfer learning in NLP
   - Fine-tuning vs. few-shot learning


## Modules for problem statement and the relevant technologies, frameworks, language modules, libraries, and databases for each module.

1. Content Extraction Module
   - Language: Python
   - Libraries: PyPDF2 or pdfminer.six
   - Purpose: Extract text from PDF textbooks

2. Text Preprocessing and Chunking Module
   - Language: Python
   - Libraries: NLTK, spaCy
   - Purpose: Clean and chunk text into 100-token segments

3. Embedding Generation Module
   - Language: Python
   - Framework: Sentence-Transformers
   - Model: SBERT (e.g., 'all-MiniLM-L6-v2')
   - Purpose: Generate vector representations of text chunks

4. RAPTOR Indexing Module
   - Language: Python
   - Libraries: scikit-learn (for GMM), NumPy
   - Framework: Transformers (for summarization with GPT-3.5-turbo)
   - Purpose: Implement hierarchical clustering and summarization

5. Vector Database Module
   - Language: Python
   - Database: Milvus
   - Library: pymilvus
   - Purpose: Store and manage vector data and metadata

6. Query Processing Module
   - Language: Python
   - Libraries: NLTK (for query expansion), Pyserini (for BM25)
   - Purpose: Process and expand user queries

7. Retrieval Module
   - Language: Python
   - Libraries: Pyserini (for BM25), Faiss (for approximate nearest neighbor search)
   - Database: Milvus
   - Purpose: Implement hybrid retrieval (BM25 + vector similarity)

8. Re-ranking Module
   - Language: Python
   - Libraries: scikit-learn or LightGBM (for learning-to-rank)
   - Purpose: Re-rank retrieved results

9. Question Answering Module
   - Language: Python
   - Framework: Transformers
   - Model: An LLM of your choice (e.g., GPT-3.5, GPT-4, or an open-source alternative)
   - Purpose: Generate answers based on retrieved context

10. User Interface Module (Optional)
    - Language: Python
    - Framework: Streamlit or Gradio
    - Purpose: Provide a user-friendly interface for querying the system

Additional components:

11. Main Application Logic
    - Language: Python
    - Purpose: Orchestrate the flow between different modules

12. Configuration Management
    - Language: Python
    - Library: configparser or PyYAML
    - Purpose: Manage application settings

13. Logging and Monitoring
    - Language: Python
    - Library: logging
    - Purpose: Track application events and performance

14. Testing
    - Language: Python
    - Framework: pytest
    - Purpose: Ensure reliability and correctness of the implementation

Overall project management:
- Version Control: Git
- Dependency Management: pip, virtualenv or conda
- Documentation: Markdown, Sphinx

---
## Flow/pipeline of the project

### Project Pipeline:

1. Content Ingestion
   → Content Extraction Module
     - Load PDF textbooks
     - Extract text content

2. Text Processing
   → Text Preprocessing and Chunking Module
     - Clean and preprocess the extracted text
     - Chunk text into 100-token segments

3. Embedding Generation
   → Embedding Generation Module
     - Generate vector embeddings for each text chunk using SBERT

4. RAPTOR Index Creation
   → RAPTOR Indexing Module
     - Perform hierarchical clustering using GMM
     - Summarize clusters using GPT-3.5-turbo
     - Create tree structure

5. Vector Storage
   → Vector Database Module
     - Store embeddings, summaries, and metadata in Milvus

6. Query Processing
   → Query Processing Module
     - Receive user query
     - Expand query (synonyms, etc.)

7. Retrieval
   → Retrieval Module
     - Perform hybrid retrieval:
       a) BM25 search
       b) Vector similarity search
     - Combine results

8. Re-ranking
   → Re-ranking Module
     - Re-rank retrieved results based on relevance

9. Answer Generation
   → Question Answering Module
     - Use LLM to generate answer based on re-ranked retrieved context

10. Result Presentation
    → User Interface Module
      - Display answer and relevant metadata to user

### Flow of Operations:

1. Offline Processing (Done once during setup):
   Content Ingestion → Text Processing → Embedding Generation → RAPTOR Index Creation → Vector Storage

2. Online Query Processing (Done for each user query):
   Query Processing → Retrieval → Re-ranking → Answer Generation → Result Presentation

Additional Continuous Processes:
- Logging and Monitoring: Track system performance and errors throughout the pipeline
- Configuration Management: Provide settings for each module
- Testing: Ensure each component and the overall system functions correctly

This pipeline ensures that:
1. The textbooks are properly processed and indexed, creating a rich knowledge base.
2. User queries are effectively expanded and used to retrieve relevant information.
3. The retrieved information is refined through re-ranking to improve relevance.
4. The final answer is generated considering the most pertinent information.

The modular nature of this pipeline allows for:
- Parallel processing where possible (e.g., processing multiple books simultaneously)
- Easy updates or replacements of individual components (e.g., switching to a different LLM)
- Scalability, as you can optimize each component independently

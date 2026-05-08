# RAG-Based Video Q&A Assistant with Timestamp Retrieval

## Problem

Searching for specific concepts in long lecture videos is slow and inefficient. Traditional keyword search fails to capture context, forcing users to manually search through hours of content.

---

## Solution

Built an end-to-end Retrieval-Augmented Generation (RAG) system that enables users to ask natural language questions and directly navigate to the exact video timestamp where the answer is discussed.

---

## System Architecture

Video → Audio Extraction → Whisper Transcription → Text Chunking → Embedding Generation → Similarity Retrieval → LLM Response → Timestamp Output

---

## Tech Stack

* Whisper (large-v2)
* bge-m3 embeddings via Ollama
* Llama 3.2 via Ollama
* Python
* NumPy, Pandas, Scikit-learn
* Cosine similarity retrieval

---

## Key Features

* Semantic search over lecture videos
* Timestamp-level navigation
* Context-aware retrieval
* Reduced hallucination using grounded transcript chunks
* Automated batch video processing

---

## Results

* Reduced search time from minutes to seconds
* Indexed 10+ hours of lecture videos
* Accurate timestamp-based navigation
* Enabled semantic retrieval over transcript chunks

---



## Future Improvements

* Integrate FAISS / Milvus for scalable vector search
* Add Streamlit or Flask UI
* Support real-time video ingestion

---

## Repository Structure

```text
rag-video-qa-assistant/
│
├── README.md
├── requirements.txt
│
├── src/
│   ├── mp3_to_json.py
│   ├── preprocess_json.py
│   ├── process_incoming.py
│   └── video_to_mp3.py
│
└── sample_output/
    └── example.txt
```

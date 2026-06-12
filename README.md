# 📡 TelecomIQ: AI-Powered Telecom Support Intelligence Platform

> Transforming telecom customer support with Retrieval-Augmented Generation (RAG), semantic search, and historical ticket intelligence.

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)]()
[![LangChain](https://img.shields.io/badge/LangChain-RAG-green.svg)]()
[![ChromaDB](https://img.shields.io/badge/VectorDB-Chroma-orange.svg)]()
[![Groq](https://img.shields.io/badge/LLM-Qwen3--32B-red.svg)]()
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-ff4b4b.svg)]()


## 🚀 Live Demo

Try the deployed app here:

👉 [Click to open Streamlit App](https://telecomchatbot-2nfrvyb6blwobyke9aheih.streamlit.app/)

## 🎥 Video Demo

[![Watch the Demo](https://img.youtube.com/vi/8SRbZjVIOFQ/maxresdefault.jpg)](https://youtu.be/8SRbZjVIOFQ)


## 🚀 The Problem

Telecom support teams manage information scattered across:

- 📖 FAQ repositories
- 📄 Technical documentation
- 🎫 Historical support tickets

Finding the right answer often requires manually searching multiple systems, resulting in:

- Long resolution times
- Repeated customer interactions
- Inconsistent support quality
- Knowledge silos across teams

---

## 💡 The Solution

**TelecomIQ** acts as an intelligent support copilot that unifies organizational knowledge into a single searchable AI system.

Instead of relying on generic LLM responses, TelecomIQ:

✅ Retrieves answers from official FAQs

✅ Searches technical telecom documentation

✅ Learns from previously resolved support tickets

✅ Generates source-grounded responses

✅ Provides transparent citations for every answer

---

## ✨ Innovation Highlights

### 🧠 Multi-Knowledge RAG Engine

Unlike traditional chatbots that rely on a single knowledge source, TelecomIQ simultaneously retrieves information from:

| Knowledge Source | Purpose |
|------------------|----------|
| FAQ Database | Policies, plans, procedures |
| Telecom Guide | Technical documentation |
| Ticket Database | Real-world resolutions |

This creates a richer context and significantly improves answer quality.

---

### 🎫 Ticket Intelligence Layer

Historical support tickets are transformed into a searchable knowledge base.

The system can identify how similar issues were resolved previously and surface proven troubleshooting steps.

---

### 📚 Explainable AI Responses

Every answer includes its source:

- FAQ references
- Ticket references
- Guide references

This improves trust and reduces hallucinations.

---

### ⚡ Real-Time Semantic Search

Using sentence-transformer embeddings and ChromaDB, TelecomIQ understands intent rather than relying on keyword matching.

Examples:

**User Query**
> My SIM stopped working after restarting my phone.

The system can retrieve:

- SIM activation FAQs
- Device troubleshooting guides
- Similar resolved tickets

even if those exact words never appear.

---

## 🏗️ System Architecture

```text
                    User Query
                         │
                         ▼
              Semantic Embedding Model
                         │
                         ▼
          ┌─────────────────────────┐
          │      ChromaDB           │
          └─────────────────────────┘
               │       │       │
               ▼       ▼       ▼
            FAQ    Tickets   Guides
               │       │       │
               └───┬───┴───┬───┘
                   ▼
           Context Aggregation
                   ▼
             Prompt Builder
                   ▼
         Qwen3-32B via Groq
                   ▼
        Source-Grounded Answer
```

---

## 🌟 Key Capabilities

| Capability | Description |
|------------|------------|
| Multi-Source Retrieval | Searches FAQ, Guide, and Ticket collections simultaneously |
| Semantic Search | Finds relevant content beyond keyword matching |
| Ticket Intelligence | Leverages historical issue-resolution data |
| Source Attribution | Provides transparent references |
| Streaming Responses | Real-time answer generation |
| Conversational UI | User-friendly Streamlit interface |
| Modular Ingestion Pipeline | Easily update FAQs, PDFs, and tickets |

---

## 🚧 Challenges Solved

### Multi-Source Retrieval
Combining FAQ, ticket, and documentation results into a single context.

### Source Attribution
Ensuring responses always reference their origin.

### Context Management
Balancing retrieval quality while keeping prompts concise.

### PDF Chunking
Selecting chunk size and overlap to preserve context.


## ▶️ Running the Application

### 1. Install Dependencies

```bash

pip install -r requirements.txt

```

### 2. Build the Knowledge Base

```bash

python ingest_faq.py

python ingest_pdf.py

python ingest_tickets.py

```

### 3. Launch the Chat Interface

```bash

streamlit run app.py

```

---



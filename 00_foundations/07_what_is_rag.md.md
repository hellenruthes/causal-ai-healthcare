# What is Retrieval-Augmented Generation (RAG)?

## Introduction

Large Language Models generate responses based on information learned during training.

However, they do not automatically know information that:

- Was created after training
    
- Exists only inside an organization
    
- Is stored in private documents
    

Retrieval-Augmented Generation (RAG) addresses this limitation by providing external information to the model at runtime.

---

## The Problem

Without RAG:

```text
Question
 ↓
LLM
 ↓
Answer
```

The model relies only on its training data.

---

## The RAG Approach

With RAG:

```text
Question
 ↓
Search
 ↓
Relevant Documents
 ↓
LLM
 ↓
Answer
```

The model receives additional context before generating a response.

---

## Example

Question:

```text
What is our organization's vacation policy?
```

A general-purpose LLM does not know the answer.

A RAG system can:

1. Search internal documents.
    
2. Retrieve the policy.
    
3. Provide the policy as context.
    
4. Generate an answer based on that information.
    

---

## Components of a RAG System

Typical RAG systems contain:

- Documents
    
- Embeddings
    
- Vector Database
    
- Retriever
    
- Language Model
    

---

## Why RAG Matters

RAG allows organizations to:

- Use private data
    
- Reduce hallucinations
    
- Improve accuracy
    
- Access current information
    
- Build domain-specific assistants
    

---

## Healthcare Applications

Healthcare RAG systems can support:

- Clinical guidelines
    
- Research articles
    
- Institutional policies
    
- Treatment protocols
    
- Electronic health records
    

---

## Key Takeaway

RAG combines information retrieval with language generation, allowing AI systems to answer questions using external knowledge rather than relying exclusively on model training data.
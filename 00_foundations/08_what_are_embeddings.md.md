# What Are Embeddings?

## Introduction

Embeddings are numerical representations of information.

In Artificial Intelligence, text, images, audio, or other types of data can be transformed into vectors: lists of numbers that represent meaning in a format computers can process.

Embeddings allow AI systems to compare information based on semantic similarity rather than exact word matching.

They are one of the foundational technologies behind modern search systems, recommendation engines, and Retrieval-Augmented Generation (RAG) applications.

---

## Simple Example

The following sentences use different words but have very similar meanings:

```text
The patient has high blood pressure.

The patient was diagnosed with hypertension.
```

A traditional keyword search may treat these sentences as unrelated because they contain different words.

An embedding-based system can recognize that they express a similar concept.

---

## How Embeddings Work

An embedding model converts information into a vector.

```text
Text
 ↓
Embedding Model
 ↓
Vector
```

Example:

```text
"The patient has diabetes."

↓

[0.23, -0.45, 0.91, 0.14, ...]
```

The numbers themselves are not meaningful to humans.

What matters is the relationship between vectors.

---

## Similarity

Embeddings allow systems to measure similarity between pieces of information.

Example:

```text
"The patient has diabetes."

"The patient suffers from type 2 diabetes."

"The patient uses insulin."
```

The generated vectors will likely be located close together in vector space because they represent related concepts.

Meanwhile:

```text
"How to repair a bicycle tire"
```

would likely be located far away because it belongs to a completely different topic.

---

## Semantic Search

Traditional search relies on matching words.

Embedding-based search relies on matching meaning.

Example:

Query:

```text
heart attack treatment
```

May retrieve documents containing:

```text
myocardial infarction

cardiac emergency

acute coronary syndrome
```

even if the phrase "heart attack treatment" does not appear in the document.

This capability is known as semantic search.

---

## Embeddings in Healthcare

Healthcare systems contain large amounts of unstructured text.

Examples include:

- Clinical notes
    
- Progress notes
    
- Discharge summaries
    
- Research articles
    
- Treatment guidelines
    

Embeddings can help identify related information across these documents.

Applications include:

- Clinical search
    
- Similar patient retrieval
    
- Literature review
    
- Research support
    
- Medical question answering
    

---

## Embeddings and RAG

Retrieval-Augmented Generation (RAG) systems frequently use embeddings.

The process typically follows:

```text
Question
 ↓
Embedding
 ↓
Vector Search
 ↓
Relevant Documents
 ↓
LLM
 ↓
Answer
```

The embedding enables the system to retrieve documents that are semantically related to the user's question.

---

## Common Embedding Models

Examples include:

- OpenAI Embeddings
    
- Gemini Embeddings
    
- Cohere Embeddings
    
- BGE Models
    
- E5 Models
    
- Instructor Models
    

Different models may perform better depending on the domain and language.

---

## Limitations

Embeddings represent similarity, not truth.

Two documents may appear similar while containing contradictory information.

Embeddings also do not establish:

- Correctness
    
- Clinical validity
    
- Causality
    

Human validation remains essential, particularly in healthcare applications.

---

## Key Takeaway

Embeddings transform information into numerical vectors that capture semantic meaning.

They enable AI systems to perform semantic search, retrieve relevant information, and support modern applications such as RAG, recommendation systems, and knowledge discovery.
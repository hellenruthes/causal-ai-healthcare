# What Are Vector Databases?

## Introduction

Vector databases are specialized systems designed to store, manage, and search embeddings efficiently.

As discussed in the previous chapter, embeddings transform information such as text, images, and documents into numerical vectors that capture semantic meaning.

Once information has been converted into vectors, a mechanism is needed to store and retrieve those vectors quickly. This is the role of a vector database.

Vector databases have become a fundamental component of modern Artificial Intelligence applications, particularly Retrieval-Augmented Generation (RAG) systems.

---

## Why Vector Databases Exist

Consider an organization with:

- 10,000 documents
    
- 100,000 clinical notes
    
- 1 million research articles
    

If each document is converted into an embedding, the result is a large collection of vectors.

Searching through every vector manually would be computationally expensive.

Vector databases are optimized to efficiently identify the vectors that are most similar to a query.

---

## Traditional Databases vs Vector Databases

Traditional databases are designed to store structured information.

Examples:

|ID|Name|Diagnosis|
|---|---|---|
|1|John|Diabetes|
|2|Mary|Hypertension|

Queries typically rely on exact matches.

Example:

```sql
SELECT *
FROM patients
WHERE diagnosis = 'Diabetes'
```

---

Vector databases operate differently.

Instead of searching for exact values, they search for semantic similarity.

Example:

Query:

```text
Patient with elevated blood sugar
```

May retrieve documents discussing:

- Diabetes
    
- Hyperglycemia
    
- Type 2 Diabetes
    
- Glucose management
    

even if those exact words were not used in the query.

---

## How Vector Search Works

The process generally follows these steps:

### Step 1: Create Embeddings

Documents are converted into vectors.

```text
Document
 ↓
Embedding Model
 ↓
Vector
```

---

### Step 2: Store Vectors

Vectors are stored inside a vector database.

```text
Vector
 ↓
Vector Database
```

---

### Step 3: Convert the Query

A user question is also transformed into an embedding.

```text
Question
 ↓
Embedding Model
 ↓
Query Vector
```

---

### Step 4: Similarity Search

The database identifies vectors that are closest to the query vector.

```text
Query Vector
 ↓
Vector Search
 ↓
Most Similar Documents
```

---

### Step 5: Return Results

Relevant documents are returned to the application.

```text
Relevant Documents
 ↓
User or LLM
```

---

## Similarity Search

Vector databases use mathematical measures to compare vectors.

Common similarity metrics include:

- Cosine Similarity
    
- Euclidean Distance
    
- Dot Product
    

The objective is to identify which stored vectors are closest to the query vector.

Closer vectors generally indicate more semantically related content.

---

## Vector Databases and RAG

One of the most common uses of vector databases is Retrieval-Augmented Generation (RAG).

A typical RAG architecture looks like:

```text
User Question
        ↓
Embedding Model
        ↓
Vector Database
        ↓
Relevant Documents
        ↓
Large Language Model
        ↓
Generated Answer
```

The vector database provides relevant context before the model generates a response.

This helps reduce hallucinations and improves answer quality.

---

## Popular Vector Databases

Several vector databases are commonly used in AI applications.

Examples include:

- FAISS
    
- Qdrant
    
- Pinecone
    
- Weaviate
    
- Milvus
    
- Chroma
    
- Databricks Vector Search
    

Each solution offers different trade-offs regarding scalability, performance, deployment complexity, and cloud integration.

---

## Healthcare Applications

Vector databases can support healthcare research and operations by enabling:

- Semantic search across clinical notes
    
- Retrieval of similar patient cases
    
- Medical literature search
    
- Guideline retrieval
    
- Research support systems
    
- Clinical RAG applications
    

For example, a clinician may search:

```text
Children with asthma and frequent emergency visits
```

and retrieve clinically relevant records even when those exact words are not present.

---

## Limitations

Vector databases retrieve similar information, but similarity does not guarantee correctness.

Important limitations include:

- Retrieved documents may be outdated
    
- Retrieved content may be inaccurate
    
- Similarity does not imply causality
    
- Clinical validation remains necessary
    

A vector database helps locate information; it does not determine whether the information is true or appropriate.

---

## Vector Databases and Causal Inference

An important distinction for this research is that vector databases support information retrieval rather than causal reasoning.

A vector database can identify documents discussing similar concepts.

However, it cannot determine:

- Cause-and-effect relationships
    
- Treatment effects
    
- Counterfactual outcomes
    
- Causal mechanisms
    

These questions require additional causal inference methodologies.

---

## Key Takeaway

Vector databases are specialized systems designed to store and search embeddings efficiently.

They form the foundation of semantic search and Retrieval-Augmented Generation systems by enabling applications to retrieve relevant information based on meaning rather than exact keyword matches.

While extremely useful for information retrieval, vector databases should not be confused with systems capable of causal reasoning or scientific validation.
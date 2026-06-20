# Prompt Engineering Basics

## Introduction

Large Language Models (LLMs) generate responses based on instructions provided by users. These instructions are commonly referred to as prompts.

A prompt can be as simple as a question or as complex as a detailed set of instructions defining objectives, constraints, examples, and expected output formats.

The quality of the prompt often has a significant impact on the quality, consistency, and usefulness of the model's response.

---

## What is a Prompt?

A prompt is the information provided to an AI model to guide its behavior.

Example:

**Prompt**

```
What is diabetes?
```

**Response**

A general explanation of diabetes.

Although simple prompts can be useful, more structured prompts often produce more reliable results.

---

## Components of an Effective Prompt

### Objective

Clearly describe what the model should accomplish.

Example:

```
Summarize the following clinical note.
```

---

### Context

Provide background information relevant to the task.

Example:

```
You are assisting a healthcare researcher reviewing clinical records.
```

---

### Instructions

Specify how the response should be generated.

Example:

```
Identify diagnoses, medications, and symptoms.
```

---

### Output Format

Define the expected structure.

Example:

```json
{
  "diagnoses": [],
  "medications": [],
  "symptoms": []
}
```

Structured outputs are often easier to evaluate and process automatically.

---

## Prompt Example

### Unstructured Prompt

```
Analyze this clinical note.
```

This request is ambiguous and may produce inconsistent results.

### Structured Prompt

```
You are assisting a healthcare researcher.

Extract the following information from the clinical note:

- Diagnoses
- Medications
- Symptoms

Return the result as JSON.

Clinical Note:
[TEXT]
```

This version provides context, instructions, and an expected output format.

---

## Prompt Engineering Principles

### Be Specific

Clear instructions generally produce more reliable outputs than vague requests.

Instead of:

```
Tell me about this patient.
```

Prefer:

```
Identify all documented diagnoses and medications mentioned in this note.
```

---

### Define Constraints

Constraints help reduce unwanted behavior.

Example:

```
Only use information explicitly present in the note.
Do not infer additional diagnoses.
```

---

### Use Examples

Providing examples can improve consistency.

This technique is commonly called few-shot prompting.

Example:

Input:

```
Patient reports asthma and uses albuterol.
```

Output:

```json
{
  "diagnoses": ["asthma"],
  "medications": ["albuterol"]
}
```

---

### Request Structured Outputs

Whenever possible, request responses in a structured format such as JSON or tables.

Structured outputs simplify evaluation and downstream processing.

---

## Common Limitations

Prompt engineering can improve results but cannot eliminate all model limitations.

LLMs may still:

- Produce incorrect information
    
- Omit relevant details
    
- Misinterpret ambiguous language
    
- Generate inconsistent outputs
    

As a result, outputs should be validated, especially in healthcare and research contexts.

---

## Prompt Engineering in Healthcare Research

Prompt engineering can support:

- Literature review
    
- Information extraction
    
- Clinical note summarization
    
- Data annotation
    
- Knowledge organization
    

However, prompts should be carefully designed to ensure transparency, reproducibility, and consistency.

---

## Key Takeaway

Prompt engineering is the practice of designing instructions that help AI systems perform tasks more reliably and consistently.

Well-designed prompts typically include a clear objective, relevant context, explicit instructions, and a defined output format.

- White, J. et al. (2023). _A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT_. DOI: **10.48550/arXiv.2302.11382**
- Reynolds, L.; McDonell, K. (2021). _Prompt Programming for Large Language Models: Beyond the Few-Shot Paradigm_. DOI: **10.48550/arXiv.2102.07350**
- Liu, P. et al. (2023). _Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing_. DOI: **10.1145/3560815**
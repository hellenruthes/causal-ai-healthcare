# What Are Tokens?

## Introduction

Large Language Models do not process text as words or sentences.

Instead, they process smaller units called tokens.

Tokens are the fundamental units used by language models to represent and understand text.

---

## What Is a Token?

A token is a piece of text used internally by a language model.

A token may represent:

- A word
    
- Part of a word
    
- A punctuation symbol
    
- A number
    
- A special character
    

Examples:

```text
Artificial Intelligence
```

May be represented internally as multiple tokens.

---

## Why Tokens Matter

Tokens determine:

- Model input size
    
- Model output size
    
- Context window limits
    
- API costs
    

Most AI providers charge based on token usage.

---

## Example

Prompt:

```text
What is Artificial Intelligence?
```

Might be represented internally as:

```text
What
 is
 Artificial
 Intelligence
 ?
```

Each piece becomes one or more tokens.

---

## Context Windows

Models have limits on how many tokens they can process at once.

The combination of:

- Input tokens
    
- Output tokens
    

must fit within the model's context window.

---

## Common Misconception

A token is not necessarily a word.

In English:

```text
Artificial
```

may be one token.

In another context it may be split into multiple tokens.

---

## Why Researchers Should Care

Token usage affects:

- Cost
    
- Latency
    
- Prompt design
    
- Retrieval systems
    
- Model scalability
    

However, token counts alone do not measure model quality or scientific validity.

A system may consume fewer tokens while producing worse results.

---

## Key Takeaway

Tokens are the units used internally by language models to process information.

They affect cost and technical performance, but they are not direct indicators of model accuracy or scientific usefulness.
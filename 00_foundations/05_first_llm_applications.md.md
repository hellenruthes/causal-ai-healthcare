# First LLM Application

## Introduction

After understanding the concepts of Artificial Intelligence, prompts, APIs, and environment variables, it is now possible to build a simple application that interacts with a Large Language Model (LLM).

The objective of this example is to demonstrate the minimum components required to send a prompt to an AI model and receive a response.

---

## Application Architecture

The interaction between an application and a Large Language Model follows a relatively simple flow.

```text
User
  ↓
Python Application
  ↓
Prompt
  ↓
OpenAI API
  ↓
GPT Model
  ↓
Response
  ↓
Application Output
```

The application sends a request to the model and receives a generated response.

---

## Project Structure

Example:

```text
causal-ai-healthcare/

├── .env
├── requirements.txt
├── Makefile
└── 00_foundations/
    └── Examples/
        └── 01_first_llm_call.py
```

---

## Required Dependencies

Install dependencies using:

```bash
make setup
```

or

```bash
pip install -r requirements.txt
```

---

## Environment Configuration

Create a `.env` file in the project root.

Example:

```env
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxx
```

The application will load the API key during execution.

---

## Example Code

```python
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "OPENAI_API_KEY not found."
    )

client = OpenAI(api_key=api_key)

response = client.responses.create(
    model="gpt-5-mini",
    input="Explain Artificial Intelligence in one paragraph."
)

print(response.output_text)
```

---

## What Happens During Execution?

Step 1:

The application loads the environment variables.

```text
.env
 ↓
OPENAI_API_KEY
```

Step 2:

The application creates a connection to the OpenAI API.

```text
Application
 ↓
OpenAI Client
```

Step 3:

A prompt is sent to the model.

```text
Explain Artificial Intelligence in one paragraph.
```

Step 4:

The model generates a response.

```text
GPT Model
 ↓
Generated Text
```

Step 5:

The response is displayed to the user.

---

## Why This Example Matters

Although simple, this example contains the fundamental building blocks of most modern AI applications:

- Environment variables
    
- API authentication
    
- Prompt execution
    
- Model interaction
    
- Response handling
    

More advanced systems such as chatbots, agents, Retrieval-Augmented Generation (RAG), and workflow automation all build upon these same concepts.

---

## Common Errors

### Missing API Key

Error:

```text
OPENAI_API_KEY not found
```

Solution:

Verify that the `.env` file exists and contains a valid API key.

---

### Missing Dependencies

Error:

```text
ModuleNotFoundError
```

Solution:

Install dependencies using:

```bash
make setup
```

---

### Invalid Credentials

Error:

```text
401 Unauthorized
```

Solution:

Verify that the API key is valid and active.

---

## Key Takeaway

A modern AI application can be reduced to a simple sequence:

```text
Prompt
 ↓
API
 ↓
Model
 ↓
Response
```

Understanding this flow is essential before exploring more advanced topics such as prompt optimization, evaluation, retrieval systems, agents, and causal reasoning workflows.
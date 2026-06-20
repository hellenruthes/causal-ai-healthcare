# Environment Variables

## Introduction

Applications frequently require access to sensitive information such as:

- API keys
    
- Passwords
    
- Database credentials
    
- Access tokens
    

Storing these values directly in source code is considered a poor security practice because sensitive information may be accidentally shared through source control systems such as Git.

Environment variables provide a safer way to store configuration values outside the application code.

---

## What is an Environment Variable?

An environment variable is a configuration value stored outside the application.

The application can read these values during execution.

Example:

```text
OPENAI_API_KEY
```

Instead of storing the API key directly in the source code, the application retrieves it from the environment.

---

## Why Environment Variables Matter

Consider the following example:

### Bad Practice

```python
client = OpenAI(
    api_key="sk-proj-xxxxxxxxxxxxxxxx"
)
```

Problems:

- Secrets are exposed in the source code.
    
- Credentials may be committed to Git repositories.
    
- Rotating credentials becomes difficult.
    

---

### Recommended Practice

```python
import os

api_key = os.getenv("OPENAI_API_KEY")
```

Benefits:

- Secrets remain outside the codebase.
    
- Credentials can be changed without modifying the application.
    
- Different environments can use different configurations.
    

---

## The .env File

During development, environment variables are commonly stored in a `.env` file.

Example:

```env
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxx
```

The application loads these values at runtime.

---

## Loading Environment Variables in Python

The `python-dotenv` library can be used to load variables from a `.env` file.

Example:

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
```

After loading the file, the variable becomes available to the application.

---

## Environment Variables and AI Applications

Most modern AI providers use API keys for authentication.

Examples include:

- OpenAI
    
- Anthropic
    
- Google Gemini
    
- Cohere
    

Applications typically authenticate using an API key stored in an environment variable.

Example:

```python
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
```

This approach avoids exposing credentials in notebooks, scripts, and repositories.

---

## Security Considerations

Environment variables improve security but should still be handled carefully.

Recommended practices:

- Never commit `.env` files to Git.
    
- Never share API keys publicly.
    
- Rotate credentials if they are accidentally exposed.
    
- Use separate credentials for development and production environments.
    

---

## Git Configuration

The `.env` file should be included in `.gitignore`.

Example:

```gitignore
.env
```

This prevents sensitive information from being uploaded to source control repositories.

---

## Key Takeaway

Environment variables provide a secure and flexible mechanism for managing application configuration.

They are widely used in modern software development and are considered a fundamental best practice when working with APIs, cloud services, databases, and Artificial Intelligence platforms.
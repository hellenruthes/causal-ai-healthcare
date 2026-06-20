## Running the Examples

This repository contains independent examples designed to demonstrate different Artificial Intelligence concepts.

## Environment Variables

Before running any example, create a `.env` file in the project root.

Example:

```env
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxx
```

### Verify Configuration

You can verify that the API key is being loaded correctly by running:

```bash
make run-example
```

If the API key is not configured correctly, you should see an error similar to:

```text
OPENAI_API_KEY not found. Check if the .env file exists in the project root.
```

### Security Notes

* Never commit your `.env` file to Git.
* Never share your API key publicly.
* Ensure `.env` is included in `.gitignore`.

Example `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
```


### Option 1 – Run Examples Individually

Navigate to the desired example folder and execute the Python script.

Example:

```bash
cd Examples
python 01_first_llm_call.py
```

This approach is useful when exploring examples one at a time.

---

### Option 2 – Use Make Commands

The repository provides a Makefile to simplify setup and execution.

Install dependencies:

```bash
make install
```

Run the first example:

```bash
make run-example
```

Using Make commands is recommended because it provides a consistent execution process across all examples.

---

### Environment Variables

Before running any example, create a `.env` file in the project root.

Example:

```env
OPENAI_API_KEY=your_api_key_here
```

The examples will automatically load the API key from this file.

---

### Recommended Workflow

1. Clone the repository.
2. Create a `.env` file.
3. Run:

```bash
make install
```

4. Execute examples using either:

```bash
python <example_file>.py
```

or

```bash
make <target>
```
### Troubleshooting

If an example fails:

1. Verify that Python is installed.
2. Verify that dependencies were installed.
3. Verify that the `.env` file exists.
4. Verify that the API key is valid.
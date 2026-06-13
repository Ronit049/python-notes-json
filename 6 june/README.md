# Gemini AI Text Processing Application

## Overview

This Python script is a simple **Gemini AI-powered text processing application**. It reads data from different files, sends that data to Google's Gemini model, and displays the generated responses.

---

# 1. Importing Libraries

```python
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
```

## Purpose

| Library               | Purpose                                       |
| --------------------- | --------------------------------------------- |
| `google.generativeai` | Access Gemini AI API                          |
| `dotenv`              | Load environment variables from `.env` file   |
| `os`                  | Access operating system environment variables |
| `json`                | Read and process JSON files                   |

---

# 2. Loading Environment Variables

```python
load_dotenv()
```

This loads environment variables from a `.env` file.

### Example `.env`

```env
gemini_api_key=AIzaSyXXXXXX
```

Retrieve the API key using:

```python
os.getenv("gemini_api_key")
```

---

# 3. Function: `generate_response()`

```python
def generate_response(prompt):
    genai.configure(api_key=os.getenv("gemini_api_key"))
    response = genai.GenerativeModel("gemini-2.5-flash")
    output = response.generate_content(prompt)
    return output.text
```

## Purpose

This function sends a prompt to Gemini and returns the generated response.

### Step-by-Step

#### Configure Gemini API

```python
genai.configure(api_key=os.getenv("gemini_api_key"))
```

Connects to Gemini using the API key.

---

#### Create Model Instance

```python
response = genai.GenerativeModel("gemini-2.5-flash")
```

Initializes the Gemini Flash model.

---

#### Generate Content

```python
output = response.generate_content(prompt)
```

Sends the prompt to Gemini.

---

#### Return Response

```python
return output.text
```

Returns the generated text output.

---

# 4. Reading `role.json`

```python
with open("input/role.json", "r") as file:
```

### Example `role.json`

```json
{
  "role": "You are a Python teacher"
}
```

Load JSON:

```python
content = json.load(file)
```

Send to Gemini:

```python
response = generate_response(str(content))
```

Example prompt sent:

```python
"{'role': 'You are a Python teacher'}"
```

Display response:

```python
print(response)
```

---

# 5. Reading `response.json`

```python
with open("input/response.json", "r") as res_file:
```

### Example `response.json`

```json
{
  "format": "Give answer in bullet points"
}
```

Load and send to Gemini:

```python
response_type = generate_response(str(json.load(res_file)))
```

### Current Issue

The result is stored in:

```python
response_type
```

but it is never used later in the code.

Therefore, this section currently has no effect on the final output.

---

# 6. Reading `prompt.txt`

```python
with open("input/prompt.txt", "r", encoding="utf-8") as prompt_data:
```

### Example `prompt.txt`

```txt
Explain Python Functions
```

Send prompt to Gemini:

```python
summerized_answer = generate_response(prompt_data.read())
```

Display output:

```python
print(summerized_answer)
```

---

# 7. Error Handling

```python
except FileNotFoundError as e:
    print("file not found")
```

If any file is missing:

* `role.json`
* `response.json`
* `prompt.txt`

the program prints:

```text
file not found
```

instead of crashing.

---

# Current Workflow

```text
role.json
    ↓
 Gemini
    ↓
 Print Response

response.json
    ↓
 Gemini
    ↓
 Stored (Unused)

prompt.txt
    ↓
 Gemini
    ↓
 Print Response
```

---

# Purpose of This Project

This project appears to be the foundation of an **Agentic AI / Prompt Engineering System**.

## role.json

Defines the AI's behavior.

Example:

```json
{
  "role": "You are an expert Python teacher"
}
```

---

## response.json

Defines the output format.

Example:

```json
{
  "format": "Answer in Markdown"
}
```

---

## prompt.txt

Contains the user's actual query.

Example:

```txt
Explain Python decorators.
```

---

# Recommended Improvement

Instead of sending each file separately to Gemini, combine them into a single prompt.

```python
final_prompt = f"""
Role:
{role}

Response Format:
{response_format}

User Query:
{prompt}
"""
```

Then generate the response:

```python
generate_response(final_prompt)
```

---

# Benefits of This Structure

✅ Better code modularity

✅ Easy role customization

✅ Easy response format customization

✅ Cleaner project structure

✅ More suitable for Agentic AI applications

---

# Conclusion

This code is a basic Gemini-powered AI assistant framework that:

1. Loads an API key from a `.env` file.
2. Reads configuration data from JSON files.
3. Reads a user prompt from a text file.
4. Sends prompts to Gemini AI.
5. Prints the generated responses.
6. Serves as a starting point for building a modular Agentic AI application.



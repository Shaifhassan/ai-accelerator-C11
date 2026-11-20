# Day 4 beginner assignments

Complete either assignment independently. Each has four TODO blocks. Replace the `raise NotImplementedError(...)` line between each START and END comment with your solution, keeping the surrounding code and indentation. Use the step-by-step guide shared by your host for hints and solutions.

1. **assignment_1_ask_ai.py** — send a question to OpenRouter and print the model's answer.
2. **assignment_2_chatbot.py** — build a Gradio chatbot that includes previous messages as conversation context.

## Run in Google Colab

Open a new notebook at https://colab.research.google.com using the default CPU runtime. No GPU or virtual environment is needed. Install the packages in a code cell:

```python
%pip install -q "gradio>=6.0,<7.0" "openai>=2.0,<3.0"
```

Upload your chosen Python file:

```python
from google.colab import files
uploaded = files.upload()
```

Open the file from Colab's Files panel, complete its four TODO blocks, and save. Then run the appropriate command in a new code cell:

```python
%run assignment_1_ask_ai.py
```

or:

```python
%run assignment_2_chatbot.py
```

Assignment 1 prompts for an OpenRouter key using hidden input and prints `AI answer:` below the cell. Assignment 2 creates a temporary public Gradio link; open it and enter your key under API settings. Keep the launch cell running while using the chatbot; stop it before restarting after edits. Download your edited file to preserve your work after the Colab runtime ends.

Get a key at https://openrouter.ai/settings/keys and confirm model access and credits with your host. Keep keys out of code and screenshots. The default model is `openai/gpt-4o-mini`. The host can select another model through the `OPENROUTER_MODEL` environment variable before running a file.

## Check your results

- Assignment 1 should print a relevant answer to your prompt. Each run starts a fresh request.
- Assignment 2: say "My name is Asha. I run a bakery." Then ask "What is my name and what business do I run?" The reply should use the earlier details.
- `Complete TODO` means a placeholder remains. An indentation error means you should check spaces, quotes, and brackets. HTTP 401 indicates a key problem; 402 indicates a credit or spending-limit problem; 429 indicates rate limiting. Ask your host about other API errors.

## Run locally

From this assignments folder, in an activated Python environment:

```text
python -m pip install -r requirements.txt
python assignment_1_ask_ai.py
```

For the chatbot, run `python assignment_2_chatbot.py` and open the printed local URL. The parent folder's `app.py` is the existing advanced demonstration, not one of these two assignments.

The previous four assignments remain recoverable in Git history.

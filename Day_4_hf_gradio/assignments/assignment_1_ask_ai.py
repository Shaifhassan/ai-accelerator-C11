"""Assignment 1: send one question to AI. Complete the four TODO blocks.

Read README.md in this folder. Replace each marked block with its guide snippet.
Run: python assignment_1_ask_ai.py
"""

import os
from getpass import getpass

from openai import OpenAI, APIConnectionError, APIStatusError

MODEL = os.getenv("OPENROUTER_MODEL", "openai/gpt-4o-mini")


def ask_ai(client, prompt):
    # TODO 2 START: wrap the question in a user message.
    raise NotImplementedError("Complete TODO 2 using the learner guide.")
    # TODO 2 END

    # TODO 3 START: send messages to the model.
    raise NotImplementedError("Complete TODO 3 using the learner guide.")
    # TODO 3 END

    # TODO 4 START: return the text from the first answer.
    raise NotImplementedError("Complete TODO 4 using the learner guide.")
    # TODO 4 END


def main():
    # Key entry and connection setup are supplied so you can focus on the request.
    api_key = os.getenv("OPENROUTER_API_KEY", "").strip()
    if not api_key:
        api_key = getpass("Paste your OpenRouter API key (hidden): ").strip()
    if not api_key:
        print("No API key entered. Run again and paste your key.")
        return

    # TODO 1 START: choose a clear question for the AI.
    raise NotImplementedError("Complete TODO 1 using the learner guide.")
    # TODO 1 END

    with OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key,
                timeout=45.0, max_retries=0) as client:
        print("Asking AI... Please wait.")
        print("AI answer:", ask_ai(client, prompt))


if __name__ == "__main__":
    try:
        main()
    except NotImplementedError as error:
        print(error)
    except APIConnectionError:
        print("Could not connect. Check your internet connection and try again.")
    except APIStatusError as error:
        print(f"API request failed (HTTP {error.status_code}). See the guide's troubleshooting section.")

"""Assignment 2: build a text chatbot with conversation context.

Complete four TODO blocks using README.md. This file works independently of
Assignment 1. Run: python assignment_2_chatbot.py
"""

import os

import gradio as gr
from openai import OpenAI, APIConnectionError, APIStatusError

MODEL = os.getenv("OPENROUTER_MODEL", "openai/gpt-4o-mini")


def text_history(history):
    """Supplied helper: convert Gradio 6 content blocks into plain text messages."""
    result = []
    for item in history:
        if item.get("role") not in ("user", "assistant"):
            continue
        content = item.get("content", "")
        if isinstance(content, list):
            content = "\n".join(
                block.get("text", "") for block in content
                if isinstance(block, dict) and block.get("type") == "text"
            )
        if isinstance(content, str) and content.strip():
            result.append({"role": item["role"], "content": content})
    return result


def build_messages(message, history):
    # TODO 1 START: give the assistant a simple instruction.
    raise NotImplementedError("Complete TODO 1 using the learner guide.")
    # TODO 1 END

    # TODO 2 START: include the earlier conversation.
    raise NotImplementedError("Complete TODO 2 using the learner guide.")
    # TODO 2 END

    # TODO 3 START: add the new question after the history.
    raise NotImplementedError("Complete TODO 3 using the learner guide.")
    # TODO 3 END
    return messages


def respond(message, history, api_key):
    key = (api_key or os.getenv("OPENROUTER_API_KEY", "")).strip()
    if not key:
        return "Open API settings and enter your OpenRouter API key first."
    if not message.strip():
        return "Please type a question."
    try:
        with OpenAI(base_url="https://openrouter.ai/api/v1", api_key=key,
                    timeout=45.0, max_retries=0) as client:
            response = client.chat.completions.create(
                model=MODEL,
                messages=build_messages(message, history),
                max_tokens=300,
            )
        return response.choices[0].message.content or "No text returned. Please try again."
    except NotImplementedError as error:
        return str(error)
    except APIConnectionError:
        return "Could not connect. Check your internet connection and try again."
    except APIStatusError as error:
        return f"API request failed (HTTP {error.status_code}). See the learner guide."


def build_demo():
    api_key_input = gr.Textbox(label="OpenRouter API Key", type="password")
    # TODO 4 START: connect the chat interface to respond and the key input.
    raise NotImplementedError("Complete TODO 4 using the learner guide.")
    # TODO 4 END


if __name__ == "__main__":
    try:
        # Gradio automatically enables a public share link in Google Colab.
        # debug=True keeps notebook execution active and shows errors there.
        build_demo().launch(debug=True)
    except NotImplementedError as error:
        print(error)

"""
CLI entry point for the telecom RAG chatbot.
Usage: python main.py
"""

import os
# FORCE Python to use the compatible protobuf parser before any other library loads
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
os.environ["TRANSFORMERS_VERBOSITY"] = "error"

# Now your regular imports can safely follow
import streamlit as st
from dotenv import load_dotenv
from rag_chain import build_chain

# ... rest of your code


load_dotenv()


def main():
    print("=== Telecom Customer Care Chatbot (RAG) ===")
    print("Type your question and press Enter. Type 'quit' to exit.\n")

    chain = build_chain()

    while True:
        question = input("Customer: ").strip()
        if not question:
            continue
        if question.lower() in {"quit", "exit", "q"}:
            print("Goodbye!")
            break

        print("\nAssistant: ", end="", flush=True)
        for chunk in chain.stream(question):
            print(chunk, end="", flush=True)
        print("\n")


if __name__ == "__main__":
    main()

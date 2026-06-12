"""
CLI entry point for the telecom RAG chatbot.
Usage: python main.py
"""
import os
import sys

# 1. FORCE the pure-Python protobuf implementation immediately
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
os.environ["TRANSFORMERS_VERBOSITY"] = "error"

# 2. Ensure local modules can be found safely
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Now your existing code can safely start below this line
from rag_chain import build_chain

# ... rest of your app.py code


import streamlit as st
from dotenv import load_dotenv
from rag_chain import build_chain



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

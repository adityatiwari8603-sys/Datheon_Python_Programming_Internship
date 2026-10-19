"""
DATHEON PYTHON PROGRAMMING INTERNSHIP
Task 4: Customer Support Chatbot

A rule-based chatbot using Python, JSON, and regex.
"""

import json
import re
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
FAQ_FILE = BASE_DIR / "faqs.json"


def load_faqs():
    """Load chatbot responses from JSON."""
    try:
        with open(FAQ_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as error:
        print(f"Error loading FAQ data: {error}")
        return None


def find_responses(message, faqs):
    """Find matching answers using keywords and regex."""
    responses = []

    for intent in faqs["intents"]:
        for pattern in intent["patterns"]:
            if re.search(pattern, message, re.IGNORECASE):
                responses.append(intent["response"])
                break

    return list(dict.fromkeys(responses))


def chatbot():
    """Start the customer support chatbot."""

    faqs = load_faqs()

    if faqs is None:
        return

    print("=" * 55)
    print("             CUSTOMER SUPPORT CHATBOT")
    print("=" * 55)

    print("Bot: Hello! Welcome to our customer support.")
    print("Bot: Ask me about products, prices, shipping,")
    print("     returns, refunds, or business hours.")
    print("Bot: Type 'bye' or 'exit' to end the conversation.")

    user_name = None

    while True:
        try:
            message = input("\nYou: ").strip()

            if not message:
                print("Bot: Please enter a question.")
                continue

            if re.fullmatch(
                r"(bye|goodbye|exit|quit)",
                message,
                re.IGNORECASE
            ):
                goodbye = (
                    f"Goodbye, {user_name}!"
                    if user_name
                    else "Goodbye!"
                )
                print(f"Bot: {goodbye} Have a great day!")
                break

            name_match = re.search(
                r"\bmy name is ([a-zA-Z]+)\b",
                message,
                re.IGNORECASE
            )

            if name_match:
                user_name = name_match.group(1).title()
                print(f"Bot: Nice to meet you, {user_name}!")
                continue

            responses = find_responses(message, faqs)

            if responses:
                for response in responses:
                    print(f"Bot: {response}")
            else:
                print(
                    "Bot: Sorry, I didn't understand that. "
                    "Please ask about products, pricing, "
                    "shipping, returns, refunds, or hours."
                )

        except (KeyboardInterrupt, EOFError):
            print("\nBot: Conversation ended. Goodbye!")
            break


if __name__ == "__main__":
    chatbot()
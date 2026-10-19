
# Customer Support Chatbot

## Datheon Python Programming Internship — Task 4

### Project Overview

This project is a rule-based Customer Support Chatbot developed using Python.

The chatbot answers common customer questions about products, pricing, shipping, returns, refunds, business hours, and contact information.

It uses regular expressions to identify customer questions and a JSON file to store predefined responses.

### Features

* Responds to greetings.
* Answers frequently asked questions.
* Provides information about products and pricing.
* Explains shipping, returns, and refund policies.
* Provides business hours and contact information.
* Supports multiple matching questions in one message.
* Remembers the user's first name during a conversation.
* Handles unrecognized questions with a fallback response.
* Supports `bye`, `exit`, and `quit` commands.

### Technologies Used

* Python 3
* JSON
* Regular expressions (`re`)
* `pathlib`

### Project Files

* `chatbot.py` — Main chatbot application.
* `faqs.json` — Questions, matching patterns, and responses.
* `README.md` — Project documentation.

### How to Run

Open a terminal in the main internship project folder and execute:

```powershell
python .\Task_4_Chatbot\chatbot.py
```

Type a question when the chatbot displays `You:`.

Enter `bye` to end the conversation.

### Example Conversation

```text
You: hello
Bot: Hello! How can I help you today?

You: What are your business hours?
Bot: Our business hours are Monday to Saturday, 9 AM to 6 PM.

You: Can I return a product?
Bot: Products can be returned within 7 days if they meet our return conditions.

You: My name is Alex
Bot: Nice to meet you, Alex!

You: bye
Bot: Goodbye, Alex! Have a great day!
```

### Testing

The chatbot was tested successfully with:

* Greetings
* Business hours
* Product information
* Pricing
* Shipping
* Returns and refunds
* Unknown questions
* Name recognition
* Goodbye commands

### Note

The business information and policies are fictional and included for demonstration purposes only.

### Author

Developed as part of the Datheon Python Programming Internship.

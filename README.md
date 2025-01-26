# AI Personal Assistant 🤖

A voice-controlled personal assistant built in Python that can perform various tasks including weather updates, news reading, email sending, web searches, and basic calculations.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Function Documentation](#function-documentation)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Troubleshooting](#troubleshooting)

## Features
- 🗣️ Voice Recognition and Response
- 🌤️ Real-time Weather Updates
- 📰 News Summarization
- 📧 Email Automation
- 🔍 Web Searches
- 🧮 Basic Calculations
- ⏰ Reminders
- 📅 Date and Time Information

## Installation

### Prerequisites
- Python 3.7+
- pip package manager

### Step 1: Clone the repository
```bash
git clone https://github.com/yourusername/ai-personal-assistant.git
cd ai-personal-assistant
python -m venv venv
# For Windows
venv\Scripts\activate
# For Unix or MacOS
source venv/bin/activate
pip install -r requirements.txt
SpeechRecognition==3.8.1
pyttsx3==2.90
requests==2.26.0
PyAudio==0.2.11
python-dotenv==0.19.0
```

### Usage
Running the Assistant
```BASH

python personal_assistant.py
Voice Commands Examples
```
```PLAINTEXT

Collapse
"What's the weather in London?"
→ Returns current weather in London

"Tell me the news"
→ Reads top 3 news headlines

"Calculate 25 plus 5"
→ Returns "30"

"Send an email"
→ Initiates email sending process

"Search for Python tutorials"
→ Opens web browser with search results

"What's the time?"
→ Speaks current time

"Set a reminder"
→ Sets a reminder for specified time
```

### Project Structure

Collapse
ai-personal-assistant/
│
├── personal_assistant.py     # Main application file
├── requirements.txt         # Package dependencies
├── .env                    # Environment variables
├── reminders.txt           # Stored reminders
├── README.md              # Project documentation
│
├── utils/
│   ├── __init__.py
│   ├── speech_utils.py    # Speech recognition utilities
│   ├── api_utils.py       # API handling utilities
│   └── email_utils.py     # Email handling utilities
│
└── tests/
    ├── __init__.py
    └── test_assistant.py  # Unit tests

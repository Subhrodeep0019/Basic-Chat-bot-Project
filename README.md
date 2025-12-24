# Basic AI Chatbot Project

    A simple Python-based AI chatbot built to explore how Hugging Face Inference APIs work and how large language model (LLM) responses are structured.

## Overview

    This project demonstrates:
    - Making API calls to Hugging Face hosted models
    - Sending prompts and receiving responses from an LLM
    - Using environment variables to securely manage API keys
    - Understanding the basic request–response flow of an AI chatbot

    This is a learning-focused project and is not intended for production use.

## Tech Stack

    - Python
    - Hugging Face Inference API
    - `huggingface_hub`
    - `python-dotenv`

## Project Structure

    chatbot-project/
    │
    ├── chatbot.py # Main chatbot script
    ├── requirements.txt # Project dependencies
    ├── .gitignore # Ignored files (venv, .env)
    └── .env # API key (not committed)



## Setup Instructions

    ### 1. Clone the repository
    git clone https://github.com/Subhrodeep0019/Basic-Chat-bot-Project.git
    cd Basic-Chat-bot-Project

### 2. Create and activate a virtual environment
    python -m venv Env1
    Env1\Scripts\activate # Windows

### 3. Install dependencies
    pip install -r requirements.txt


### 4. Create a `.env` file
    Create a file named `.env` in the project root and add:

    API_KEY=your_huggingface_api_key_here


### 5. Run the chatbot
    python chatbot.py


## Notes

    - The `.env` file is intentionally excluded from version control.
    - API response formats may differ between providers (Hugging Face, OpenAI, etc.).
    - This project focuses on API usage, not model training.

## Future Improvements

    - Add conversation memory
    - Improve prompt handling
    - Convert to a backend service (FastAPI/Flask)
    - Add error handling and logging

## License

    This project is for educational purposes.

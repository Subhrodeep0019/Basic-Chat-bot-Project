import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# get hugging face api key form .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

model = "google/gemma-2-2b-it"

client = InferenceClient(model = model, token = API_KEY)

message = [
    {
        "role": "system",
        "content": "you are a friendly sarcastic consise assistant. Keep replies short but funny sarcastic." 
    }
]

print("\nChat-bot (conversational), type 'exit' or 'quit' to quit.\n")

while True:
    user_text = input("you: ").strip()
    if user_text in ["exit", "quit"]: 
        print("Bot: bye bye...")
        break
    
    message.append(
        {
            "role": "user",
            "content": user_text
        }
    )
    4
    try:
        response = client.chat_completion(
            messages= message,
            max_tokens= 300,
            temperature= 0.7,
            top_p= 0.9,
            stop= ["\nUser: ", "\nSystem: "]
        )

        bot_text = response.choices[0].message["content"]
        
    except Exception as e:
        print(f"bot error: {e}")
        # remove the last user message so the history stays clean on errors
        message.pop()
        continue

    print(f"Bot: {bot_text}")
    message.append(
        {
            "role": "assistant",
            "content": bot_text
        }
    )

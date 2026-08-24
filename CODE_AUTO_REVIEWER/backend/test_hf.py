import os
from dotenv import load_dotenv
from huggingface_hub import login

load_dotenv()

token = os.getenv("HF_TOKEN")

if token:
    login(token=token)
    print("Hugging Face login successful!")
else:
    print("HF_TOKEN not found!")
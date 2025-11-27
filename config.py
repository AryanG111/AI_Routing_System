# config.py
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# 1. Get API Key from Environment Variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Please set it in the .env file.")

# 2. Configure the Client to point to Google
genai.configure(api_key=GEMINI_API_KEY)

# 3. Define Models
# We use Gemini 2.0 Flash as it is available and performant.
# You can switch the SMART model to "gemini-1.5-pro" if you need higher intelligence later.
MODEL_SMART = "gemini-2.0-flash"
MODEL_FAST = "gemini-2.0-flash"
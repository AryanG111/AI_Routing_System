# config.py
import os
from openai import OpenAI

# 1. PASTE YOUR GEMINI KEY HERE
# (Keep this safe! Don't share this file publicly)
GEMINI_API_KEY = "AIzaSyC-6lsc_pQ0Fm3ypLXrKhCeDbOhjA_yexs" 

# 2. Configure the Client to point to Google
client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# 3. Define Models
# We use Gemini 1.5 Flash for everything because it's fast and free.
# You can switch the SMART model to "gemini-1.5-pro" if you need higher intelligence later.
MODEL_SMART = "gemini-1.5-flash"
MODEL_FAST = "gemini-1.5-flash"
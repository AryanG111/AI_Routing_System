# core_logic.py
import json
import google.generativeai as genai
from config import MODEL_SMART, MODEL_FAST
from prompts import ROUTER_SYSTEM_PROMPT, AGENT_PROMPTS, MERGER_SYSTEM_PROMPT

class Router:
    def route(self, query):
        """Decides which agents to call."""
        try:
            model = genai.GenerativeModel(
                model_name=MODEL_SMART,
                system_instruction=ROUTER_SYSTEM_PROMPT,
                generation_config={"response_mime_type": "application/json"}
            )
            
            response = model.generate_content(query)
            
            content = response.text
            data = json.loads(content)
            return data.get("selected_agents", [])
            
        except Exception as e:
            print(f"⚠️ Router Error: {e}")
            # Fallback mechanism: If router fails, default to Tech Agent
            return ["tech_agent"]

class SpecializedAgent:
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.system_prompt = AGENT_PROMPTS.get(agent_id, "You are a helpful assistant.")

    def run(self, query):
        """Generates a specific expert response."""
        try:
            model = genai.GenerativeModel(
                model_name=MODEL_FAST,
                system_instruction=self.system_prompt
            )
            response = model.generate_content(query)
            return response.text
        except Exception as e:
            return f"Error in agent {self.agent_id}: {str(e)}"

class Merger:
    def merge(self, query, agent_responses):
        """Combines multiple responses into one."""
        combined_text = ""
        for agent_id, text in agent_responses.items():
            # Clean up the ID for better reading (e.g., "tech_agent" -> "Tech Agent")
            readable_name = agent_id.replace("_", " ").title()
            combined_text += f"\n--- INPUT FROM {readable_name} ---\n{text}\n"

        prompt = f"User Query: {query}\n\nExpert Reports:{combined_text}"

        try:
            model = genai.GenerativeModel(
                model_name=MODEL_SMART,
                system_instruction=MERGER_SYSTEM_PROMPT
            )
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error in merger: {str(e)}"
# core_logic.py
import json
import re
from config import client, MODEL_SMART, MODEL_FAST
from prompts import ROUTER_SYSTEM_PROMPT, AGENT_PROMPTS, MERGER_SYSTEM_PROMPT

class Router:
    def route(self, query):
        """Decides which agents to call."""
        try:
            response = client.chat.completions.create(
                model=MODEL_SMART,
                messages=[
                    {"role": "system", "content": ROUTER_SYSTEM_PROMPT},
                    {"role": "user", "content": query}
                ],
                response_format={"type": "json_object"}
            )
            
            content = response.choices[0].message.content
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
        response = client.chat.completions.create(
            model=MODEL_FAST,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": query}
            ]
        )
        return response.choices[0].message.content

class Merger:
    def merge(self, query, agent_responses):
        """Combines multiple responses into one."""
        combined_text = ""
        for agent_id, text in agent_responses.items():
            # Clean up the ID for better reading (e.g., "tech_agent" -> "Tech Agent")
            readable_name = agent_id.replace("_", " ").title()
            combined_text += f"\n--- INPUT FROM {readable_name} ---\n{text}\n"

        prompt = f"User Query: {query}\n\nExpert Reports:{combined_text}"

        response = client.chat.completions.create(
            model=MODEL_SMART,
            messages=[
                {"role": "system", "content": MERGER_SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content  
from core_logic import Router, SpecializedAgent, Merger

class AIWorkflow:
    def __init__(self):
        self.router = Router()
        self.merger = Merger()
        # Pre-load agents into a dictionary for easy access
        self.agents = {
            "sustainability_agent": SpecializedAgent("sustainability_agent"),
            "business_agent": SpecializedAgent("business_agent"),
            "tech_agent": SpecializedAgent("tech_agent")
        }

    def process_query(self, user_query):
        print(f"🔹 Processing: {user_query}")
        
        # Step 1: Route
        selected_agent_ids = self.router.route(user_query)
        print(f"🔸 Routing to: {selected_agent_ids}")

        # Step 2: Parallel Execution (Gathering responses)
        agent_responses = {}
        for agent_id in selected_agent_ids:
            if agent_id in self.agents:
                # In a real app, you would run these in parallel using asyncio
                print(f"   ...Running {agent_id}...")
                response_text = self.agents[agent_id].run(user_query)
                agent_responses[agent_id] = response_text

        # Step 3: Merge
        print("🔹 Merging responses...")
        final_answer = self.merger.merge(user_query, agent_responses)
        
        return final_answer
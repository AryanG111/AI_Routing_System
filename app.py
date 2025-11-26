import streamlit as st
import time
from workflow import AIWorkflow

# Page Configuration
st.set_page_config(
    page_title="AI Agent Orchestrator",
    page_icon="🤖",
    layout="centered"
)

# Initialize the Backend (Cache it so it doesn't reload on every click)
@st.cache_resource
def get_workflow():
    return AIWorkflow()

system = get_workflow()

# Title & Description
st.title("🤖 Multi-Agent Routing System")
st.markdown("""
Ask a question, and the **Router** will dispatch it to the correct expert:
- 🌿 **Sustainability Agent**
- 💼 **Business Strategy Agent**
- ⚙️ **Tech & AI Agent**
""")

st.divider()

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Previous Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- THE INPUT HANDLER ---
if prompt := st.chat_input("Ex: How can AI help reduce carbon footprint in logistics?"):
    
    # 1. Display User Message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Process with AI (The "Thinking" Phase)
    with st.chat_message("assistant"):
        
        # Create a Status Container to show the backend logic working
        status_container = st.status("🧠 Processing Query...", expanded=True)
        
        try:
            # Step A: Routing
            status_container.write("🔄 Router: Analyzing intent...")
            # We can't see the internal prints of workflow.py here, 
            # but we simulate the visual delay for better UX
            time.sleep(1) 
            
            # Step B: Execution (This calls your actual backend)
            status_container.write("🏃 Agents: Parallel Execution started...")
            final_response = system.process_query(prompt)
            
            # Step C: Merging
            status_container.write("📝 Merger: Synthesizing final answer...")
            time.sleep(0.5)
            
            # Update status to complete
            status_container.update(label="✅ Response Ready", state="complete", expanded=False)
            
            # 3. Display Final Answer
            st.markdown(final_response)
            
            # Save to history
            st.session_state.messages.append({"role": "assistant", "content": final_response})
            
        except Exception as e:
            status_container.update(label="❌ Error", state="error")
            st.error(f"An error occurred: {str(e)}")
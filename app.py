import streamlit as st
import time
from workflow import AIWorkflow

# Page Configuration
st.set_page_config(
    page_title="AI Agent System",
    page_icon="🤖",
    layout="wide"
)

# --- CUSTOM CSS FOR DYNAMIC UI ---
st.markdown("""
    <style>
        /* Import Font */
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Outfit', sans-serif;
            color: #E0E0E0;
            background-color: #000000;
        }

        /* Improved Fluid Animation */
        @keyframes fluid {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .stApp {
            /* More distinct colors for visibility */
            background: linear-gradient(-45deg, #000000, #1a1a2e, #16213e, #000000);
            background-size: 400% 400%;
            animation: fluid 10s ease infinite; /* Faster for visibility */
        }
        
        /* Fast Animation Class for Processing */
        .fast-anim {
            animation-duration: 2s !important;
        }

        /* Glassmorphism Cards */
        .agent-card {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(20px);
            border-radius: 15px;
            padding: 20px;
            border: 1px solid rgba(255, 255, 255, 0.05);
            text-align: center;
            transition: transform 0.3s ease, background 0.3s ease;
        }
        
        .agent-card:hover {
            transform: translateY(-2px);
            background: rgba(255, 255, 255, 0.07);
        }

        /* Hide Streamlit Elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Chat Styling */
        .stChatMessage {
            background-color: transparent;
            border: none;
        }

        /* User Message - Right Aligned */
        [data-testid="stChatMessage"]:nth-child(odd) {
            flex-direction: row-reverse;
            text-align: right;
            background-color: rgba(60, 60, 80, 0.6);
            border-radius: 12px;
            margin-left: 20%;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        /* Assistant Message - Left Aligned */
        [data-testid="stChatMessage"]:nth-child(even) {
            background-color: rgba(20, 20, 20, 0.8);
            border-radius: 12px;
            margin-right: 20%;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }
        
        h1 {
            font-weight: 600;
            text-align: center;
            color: #FFFFFF;
            text-shadow: 0 0 20px rgba(255, 255, 255, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Initialize Backend
@st.cache_resource
def get_workflow():
    return AIWorkflow()

system = get_workflow()

# --- HEADER & AGENT VISUALIZATION ---
st.title("🌌 Neural Routing System")
st.markdown("<p style='text-align: center; opacity: 0.7;'>Powered by Multi-Agent Intelligence</p>", unsafe_allow_html=True)

st.write("")
st.write("")

# Agent Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="agent-card">
        <h3>🌿 Sustainability</h3>
        <p>Expert in green energy, carbon footprint, and eco-impact.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="agent-card">
        <h3>💼 Business</h3>
        <p>Strategist for ROI, market analysis, and risk management.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="agent-card">
        <h3>⚙️ Tech & AI</h3>
        <p>Architect for software, AI stacks, and implementation.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- CHAT INTERFACE ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask the hive mind..."):
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Dynamic Speed Up Logic (Simulated via CSS injection for this block)
        st.markdown("""
            <style>
                .stApp { animation-duration: 2s !important; }
            </style>
        """, unsafe_allow_html=True)
        
        status_placeholder = st.empty()
        status_placeholder.markdown("⚡ **Routing Signal...**")
        
        try:
            # Simulate thinking steps
            time.sleep(0.8)
            status_placeholder.markdown("🧠 **Agents Processing...**")
            
            final_response = system.process_query(prompt)
            
            status_placeholder.empty()
            st.markdown(final_response)
            
            st.session_state.messages.append({"role": "assistant", "content": final_response})
            
        except Exception as e:
            st.error(f"System Failure: {str(e)}")
        
        # Revert Animation Speed
        st.markdown("""
            <style>
                .stApp { animation-duration: 10s !important; }
            </style>
        """, unsafe_allow_html=True)
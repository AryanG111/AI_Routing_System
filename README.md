# Neural Routing System

An intelligent multi-agent system that routes user queries to specialized agents (Sustainability, Business, Tech), executes them in parallel, and merges their insights into a cohesive response.

## Features

- **Intelligent Routing**: Analyzes user queries to select the most relevant agents.
- **Multi-Agent Architecture**:
  - **Sustainability Agent**: Focuses on environmental impact and green energy.
  - **Business Agent**: Focuses on ROI, market strategy, and profitability.
  - **Tech Agent**: Focuses on software architecture and implementation.
- **Parallel Execution**: Agents process queries concurrently for efficiency.
- **Smart Merging**: Combines insights from multiple agents into a single, unified answer.
- **Dynamic UI**: A beautiful, dark-themed Streamlit interface with fluid animations.

## Setup

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Environment Variables**:
    Create a `.env` file in the root directory and add your Google Gemini API key:
    ```env
    GEMINI_API_KEY=your_api_key_here
    ```

## Usage

Run the Streamlit application:
```bash
streamlit run app.py
```

## Project Structure

- `app.py`: Main Streamlit application file.
- `core_logic.py`: Contains the Router, SpecializedAgent, and Merger classes.
- `workflow.py`: Orchestrates the flow between Router, Agents, and Merger.
- `prompts.py`: System prompts for the agents.
- `config.py`: Configuration settings (API keys, model names).

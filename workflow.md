# AI Routing System Workflow

This document outlines the architectural flow of the AI Routing System.

## System Overview

The system is designed to intelligently route user queries to specialized AI agents, execute them in parallel, and merge their insights into a cohesive response.

## Flow Description

1.  **User Query**: The process begins when a user submits a query through the Streamlit interface.
2.  **AIWorkflow Orchestrator**: The `AIWorkflow` class manages the lifecycle of the request.
3.  **Router**: The `Router` analyzes the query and determines which specialized agents are best suited to handle it. It returns a list of agent IDs.
4.  **Specialized Agents**: The selected agents (Sustainability, Business, Tech) process the query independently using their specific system prompts.
5.  **Merger**: The `Merger` collects all agent responses and synthesizes them into a single, comprehensive answer.
6.  **Final Response**: The merged response is displayed to the user.

## Mermaid Diagram

```mermaid
graph TD
    User([User]) -->|Submits Query| UI[Streamlit Interface]
    UI -->|Passes Query| Workflow[AIWorkflow Class]
    
    subgraph Core Logic
        Workflow -->|1. Route| Router[Router Agent]
        Router -->|Selects Agents| AgentSelection{Selected Agents}
        
        AgentSelection -->|Includes| Sust[Sustainability Agent]
        AgentSelection -->|Includes| Biz[Business Agent]
        AgentSelection -->|Includes| Tech[Tech Agent]
        
        Sust -->|Response| Responses[Aggregated Responses]
        Biz -->|Response| Responses
        Tech -->|Response| Responses
        
        Responses -->|2. Merge| Merger[Merger Agent]
    end
    
    Merger -->|Final Answer| Workflow
    Workflow -->|Display| UI
    UI -->|Show Result| User

    style User fill:#f9f,stroke:#333,stroke-width:2px
    style UI fill:#bbf,stroke:#333,stroke-width:2px
    style Workflow fill:#dfd,stroke:#333,stroke-width:2px
    style Router fill:#fdd,stroke:#333,stroke-width:2px
    style Merger fill:#ddf,stroke:#333,stroke-width:2px
```

# 👔 Enterprise AI Mock Interview Simulator

## 📌 Business Objective
Technical and behavioral mock interviews are historically expensive, difficult to schedule, and prone to human bias. This application provides a zero-latency, highly customizable, AI-driven mock interview environment. It simulates both HR and Technical interviewers, adapts to the candidate's specific resume and target role, and provides a quantitative evaluation scorecard to accelerate interview readiness.

## 🏗️ Architecture & Tech Stack
* **Frontend UI & State Management:** `Streamlit` (Rapid Python-based Web UI)
* **Inference Engine:** **Groq LPU Cloud** (Millisecond latency inference)
* **Large Language Models (LLM):** `Llama-3` / `Mixtral` (Open-source, high-performance)
* **Architecture Pattern:** Stateful Chatbot with Persona-Driven System Prompting

## 📊 Executive Architecture (SOP)

```mermaid
graph TD
    %% High Contrast Theme Definitions
    classDef ui fill:#e3f2fd,stroke:#1565c0,stroke-width:3px,color:#000000,font-weight:bold;
    classDef logic fill:#ffffff,stroke:#333333,stroke-width:3px,color:#000000,font-weight:bold;
    classDef cloud fill:#fff3e0,stroke:#e65100,stroke-width:3px,color:#000000,font-weight:bold;
    classDef output fill:#e8f5e9,stroke:#2e7d32,stroke-width:3px,color:#000000,font-weight:bold;

    %% Nodes
    A([User: Configures Interview <br/> Role, Skills, Persona]):::ui
    B[Streamlit Session State <br/> Memory Initialization]:::logic
    C{Persona Router}:::logic
    
    D[HR System Prompt]:::logic
    E[Technical System Prompt]:::logic
    
    F[Groq API <br/> Llama-3 Inference]:::cloud
    G([AI Asks Question]):::ui
    H([User Provides Answer]):::ui
    
    I[Evaluation System Prompt]:::logic
    J[(Final Scorecard <br/> Strengths & Weaknesses)]:::output

    %% Flow Paths
    A -->|Parameters| B
    B --> C
    C -->|Behavioral| D
    C -->|Hard Skills| E
    
    D -->|Context| F
    E -->|Context| F
    
    F --> G
    G --> H
    H -->|Append to Chat History| F
    
    H -.->|End Interview| I
    I -->|Full Transcript| F
    F -->|Generate Report| J
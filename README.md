# Talentrix: HR & Technical Interview Evaluator

![Talentrix Architecture](https://img.shields.io/badge/Architecture-Modular-blue)
![Status](https://img.shields.io/badge/Status-Deployed-green)

Talentrix is an enterprise-grade AI-powered platform designed to automate, standardize, and elevate the technical interview process. It provides objective, real-time, and actionable feedback for candidates across technical and behavioral dimensions.

## 🏗️ System Architecture
The application follows a decoupled, modular design to ensure high performance and maintainability.

```mermaid
graph TD
    User[User/Candidate] -->|Interacts| UI[Streamlit Frontend]
    UI -->|Sends Input| Engine[Inference Engine - engine.py]
    Engine -->|Calls API| Groq[Groq LLM API]
    Groq -->|Returns Response| Engine
    Engine -->|Processes & Stores| State[Session State]
    UI -->|Triggers| Eval[Evaluation Layer - evaluate.py]
    Eval -->|Generates| Scorecard[HR Scorecard]
    
    subgraph "Deployment Environment"
    UI
    Engine
    Eval
    State
    end
    
    subgraph "Security Layer"
    Secrets[secrets.toml] -.->|Injected| Engine
    end
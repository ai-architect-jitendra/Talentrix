# Talentrix: Standard Operating Procedure (SOP)

## 1. Environment Setup & Configuration
* **Clone Repository:** `git clone https://github.com/YOUR_USERNAME/Talentrix.git`
* **Install Dependencies:** `pip install -r requirements.txt`
* **Security Layer:** 
    * Create a hidden folder: `.streamlit`
    * Create file: `secrets.toml`
    * Add your API key: `GROQ_API_KEY = "your_actual_api_key"`
* **Safety:** The `.gitignore` file is pre-configured to prevent sensitive files (`secrets.toml`, `__pycache__`) from being committed to the public repository.

## 2. Operational Workflow
1. **Launch Application:** Run `streamlit run main.py` in your terminal.
2. **Session Initialization:** The `setup.py` module parses candidate resumes/input.
3. **Interview Engine:** The `engine.py` module manages the LLM persona, utilizing sliding window memory to maintain context throughout the interview.
4. **Evaluation:** Upon completion, the `evaluate.py` module processes the entire chat history and generates a structured HR scorecard.

## 3. Deployment & Production
* **Platform:** Hosted on [Streamlit Community Cloud](https://share.streamlit.io/).
* **CI/CD:** The application is linked to the GitHub `main` branch. Every commit to `main` automatically triggers a production re-build.
* **Credential Handling:** Production API keys are injected via the Streamlit "Advanced Settings" portal, ensuring they are never hardcoded.

## 4. Maintenance & Security
* **Dependency Updates:** If you add new libraries, update `requirements.txt` and push to `main` to trigger an auto-rebuild.
* **Security Rotation:** To update API keys, log into the Streamlit Cloud dashboard, navigate to your app's "Advanced Settings," and update the secrets block.
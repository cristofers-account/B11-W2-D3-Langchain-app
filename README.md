# LangChain & LangSmith Quickstart

A clean, beginner-to-medium level Python implementation demonstrating how to connect the **LangChain framework** with **OpenAI's chat models** while enabling automated run tracking, latency metrics, and input/output visibility via the **LangSmith dashboard**.

## 🛠️ Features
- **LangChain Integration:** Communicates with OpenAI models natively through the framework ecosystem.
- **Automated Tracing:** Seamless connection to LangSmith to observe prompts, responses, token usage, and latency.
- **Security First:** Zero hard-coded keys; fully powered by system environment variables.
- **Single-File Architecture:** Keep configurations lightweight and easy to follow inside `main.py`.

## 📋 Prerequisites
Ensure you have the following credentials ready:
- An [OpenAI API Key](https://openai.com)
- A [LangSmith API Key](https://langchain.com)

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com
cd langchain-langsmith-quickstart
```

### 2. Set Up a Virtual Environment
```bash
# Create environment
python -m venv venv

# Activate environment
# On macOS/Linux:
source venv/bin/activate
# On Windows (Command Prompt):
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install langchain-openai dotenv
```

### 4. Configure Environment Variables
Set your secret keys in your current terminal session before launching the application.

**macOS/Linux:**
```bash
export OPENAI_API_KEY="your-openai-api-key"
export LANGSMITH_API_KEY="your-langsmith-api-key"
export LANGSMITH_TRACING="true"
export LANGSMITH_PROJECT="LangChain-Quickstart"
```

**Windows (Command Prompt):**
```cmd
set OPENAI_API_KEY=your-openai-api-key
set LANGSMITH_API_KEY=your-langsmith-api-key
set LANGSMITH_TRACING=true
set LANGSMITH_PROJECT=LangChain-Quickstart
```

### 5. Run the Application
```bash
python main.py
```

## 📊 Viewing Dashboard Traces
Once execution finishes successfully:
1. Navigate to your [LangSmith Dashboard](https://langchain.com).
2. Select the `LangChain-Quickstart` project.
3. Click on the latest run trace to inspect the precise response breakdown, execution latency, and token consumption graphs.

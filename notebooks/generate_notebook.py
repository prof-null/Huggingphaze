import nbformat as nbf
from datetime import datetime
import os

# Pull secrets from environment (GitHub Actions)
openrouter_key = os.getenv("OPENROUTER_API_KEY")
hf_key = os.getenv("HUGGINGFACE_API_KEY")

nb = nbf.v4.new_notebook()
cells = []

# Title
cells.append(nbf.v4.new_markdown_cell(
    f"# Huggingphaze Notebook\nGenerated: {datetime.utcnow()} UTC"
))

# Intro
cells.append(nbf.v4.new_markdown_cell(
    "This notebook was automatically generated.\n\n"
    "⚠️ API keys are handled securely via environment variables."
))

# Config cell
cells.append(nbf.v4.new_code_cell("""config = {
    "name": "SupportBot",
    "tone": "friendly",
    "platform": "web"
}

config"""))

# Chatbot logic
cells.append(nbf.v4.new_code_cell("""def chatbot_response(user_input):
    return f"Hello! You said: {user_input}"

chatbot_response("Test message")"""))

# Secure API section
cells.append(nbf.v4.new_markdown_cell("## Secure API Integration"))

cells.append(nbf.v4.new_code_cell("""import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

if not OPENROUTER_API_KEY and not HUGGINGFACE_API_KEY:
    print("⚠️ No API keys found. Add them as environment variables.")
else:
    print("✅ API keys detected (hidden for security)")"""))

# Example API call (safe template)
cells.append(nbf.v4.new_code_cell("""import requests

def example_openrouter_call(prompt):
    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        return "Missing API key"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=data
    )

    return response.json()

# example_openrouter_call("Hello world")
"""))

nb['cells'] = cells

# Ensure folder exists
os.makedirs("notebooks", exist_ok=True)

with open("notebooks/huggingphaze_notebook.ipynb", "w") as f:
    nbf.write(nb, f)

print("✅ Notebook generated securely!")
